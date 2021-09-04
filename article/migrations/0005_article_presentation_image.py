# Generated by Django 3.2.4 on 2021-07-25 08:43
from django.db import migrations

import autoimagefield.fields
import linuxos.model_fields


class Migration(migrations.Migration):

	dependencies = [
		('attachment', '0003_auto_20170603_1644'),
		('article', '0004_auto_20170603_1644'),
	]

	operations = [
		migrations.AddField(
			model_name='article',
			name='presentation_image',
			field=linuxos.model_fields.PresentationImageField(),
		),
		migrations.AddField(
			model_name='category',
			name='image',
			field=autoimagefield.fields.AutoImageField(blank=True, upload_to='article/categories'),
		),
	]
