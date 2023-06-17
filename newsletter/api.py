# -*- coding: utf-8 -*-
from datetime import timedelta, time, datetime
from typing import Tuple

from django.template.loader import select_template
from django.utils import timezone

from article.models import Article
from linuxos.templatetags.linuxos import get_base_uri


TimeRange = Tuple[datetime, datetime]


def get_week_date_range() -> TimeRange:
	today = timezone.now().date()

	week_start = today - timedelta(days=today.weekday())
	week_end = week_start + timedelta(days=7)

	midnight = time(0)
	tz = timezone.get_current_timezone()

	week_start = timezone.make_aware(datetime.combine(week_start, midnight), tz)
	week_end = timezone.make_aware(datetime.combine(week_end, midnight), tz)

	return (week_start, week_end)


def collect_articles(time_range: TimeRange):
	return Article.objects.order_by('pub_time').select_related('category').only('category', 'title', 'slug', 'original_perex', 'filtered_perex')


COLLECTORS = [
	{'name': 'article', 'verbose_name': "Články", 'fn': collect_articles}
]


def collect_activity(time_range: TimeRange):
	activity_sections = []

	for collector in COLLECTORS:
		context = collector.copy()

		collector_fn = context.pop('fn')

		items = collector_fn(time_range)
		if not items:
			continue

		base_name = context['name']

		context['base_uri'] = get_base_uri()
		context[f'{base_name}_list'] = items
		context[f'item_list'] = items

		html_list_template = select_template([f'newsletter/{base_name}_list.html', 'newsletter/list.html'])
		html_item_template = select_template([f'newsletter/{base_name}_item.html', 'newsletter/item.html'])
		txt_list_template = select_template([f'newsletter/{base_name}_list.txt', 'newsletter/list.txt'])
		txt_item_template = select_template([f'newsletter/{base_name}_item.txt', 'newsletter/item.txt'])

		html_rendered_items = []
		txt_rendered_items = []
		for item in items:
			context['item'] = item
			context[base_name] = item
			html_rendered_items.append(html_item_template.render(context))
			txt_rendered_items.append(txt_item_template.render(context))

		del context['item']
		del context[base_name]

		context['rendered_item_list'] = html_rendered_items
		context[f'rendered_{base_name}_list'] = html_rendered_items
		html_rendered_content = html_list_template.render(context)

		context['rendered_item_list'] = txt_rendered_items
		context[f'rendered_{base_name}_list'] = txt_rendered_items
		txt_rendered_content = txt_list_template.render(context)

		activity_sections.append({
			'html': html_rendered_content,
			'txt': txt_rendered_content,
		})

	return activity_sections


def send_weekly():
	activity = collect_activity(get_week_date_range())
	if not activity: # no updates, don't need to do anything
		return

	txt_content = ''.join(record['txt'] for record in activity)
	html_content = '\n'.join(record['html'] for record in activity)

	print(html_content)
