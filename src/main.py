import wx
from main_frame import MainWindow


def main():
    app = wx.App()
    frame = MainWindow(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
