# -*- coding: utf-8 -*-
from django import forms
from django.contrib.comments.forms import COMMENT_MAX_LENGTH
from django.forms import ChoiceField, ModelChoiceField
from django.forms.models import ModelChoiceIterator
from django.forms.widgets import RadioSelect, RadioFieldRenderer, RadioInput
from django.template.defaultfilters import capfirst
from django.utils.encoding import force_unicode
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from antispam.fields import AntispamField
from antispam.forms import AntispamMethodsMixin
from html_editor.fields import HtmlField
from models import Topic, Section


class SectionChoiceIterator(ModelChoiceIterator):
	def choice(self, obj):
		return (self.field.prepare_value(obj), self.field.label_from_instance(obj), obj.description)


class SectionModelChoiceField(ModelChoiceField):
	def _get_choices(self):
		return SectionChoiceIterator(self)
	choices = property(_get_choices, ChoiceField._set_choices)


class SectionRenderer(RadioFieldRenderer):
	def render_choice(self, idx):
		choice = self.choices[idx]
		return force_unicode(RadioInput(self.name, self.value, self.attrs.copy(), choice, idx)) + '<p class="radio-description">' + force_unicode(escape(choice[2])) + '</p>'

	def __iter__(self):
		for idx, choice in enumerate(self.choices):
			yield self.render_choice(idx)

	def __getitem__(self, idx):
		return self.render_choice(idx)


class TopicForm(forms.ModelForm, AntispamMethodsMixin):
	section = SectionModelChoiceField(Section.objects.all(), empty_label=None, widget = RadioSelect(renderer = SectionRenderer), label = capfirst(_('section')))
	text = HtmlField(label = _("Text"), max_length = COMMENT_MAX_LENGTH)
	captcha = AntispamField(required = True)

	def __init__(self, *args, **kwargs):
		logged = kwargs.pop('logged', False)
		request = kwargs.pop('request')
		super(TopicForm, self).__init__(*args, **kwargs)
		if logged:
			del(self.fields['authors_name'])
			del(self.fields['captcha'])
		self.process_antispam(request)

	class Meta:
		model = Topic
		exclude = ('author', 'time', )
		fields = ('section', 'authors_name', 'title', 'text', )
