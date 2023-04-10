# Generated by Django 4.0.10 on 2023-04-10 16:04

from django.db import migrations
import fulltext.db_indexes


class Migration(migrations.Migration):

	dependencies = [
		('fulltext', '0002_auto_20210619_0745'),
	]

	operations = [
		migrations.RemoveIndex(
			model_name='searchindex',
			name='fulltext_se_documen_498bf9_gin',
		),
		migrations.RemoveIndex(
			model_name='searchindex',
			name='fulltext_se_comment_079629_gin',
		),
		migrations.RemoveIndex(
			model_name='searchindex',
			name='fulltext_se_combine_008edf_gin',
		),
		migrations.AddIndex(
			model_name='searchindex',
			index=fulltext.db_indexes.RumIndex(fields=['document_search_vector'], name='document_search_vector_idx', opclasses=['rum_tsvector_ops']),
		),
		migrations.AddIndex(
			model_name='searchindex',
			index=fulltext.db_indexes.RumIndex(fields=['comments_search_vector'], name='comments_search_vector_idx', opclasses=['rum_tsvector_ops']),
		),
		migrations.AddIndex(
			model_name='searchindex',
			index=fulltext.db_indexes.RumIndex(fields=['combined_search_vector'], name='combined_search_vector_idx', opclasses=['rum_tsvector_ops']),
		),
	]
