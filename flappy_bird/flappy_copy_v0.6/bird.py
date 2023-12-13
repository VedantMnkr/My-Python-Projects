import pygame
from fb_settings import flying, game_over, screen_height, screen_width
from options import spriteResize

class Bird(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range (1, 4):
			imgOrg = pygame.image.load(f"img/bird{num}.png")
			img = spriteResize(imgOrg, pygame, screen_width, screen_height)
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False

	def update(self):

		if flying == True:
			#apply gravity
			# self.vel += 0.5  # used to increase y velocity downwards continously
			if self.vel > 8:
				self.vel = 8
			if self.rect.bottom < 768:
				self.rect.y += int(self.vel)

		if game_over == False:

			#jump // orginal mechanic
			# if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
			# 	self.clicked = True
			# 	self.vel = -10
			# if pygame.mouse.get_pressed()[0] == 0:
			# 	self.clicked = False

			# controlled by mouse
			if pygame.mouse.get_pressed()[0] == 1:
				self.clicked = True
				self.x_mouse_pos ,self.y_mouse_pos = pygame.mouse.get_pos()
				self.rect.y = self.y_mouse_pos
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False


			#handle the animation
			flap_cooldown = 5
			self.counter += 1
			
			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
				self.image = self.images[self.index]


			#rotate the bird
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			#point the bird at the ground
			self.image = pygame.transform.rotate(self.images[self.index], -90)