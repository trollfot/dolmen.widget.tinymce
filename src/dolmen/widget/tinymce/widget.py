# -*- coding: utf-8 -*-

import grokcore.view as grok
import megrok.z3cform.base as z3cform
from zope.interface import Interface
from zope.schema.interfaces import IText
from dolmen.widget.tinymce import JqueryTinyMCE
from z3c.form.widget import FieldWidget
from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.interfaces import IFieldWidget, IFormLayer
from z3c.form.interfaces import IField, INPUT_MODE, DISPLAY_MODE


class TinyMCEWidget(TextAreaWidget):
    """A textarea widget with a tinyMCE editor.
    """   
    @property
    def script(self):
        JqueryTinyMCE.need()
        return """<script type="text/javascript">
          $(document).ready(function(){
          $('textarea[name="%s"]').tinymce();
        });
        </script>""" % self.name


class RichWidgetInput(z3cform.WidgetTemplate):
    grok.context(Interface)
    grok.layer(IFormLayer)
    grok.template('templates/input.pt')
    z3cform.directives.widget(TinyMCEWidget)
    z3cform.directives.mode(INPUT_MODE)


class RichWidgetDisplay(z3cform.WidgetTemplate):
    grok.context(Interface)
    grok.layer(IFormLayer)
    grok.template('templates/display.pt')
    z3cform.directives.widget(TinyMCEWidget)
    z3cform.directives.mode(DISPLAY_MODE)


@grok.adapter(IText, IFormLayer)
@grok.implementer(IFieldWidget)
def TinyMCEWidgetFactory(field, request):
    """IFieldWidget factory for TinyMCEWidget."""
    return FieldWidget(field, TinyMCEWidget(request))