# -*- coding: utf-8 -*-
import pygame
import Image
from pygame.locals import *
import sys

import cv

class Camera:
	def __init__(self, device = "/dev/video0", fps = 15, width = 640, height = 480):
		''''''
		self.device = device
		self.SetCamDevice(self.device)
		self.fps = fps
		self.width = width
		self.height = height
		
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
		self.window = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption("Pyclops")
		self.screen = pygame.display.get_surface()
		grabeframes = False
		i = 0
		while True:
			events = pygame.event.get()
			for event in events:
				if event.type == QUIT:
					self.closeCam()
					return
				if event.type == KEYDOWN:
					grabeframes = not grabeframes
			im = self.get_image()
			if grabeframes:
				cv.SaveImage("/tmp/shot"+str(i)+".jpg", im)
				i+=1
			pg_img = pygame.image.frombuffer(im.tostring(), cv.GetSize(im), "RGB")
			self.screen.blit(pg_img, (0,0))
			pygame.display.flip()
			pygame.time.delay(int(1000 * 1.0/self.fps))

	def closeCam(self):
		pygame.display.quit()
		self.camera = None
		self.SetCamDevice(self.device)
		#cv.ReleaseCapture(self.camera)

	def get_image(self):
		im = cv.QueryFrame(self.camera)
		return im