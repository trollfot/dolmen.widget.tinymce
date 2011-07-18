# -*- coding: utf-8 -*-

from os import path
from dolmen.forms.base.markers import ModeMarker
from dolmen.forms.base.widgets import DisplayFieldWidget
from dolmen.forms.ztk.widgets import text
from dolmen.template import TALTemplate
from dolmen.widget.tinymce import JqueryTinyMCE
from grokcore.component import name, adapts
from zope.interface import Interface

TEMPLATE_DIR = path.join(path.dirname(__file__), 'templates')
TINYMCE_INPUT = ModeMarker('TINYMCE.INPUT')
TINYMCE_DISPLAY = ModeMarker('TINYMCE.DISPLAY', extractable=False)


class TinyMCEWidget(text.TextFieldWidget):
    """A textarea widget with a tinyMCE editor.
    """
    name(str(TINYMCE_INPUT))
    adapts(text.TextSchemaField, Interface, Interface)

    template = TALTemplate(path.join(TEMPLATE_DIR, 'input.pt'))

    @property
    def script(self):
        JqueryTinyMCE.need()
        return """<script type="text/javascript">
          $(document).ready(function() {
          $('textarea[name="%s"]').tinymce();
        });
        </script>""" % self.identifier


class RichWidgetDisplay(DisplayFieldWidget):
    name(str(TINYMCE_DISPLAY))
    adapts(text.TextSchemaField, Interface, Interface)

    template = TALTemplate(path.join(TEMPLATE_DIR, 'display.pt'))
