# -*- coding: utf-8 -*-

import grokcore.view as grok
from zope.interface import Interface
from zope.schema.interfaces import IText
from dolmen.widget.tinymce import JqueryTinyMCE
from zeam.form.ztk.widgets import text
from zeam.form.base.widgets import DisplayFieldWidget

grok.templatedir('templates')


class TinyMCEWidget(text.TextFieldWidget):
    """A textarea widget with a tinyMCE editor.
    """
    grok.name('tinymce.input')
    grok.template('input')
    grok.adapts(text.TextSchemaField, Interface, Interface)

    @property
    def script(self):
        JqueryTinyMCE.need()
        return """<script type="text/javascript">
          $(document).ready(function(){
          $('textarea[name="%s"]').tinymce();
        });
        </script>""" % self.identifier


class RichWidgetDisplay(DisplayFieldWidget):
    grok.name('tinymce.display')
    grok.template('display')
    grok.adapts(text.TextSchemaField, Interface, Interface)
