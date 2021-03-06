# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Fri Nov 19 23:03:36 2010

import wx
import os.path
import Camera
# begin wxGlade: extracode

# end wxGlade

class Main(wx.Frame):
	def __init__(self, *args, **kwds):
		devices = []
		#a piece of crap
		if os.path.exists("/dev/video0"):
			devices.append("/dev/video0")
		if os.path.exists("/dev/video1"):
			devices.append("/dev/video1")
		if os.path.exists("/dev/video2"):
			devices.append("/dev/video2")
		if os.path.exists("/dev/video3"):
			devices.append("/dev/video3")
		# begin wxGlade: Main.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.videodev = wx.Choice(self, -1, choices=devices)
		self.resolution = wx.Choice(self, -1, choices=["1280x1024", "1280x900", "800x600", "640x480", "320x240"])
		self.takephoto = wx.Button(self, -1, "Photo")
		self.takevideo = wx.Button(self, -1, "Video")
		self.closecam = wx.Button(self, -1, "Close Camera")
		self.brightness_l = wx.StaticText(self, -1, "brightness")
		self.bright = wx.Slider(self, -1, 0, 0, 255)
		self.contrast_l = wx.StaticText(self, -1, "Contrast")
		self.bright_copy = wx.Slider(self, -1, 0, 0, 255)
		self.saturation_l = wx.StaticText(self, -1, "Saturation")
		self.bright_copy_1 = wx.Slider(self, -1, 0, 0, 255)
		self.hue_l = wx.StaticText(self, -1, "Hue")
		self.bright_copy_2 = wx.Slider(self, -1, 0, 0, 255)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_CHOICE, self.printselection, self.videodev)
		self.Bind(wx.EVT_CHOICE, self.setResolution, self.resolution)
		self.Bind(wx.EVT_BUTTON, self.takePhoto, self.takephoto)
		self.Bind(wx.EVT_BUTTON, self.takeVideo, self.takevideo)
		self.Bind(wx.EVT_BUTTON, self.closeCam, self.closecam)
		# end wxGlade
		self.camera = Camera.Camera()

	def __set_properties(self):
		# begin wxGlade: Main.__set_properties
		self.SetTitle("Pyclops")
		self.SetSize((340, 450))
		self.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.SetForegroundColour(wx.Colour(109, 0, 0))
		self.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.videodev.SetMinSize((120, 27))
		self.videodev.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.resolution.SetMinSize((120, 27))
		self.resolution.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.resolution.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
		self.resolution.SetSelection(3)
		self.takephoto.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.takevideo.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.closecam.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.brightness_l.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.brightness_l.SetForegroundColour(wx.Colour(0, 0, 0))
		self.brightness_l.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.bright.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.bright.SetForegroundColour(wx.Colour(0, 0, 0))
		self.bright.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
		self.bright.SetToolTipString("brightness")
		self.contrast_l.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.contrast_l.SetForegroundColour(wx.Colour(0, 0, 0))
		self.contrast_l.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.bright_copy.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.bright_copy.SetForegroundColour(wx.Colour(0, 0, 0))
		self.bright_copy.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
		self.bright_copy.SetToolTipString("brightness")
		self.saturation_l.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.saturation_l.SetForegroundColour(wx.Colour(0, 0, 0))
		self.saturation_l.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.bright_copy_1.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.bright_copy_1.SetForegroundColour(wx.Colour(0, 0, 0))
		self.bright_copy_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
		self.bright_copy_1.SetToolTipString("brightness")
		self.hue_l.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.hue_l.SetForegroundColour(wx.Colour(0, 0, 0))
		self.hue_l.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.bright_copy_2.SetBackgroundColour(wx.Colour(109, 0, 0))
		self.bright_copy_2.SetForegroundColour(wx.Colour(0, 0, 0))
		self.bright_copy_2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
		self.bright_copy_2.SetToolTipString("brightness")
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: Main.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_1 = wx.GridSizer(4, 2, 4, 4)
		sizer_1.Add(self.videodev, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 4)
		sizer_1.Add(self.resolution, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 4)
		sizer_1.Add(self.takephoto, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 4)
		sizer_1.Add(self.takevideo, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 4)
		sizer_1.Add(self.closecam, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 4)
		grid_sizer_1.Add(self.brightness_l, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_1.Add(self.bright, 0, wx.ALL|wx.EXPAND, 4)
		grid_sizer_1.Add(self.contrast_l, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_1.Add(self.bright_copy, 0, wx.ALL|wx.EXPAND, 4)
		grid_sizer_1.Add(self.saturation_l, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_1.Add(self.bright_copy_1, 0, wx.ALL|wx.EXPAND, 4)
		grid_sizer_1.Add(self.hue_l, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_1.Add(self.bright_copy_2, 0, wx.ALL|wx.EXPAND, 4)
		sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		self.Layout()
		# end wxGlade
	
	def printselection(self, event): # wxGlade: Main.<event_handler>
		self.camera.setCamDevice(self.videodev.GetStringSelection())
		event.Skip()

	def setResolution(self, event): # wxGlade: Main.<event_handler>
		if self.resolution.GetStringSelection() == "1280x1024":
			self.camera.setResolution(1280,1024)
		if self.resolution.GetStringSelection() == "1280x900":
			self.camera.setResolution(1280,900)
		if self.resolution.GetStringSelection() == "800x600":
			self.camera.setResolution(800,600)
		if self.resolution.GetStringSelection() == "640x480":
			self.camera.setResolution(640,480)
		if self.resolution.GetStringSelection() == "320x240":
			self.camera.setResolution(320,240)
		event.Skip()

	def takePhoto(self, event): # wxGlade: Main.<event_handler>
		self.videodev.Disable()
		self.resolution.Disable()
		self.camera.takePhoto()
		event.Skip()

	def takeVideo(self, event): # wxGlade: Main.<event_handler>
		self.videodev.Disable()
		self.resolution.Disable()
		self.takephoto.Disable()
		self.takevideo.Disable()
		self.camera.takeVideo()
		event.Skip()

	def closeCam(self, event): # wxGlade: Main.<event_handler>
		self.videodev.Enable()
		self.resolution.Enable()
		self.takevideo.Enable()
		self.takephoto.Enable()
		self.camera.closeCam()
		event.Skip()

# end of class Main


