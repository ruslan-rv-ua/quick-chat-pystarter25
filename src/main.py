import wx

from main_frame import MainFrame


def main():
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
