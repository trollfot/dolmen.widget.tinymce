# -*- coding: utf-8 -*-

import grok
from megrok import resourcelibrary
from menhir.library.tinyMCE import TinyMCE
from menhir.library.jquery import JQueryBase


class JqueryTinyMCE(resourcelibrary.ResourceLibrary):
    grok.name('dolmen.widget.tinymce')
    resourcelibrary.depend(TinyMCE)
    resourcelibrary.depend(JQueryBase)
    resourcelibrary.directory('resources')
    resourcelibrary.include('jquery_tiny_mce.js')
