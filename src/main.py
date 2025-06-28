import wx

from gui.main_frame import MainFrame


def main():
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
