import pygame
from fb_settings import scroll_speed, screen_height, screen_width
from options import spriteResize


class Bugga(pygame.sprite.Sprite):

	def __init__(self, x, y, bugga_img):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = bugga_img
		self.image = spriteResize(self.image, pygame, screen_width, screen_height)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self, bugga_drawn):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill() 
		
		if bugga_drawn == True:
			bugga_drawn = False
			# acc = 8000
			# global pipe_frequency
			# pipe_frequency = (8000 + acc )/ scroll_speed