# Copyright (c) 2011-2012 EditorConfig Team
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import gedit
import gtk
from shared import EditorConfigPluginMixin

class EditorConfigPlugin(gedit.Plugin, EditorConfigPluginMixin):
    def activate(self, window):
        handler_id = window.connect('active_tab_state_changed', self.set_config)
        window.set_data(self.HANDLER_NAME, handler_id)
        self.exec_path_buffer = gtk.TextBuffer()

    def get_document_properties(self, document):
        """Call EditorConfig core and return properties dict for document"""

        if document:
            file_uri = document.get_uri()
            if file_uri and file_uri.startswith("file:///"):
                return self.get_properties_from_filename(file_uri[7:])
        return {}

    def deactivate(self, window):
        handler_id = window.get_data(self.HANDLER_NAME)
        window.disconnect(handler_id)
        window.set_data(self.HANDLER_NAME, None)
