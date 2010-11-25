# -*- coding: utf-8 -*-
import pygame
import Image
from pygame.locals import *
import sys
from threading import Thread
import time
import cv

class Camera:
	def __init__(self, device = "/dev/video0", fps = 15, width = 640, height = 480):
		''''''
		self.device = device
		self.SetCamDevice(self.device)
		self.fps = fps
		self.width = width
		self.height = height
		self.vthread = None
		
	def SetCamDevice(self, device):
		'''A piece of crap!'''
		if device == "/dev/video0":
			self.camera = cv.CaptureFromCAM(0)
		if device == "/dev/video1":
			self.camera = cv.CaptureFromCAM(1)
		if device == "/dev/video2":
			self.camera = cv.CaptureFromCAM(2)
		if device == "/dev/video3":
			self.camera = cv.CaptureFromCAM(3)

	def SetFPS(self, fps):
		self.fps = fps

	def SetDimensions(self, width, height):
		self.width = width
		self.height = height

	def takePhoto(self):
		self.window = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption("Pyclops")
		self.screen = pygame.display.get_surface()
		im = self.get_image()
		pg_img = pygame.image.frombuffer(im.tostring(), cv.GetSize(im), "RGB")
		self.screen.blit(pg_img, (0,0))
		pygame.display.flip()

	def takeVideo(self):
		self.vthread = VideoThread(self)

	def closeCam(self):
		if self.vthread != None:
			self.vthread.keepgoing = False
			time.sleep(0.25)
		pygame.display.quit()
		self.camera = None
		self.SetCamDevice(self.device)
		#cv.ReleaseCapture(self.camera)

	def get_image(self):
		im = cv.QueryFrame(self.camera)
		return im
	
class VideoThread(Thread):
	"""Video Thread Class."""
	def __init__(self, camera):
		"""Init Video Thread Class."""
		Thread.__init__(self)
		self.camera = camera
		self.keepgoing = True
		self.start()    # start the thread

	def run(self):
		"""Run Worker Thread."""
		# This is the code executing in the new thread.
		self.camera.window = pygame.display.set_mode((self.camera.width,self.camera.height))
		pygame.display.set_caption("Pyclops")
		self.camera.screen = pygame.display.get_surface()
		grabeframes = False
		i = 0
		while self.keepgoing:
			events = pygame.event.get()
			for event in events:
				if event.type == QUIT:
					self.camera.closeCam()
					return
				if event.type == KEYDOWN:
					grabeframes = not grabeframes
			im = self.camera.get_image()
			if grabeframes:
				cv.SaveImage("/tmp/shot"+str(i)+".jpg", im)
				i+=1
			pg_img = pygame.image.frombuffer(im.tostring(), cv.GetSize(im), "RGB")
			self.camera.screen.blit(pg_img, (0,0))
			pygame.display.flip()
			pygame.time.delay(int(1000 * 1.0/self.camera.fps))
 
