from pathlib import Path

import wx
import wx.html2
from ObjectListView3 import ColumnDefn, ObjectListView

from templates.marked import Template


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Quick Chat")
        self.init_ui()
        self.template = Template("marked.html")
        self.about_html = self.template.render_file(
            Path(__file__).parent / "about.md", title="Про програму", lang="uk"
        )
        self.setup_demo_data()

    def setup_demo_data(self):
        self.messages_list_view.SetObjects(
            [
                {"message": "Це типу повідомлення користувача"},
                {"message": "Це типу повідомлення нейронки"},
            ]
        )
        self.messages_list_view.Select(0)
        self.messages_list_view.Focus(0)
        self.webview.SetPage(self.about_html, "")

    def init_ui(self):
        panel = wx.Panel(self)

        # Left: ObjectListView for messages and TextCtrl for user input
        message_input_sizer = wx.BoxSizer(wx.VERTICAL)
        self.messages_list_view = ObjectListView(panel, style=wx.LC_REPORT)
        self.messages_list_view.SetColumns(
            [
                ColumnDefn(title="Message", valueGetter="message", isSpaceFilling=True),
            ]
        )
        # Add label for user input
        user_input_label = wx.StaticText(parent=panel, label="Введіть повідомлення:")
        self.user_input = wx.TextCtrl(parent=panel, style=wx.TE_MULTILINE)
        message_input_sizer.Add(self.messages_list_view, 1, wx.EXPAND | wx.ALL, 5)
        message_input_sizer.Add(user_input_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 5)
        message_input_sizer.Add(self.user_input, 0, wx.EXPAND | wx.ALL, 5)

        # Right: wx.html2.WebView
        self.webview = wx.html2.WebView.New(panel)

        # Set up the main sizer
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(message_input_sizer, 2, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.webview, 2, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(main_sizer)
        self.Maximize()
