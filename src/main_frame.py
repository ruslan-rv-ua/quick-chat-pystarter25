import wx
import wx.html2
from ObjectListView3 import ColumnDefn, ObjectListView


from webview_marked import WebviewMarked


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        message_input_sizer = wx.BoxSizer(wx.VERTICAL)
        self.messages_olv = ObjectListView(panel, style=wx.LC_REPORT)
        self.messages_olv.SetColumns(
            [
                ColumnDefn(title="Message", valueGetter="message", isSpaceFilling=True),
            ]
        )
        self.user_input = wx.TextCtrl(
            panel, style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER
        )
        message_input_sizer.Add(self.messages_olv, 1, wx.EXPAND | wx.ALL, 5)
        message_input_sizer.Add(self.user_input, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(message_input_sizer, 2, wx.EXPAND | wx.ALL, 5)

        # Right: wx.html2.WebView
        self.webview = wx.html2.WebView.New(panel)
        main_sizer.Add(self.webview, 2, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(main_sizer)
        self.Maximize()
        
