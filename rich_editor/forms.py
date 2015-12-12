# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import CharField

from .parser import HtmlParser
from .syntax import highlight_pre_blocks
from .widgets import RichOriginalEditor, RichEditor


class RichTextField(CharField):
	widget = RichEditor

	def __init__(self, *args, **kwargs):
		self.parser = kwargs.pop('parser', HtmlParser())
		super(RichTextField, self).__init__(*args, **kwargs)

	def widget_attrs(self, widget):
		attrs = super(RichTextField, self).widget_attrs(widget)
		attrs.update(self.parser.get_attributes())
		return attrs

	def clean(self, value):
		self.parser.parse(value)
		return self.parser.get_output()


class RichOriginalField(CharField):
	widget = RichOriginalEditor

	def __init__(self, parsers, parsers_conf, *args, **kwargs):
		self.parsers = parsers
		self.parsers_conf = parsers_conf
		super(RichOriginalField, self).__init__(*args, **kwargs)

	def widget_attrs(self, widget):
		attrs = super(RichOriginalField, self).widget_attrs(widget)
		attrs['parsers_conf'] = self.parsers_conf
		for parser in self.parsers.values():
			attrs.update(parser.get_attributes())
		return attrs

	def clean(self, value):
		fmt = value.field_format
		txt = super(RichOriginalField, self).clean(value.field_text)
		parser = self.parsers.get(fmt, self.parsers[fmt])
		parser.parse(txt)
		parsed = parser.get_output()
		parsed = highlight_pre_blocks(parsed)
		return (fmt, txt, parsed)
