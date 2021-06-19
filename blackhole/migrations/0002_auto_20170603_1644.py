# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 14:44
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

	dependencies = [
		('blackhole', '0001_initial'),
	]

	operations = [
		migrations.AlterField(
			model_name='file',
			name='node',
			field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blackhole.Node'),
		),
		migrations.AlterField(
			model_name='node',
			name='author',
			field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
		),
		migrations.AlterField(
			model_name='noderevision',
			name='author',
			field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
		),
		migrations.AlterField(
			model_name='term',
			name='parent',
			field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='blackhole.Term'),
		),
		migrations.AlterField(
			model_name='term',
			name='vocabulary',
			field=models.ForeignKey(db_column='vid', on_delete=django.db.models.deletion.PROTECT, to='blackhole.VocabularyNodeType'),
		),
	]
