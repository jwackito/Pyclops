# -*- coding: utf-8 -*-
import pygame
import Image
from pygame.locals import *
import sys

import cv

class Camera:
	def __init__(self, device = "/dev/video0", fps = 15, width = 640, height = 480):
		''''''
		self.SetCamDevice(device)
		self.fps = fps
		self.width = width
		self.height = height
		self.window = pygame.display.set_mode((width,height))
		pygame.display.set_caption("Pyclops")
		self.screen = pygame.display.get_surface()
		
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
		else:
			self.camera = cv.CaptureFromCAM(0)

	def SetFPS(self, fps):
		self.fps = fps

	def SetDimensions(self, width, height):
		self.width = width
		self.height = height

	def takeShot(self):
		im = self._get_image()
		print im
		pg_img = pygame.image.frombuffer(im.tostring(), cv.GetSize(im), "RGB")
		self.screen.blit(pg_img, (0,0))
		pygame.display.flip()

	def _get_image(self):
		im = cv.QueryFrame(self.camera)
		return im