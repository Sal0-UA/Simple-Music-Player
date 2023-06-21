# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Simple Music Player", pos = wx.DefaultPosition, size = wx.Size( 300,486 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		MainSizer = wx.BoxSizer( wx.VERTICAL )

		Sizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.AuthorButton = wx.Button( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.Size( -1,35 ), 0|wx.BORDER_NONE )
		self.AuthorButton.SetLabelMarkup( u"Author" )
		self.AuthorButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.AuthorButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.AuthorButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer1.Add( self.AuthorButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Label1 = wx.StaticText( self, wx.ID_ANY, u"Songs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Label1.Wrap( -1 )

		self.Label1.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.Label1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		Sizer1.Add( self.Label1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.SettingsButton = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,40 ), 0|wx.BORDER_NONE )
		self.SettingsButton.SetLabelMarkup( wx.EmptyString )
		self.SettingsButton.SetBitmap( wx.Bitmap( u"pics/settings.png", wx.BITMAP_TYPE_ANY ) )
		self.SettingsButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.SettingsButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SettingsButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		Sizer1.Add( self.SettingsButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		MainSizer.Add( Sizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LI_HORIZONTAL )
		self.m_staticline1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticline1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		MainSizer.Add( self.m_staticline1, 0, wx.ALL, 5 )

		TracksListChoices = [ u"Song1 - Author1 | 0:00", u"Song2 - Author 2 | 0:00", u"Song3 - Author3 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00", u"Song4 - Author4 | 0:00" ]
		self.TracksList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, TracksListChoices, 0|wx.BORDER_NONE|wx.VSCROLL )
		self.TracksList.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.TracksList.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.TracksList.SetMinSize( wx.Size( -1,250 ) )

		MainSizer.Add( self.TracksList, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		Sizer2 = wx.GridSizer( 0, 3, 0, 0 )

		self.AddTrackButton = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.AddTrackButton.SetLabelMarkup( u"Add" )
		self.AddTrackButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.AddTrackButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.AddTrackButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer2.Add( self.AddTrackButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.RemoveTrackButton = wx.Button( self, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.RemoveTrackButton.SetLabelMarkup( u"Remove" )
		self.RemoveTrackButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.RemoveTrackButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.RemoveTrackButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer2.Add( self.RemoveTrackButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ClearTracksButton = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.ClearTracksButton.SetLabelMarkup( u"Clear" )
		self.ClearTracksButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.ClearTracksButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.ClearTracksButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer2.Add( self.ClearTracksButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		MainSizer.Add( Sizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline2.SetMinSize( wx.Size( 300,-1 ) )

		MainSizer.Add( self.m_staticline2, 0, wx.ALL, 5 )

		Sizer3 = wx.GridSizer( 0, 5, 0, 0 )

		self.PreviousTrackButton = wx.Button( self, wx.ID_ANY, u"⏮", wx.DefaultPosition, wx.Size( 50,-1 ), 0|wx.BORDER_NONE )
		self.PreviousTrackButton.SetLabelMarkup( u"⏮" )
		self.PreviousTrackButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.PreviousTrackButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.PreviousTrackButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer3.Add( self.PreviousTrackButton, 0, wx.ALL, 5 )

		self.RepeatTrackButton = wx.Button( self, wx.ID_ANY, u"⏪", wx.DefaultPosition, wx.Size( 50,-1 ), 0|wx.BORDER_NONE )
		self.RepeatTrackButton.SetLabelMarkup( u"⏪" )
		self.RepeatTrackButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.RepeatTrackButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.RepeatTrackButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer3.Add( self.RepeatTrackButton, 0, wx.ALL, 5 )

		self.PausePlayTrackButton = wx.Button( self, wx.ID_ANY, u"⏯", wx.DefaultPosition, wx.Size( 50,-1 ), 0|wx.BORDER_NONE )
		self.PausePlayTrackButton.SetLabelMarkup( u"⏯" )
		self.PausePlayTrackButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.PausePlayTrackButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.PausePlayTrackButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer3.Add( self.PausePlayTrackButton, 0, wx.ALL, 5 )

		self.SkipTrackButton = wx.Button( self, wx.ID_ANY, u"⏩", wx.DefaultPosition, wx.Size( 50,-1 ), 0|wx.BORDER_NONE )
		self.SkipTrackButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.SkipTrackButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SkipTrackButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer3.Add( self.SkipTrackButton, 0, wx.ALL, 5 )

		self.NextTrackButton = wx.Button( self, wx.ID_ANY, u"⏭", wx.DefaultPosition, wx.Size( 50,-1 ), 0|wx.BORDER_NONE )
		self.NextTrackButton.SetLabelMarkup( u"⏭" )
		self.NextTrackButton.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.NextTrackButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.NextTrackButton.SetBackgroundColour( wx.Colour( 81, 81, 81 ) )

		Sizer3.Add( self.NextTrackButton, 0, wx.ALL, 5 )


		MainSizer.Add( Sizer3, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Sizer4 = wx.BoxSizer( wx.VERTICAL )

		self.TrackGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 300,3 ), wx.GA_HORIZONTAL )
		self.TrackGauge.SetValue( 50 )
		self.TrackGauge.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		Sizer4.Add( self.TrackGauge, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		MainSizer.Add( Sizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( MainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


