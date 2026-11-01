# -*- coding: utf-8 -*-
"""Document-independent modal WebView2 reader with an explicit WPF fallback."""
from __future__ import unicode_literals

import os

from compass.library import library_directory, read_document_text, reader_documents, verify_library


def create_reader_window(force_fallback=False, collection='compass'):
    """Construct without showing; useful for isolated real-WPF lifecycle acceptance."""
    if collection != 'compass':
        raise ValueError('Bu bağımsız paket yalnız Compass mevzuatını içerir.')
    manifest = verify_library()
    documents = reader_documents(manifest, collection)
    collection_title = 'Parametrically Compass — Mevzuat Kitaplığı'
    import clr
    clr.AddReference('PresentationFramework')
    clr.AddReference('PresentationCore')
    clr.AddReference('WindowsBase')
    from System import Uri
    from System.Windows import Window, WindowStartupLocation, Thickness
    from System.Windows.Controls import DockPanel, Dock, ListBox, TextBox, TextBlock, Button, ScrollBarVisibility
    from System.Windows import TextWrapping

    class ReaderWindow(Window):
        def __init__(self):
            self.Title = collection_title
            self.Width, self.Height = 1280, 870
            self.MinWidth, self.MinHeight = 620, 480
            self.WindowStartupLocation = WindowStartupLocation.CenterScreen
            self.webview = None
            self.core = None
            self.handlers = []
            self.mode = 'initializing'
            self.failure_reason = ''
            self.Closed += self._closed
            self.Loaded += self._loaded
            self.entry_uri = Uri(os.path.join(library_directory(), 'index.html')).AbsoluteUri
            self.pdf_uri = Uri(os.path.join(library_directory(), 'sources', '20260805-2-1.pdf')).AbsoluteUri
            if force_fallback:
                self._fallback('WPF görünümü kullanıcı tarafından seçildi.')
            else:
                try:
                    self._webview()
                except Exception as error:
                    self._fallback('WebView2 başlatılamadı: ' + str(error))

        def _attach(self, obj, event, handler):
            getattr(obj, event).__iadd__(handler)
            self.handlers.append((obj, event, handler))

        def _dispose_webview(self):
            for obj, event, handler in reversed(self.handlers):
                try:
                    getattr(obj, event).__isub__(handler)
                except Exception:
                    pass
            self.handlers = []
            view, self.webview = self.webview, None
            self.core = None
            if view is not None:
                view.Dispose()

        def _webview(self):
            from pyrevit import BIN_DIR
            for name in ('Core', 'Wpf'):
                path = os.path.join(BIN_DIR, 'Microsoft.Web.WebView2.' + name + '.dll')
                clr.AddReferenceToFileAndPath(path)
            from Microsoft.Web.WebView2.Wpf import WebView2, CoreWebView2CreationProperties
            view = WebView2()
            self.webview = view
            properties = CoreWebView2CreationProperties()
            base = os.environ.get('LOCALAPPDATA') or os.environ.get('APPDATA')
            if not base:
                raise ValueError('Kullanıcı veri dizini bulunamadı.')
            properties.UserDataFolder = os.path.join(base, 'ParametricallyCompass', 'WebView2')
            view.CreationProperties = properties
            self._attach(view, 'NavigationStarting', self._navigation)
            self._attach(view, 'CoreWebView2InitializationCompleted', self._initialized)
            self.Content = view

        def _loaded(self, sender, args):
            # Initialize after the WPF host is loaded, with finalized creation properties.
            self.Loaded -= self._loaded
            if self.webview is not None:
                try:
                    self.webview.Source = Uri(self.entry_uri + '?collection=' + collection)
                except Exception as error:
                    self._fallback('WebView2 başlatılamadı: ' + str(error))

        def _navigation(self, sender, args):
            address = str(args.Uri).split('#', 1)[0].split('?', 1)[0]
            args.Cancel = address.lower() not in (self.entry_uri.lower(), self.pdf_uri.lower())

        def _new_window(self, sender, args):
            args.Handled = True
            allowed = ('https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2.htm',
                       'https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2-1.pdf')
            if str(args.Uri) in allowed:
                from System.Diagnostics import Process, ProcessStartInfo
                try:
                    start = ProcessStartInfo(str(args.Uri))
                    start.UseShellExecute = True
                    Process.Start(start)
                except Exception as error:
                    from pyrevit import forms
                    forms.alert('Kaynak tarayıcıda açılamadı.\n' + str(error), title=self.Title)

        def _external_scheme(self, sender, args):
            args.Cancel = True

        def _initialized(self, sender, args):
            if not args.IsSuccess:
                self._fallback('WebView2 çalışma ortamı açılamadı: ' + str(args.InitializationException))
                return
            try:
                self.core = self.webview.CoreWebView2
                settings = self.core.Settings
                settings.IsWebMessageEnabled = False
                settings.AreHostObjectsAllowed = False
                settings.AreDevToolsEnabled = False
                settings.AreDefaultScriptDialogsEnabled = False
                self._attach(self.core, 'NewWindowRequested', self._new_window)
                self._attach(self.core, 'FrameNavigationStarting', self._navigation)
                if hasattr(self.core, 'LaunchingExternalUriScheme'):
                    self._attach(self.core, 'LaunchingExternalUriScheme', self._external_scheme)
                self.mode = 'webview2'
            except Exception as error:
                self._fallback('WebView2 yapılandırılamadı: ' + str(error))

        def _fallback(self, reason):
            self.failure_reason = reason
            self._dispose_webview()
            self.mode = 'wpf'
            self.Title = collection_title + ' (WPF)'
            root = DockPanel()
            note = TextBlock()
            note.Text = reason + '\nMarkdown okuma görünümü. Ek tablolarını özgün PDF’den teyit edin.'
            note.TextWrapping = TextWrapping.Wrap
            note.Margin = Thickness(16)
            DockPanel.SetDock(note, Dock.Top)
            root.Children.Add(note)
            find = DockPanel()
            find.Margin = Thickness(16, 0, 16, 12)
            next_button = Button()
            next_button.Content = 'Sonrakini bul'
            next_button.MinWidth = 110
            DockPanel.SetDock(next_button, Dock.Right)
            find.Children.Add(next_button)
            self.find_text = TextBox()
            from System.Windows.Automation import AutomationProperties
            AutomationProperties.SetName(self.find_text, 'Seçili belgede ara')
            find.Children.Add(self.find_text)
            DockPanel.SetDock(find, Dock.Top)
            root.Children.Add(find)
            self.doc_list = ListBox()
            self.doc_list.Width = 245
            self.doc_list.Margin = Thickness(12)
            AutomationProperties.SetName(self.doc_list, 'Kitaplık belgeleri')
            for doc in documents:
                self.doc_list.Items.Add(doc['title'])
            DockPanel.SetDock(self.doc_list, Dock.Left)
            root.Children.Add(self.doc_list)
            self.body = TextBox()
            self.body.IsReadOnly = True
            self.body.AcceptsReturn = True
            self.body.TextWrapping = TextWrapping.Wrap
            self.body.VerticalScrollBarVisibility = ScrollBarVisibility.Auto
            self.body.Margin = Thickness(12)
            self.body.FontSize = 16
            AutomationProperties.SetName(self.body, 'Seçili belgenin Markdown metni')
            root.Children.Add(self.body)
            self.doc_list.SelectionChanged += self._document_changed
            next_button.Click += self._find_next
            self.fallback_find_button = next_button
            self.Content = root
            self.doc_list.SelectedIndex = 0

        def _document_changed(self, sender, args):
            index = self.doc_list.SelectedIndex
            if index >= 0:
                self.body.Text = read_document_text(documents[index]['file'])

        def _find_next(self, sender, args):
            from System import StringComparison
            query = self.find_text.Text
            if not query:
                return
            start = self.body.SelectionStart + self.body.SelectionLength
            index = self.body.Text.IndexOf(query, start, StringComparison.CurrentCultureIgnoreCase)
            if index < 0:
                index = self.body.Text.IndexOf(query, StringComparison.CurrentCultureIgnoreCase)
            if index >= 0:
                self.body.Select(index, len(query))
                self.body.ScrollToLine(self.body.GetLineIndexFromCharacterIndex(index))
                self.body.Focus()

        def _closed(self, sender, args):
            self.Closed -= self._closed
            self.Loaded -= self._loaded
            self._dispose_webview()
            if self.mode == 'wpf':
                self.doc_list.SelectionChanged -= self._document_changed
                self.fallback_find_button.Click -= self._find_next
            self.Content = None
            self.mode = 'closed'

    return ReaderWindow()


def launch_reader(force_fallback=False, collection='compass'):
    from pyrevit import forms
    try:
        window = create_reader_window(force_fallback=force_fallback, collection=collection)
        window.ShowDialog()
        return window
    except Exception as error:
        forms.alert('Standartlar kitaplığı açılamadı. Kaynak veya kurulum bütünlüğünü kontrol edin.\n' + str(error),
                    title='Parametrically Compass')
        return None
