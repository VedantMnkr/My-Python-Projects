import pygame


class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def draw(self, screen):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			'''
			check mouseover and clicked conditions
			'''
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action
	

class Heart:
	def __init__(self, image, x, y) -> None:
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
	
	def draw(self, lives, screen):
		for i in range(1,lives+1):
			distance = i * ((self.image.get_width() // 2) + 25)
			screen.blit(self.image, (self.rect.x + distance, self.rect.y))