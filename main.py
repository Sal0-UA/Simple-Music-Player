import window
import wx


class MainApp(wx.App):
    def OnInit(self):
        mainFrame = window.MainFrame(None)
        mainFrame.Show(True)
        return True

# launching app


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
