import pygame
from fb_settings import screen_height, screen_width, pipe_gap, scroll_speed
from options import spriteResize

class Pipe(pygame.sprite.Sprite):

	def __init__(self, x, y, position,pipeLimit, pipeHeight):
		pygame.sprite.Sprite.__init__(self)
		self.imageOrg = pygame.image.load("img/pipe.png")
		self.image = spriteResize(self.imageOrg, pygame, screen_width, screen_height)
		self.image = pygame.transform.scale(self.image, (self.image.get_width(), int(screen_height)))
		self.rect = self.image.get_rect()
		'''
		position variable determines if the pipe is coming from the bottom or top
		position 1 is from the top, -1 is from the bottom
		'''
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			if pipeLimit == pipeHeight:
				self.rect.bottomleft = [x, y - int(40)]
			else:
				self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
		elif position == -1:
			if pipeLimit == pipeHeight:
				self.rect.topleft = [x, y + int(40)]
			else:
				self.rect.topleft = [x, y + int(pipe_gap / 2)]
	

	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill()
			

def pipeGenerate(pipe_height, pipeUpperLimit, pipeLowerLimit, pipeHeightIncrement, flag):
	'''
	Takes args to generate pipe in the main loop.
	returns pipe height and flags
	'''
	if pipe_height >= pipeUpperLimit and flag == 1:
		pipe_height -= pipeHeightIncrement #	method to generate systematic pipes 
		if pipe_height <= pipeUpperLimit:
			pipe_height = pipeUpperLimit
			# pipe_height = int(max(pipeLowerLimit, -((screen_height - 200) / 2)))
			flag = 0
		return pipe_height, flag
			
	elif pipe_height <= pipeLowerLimit and flag == 0:
		pipe_height += pipeHeightIncrement
		if pipe_height >= pipeLowerLimit:
			pipe_height = pipeLowerLimit
			# pipe_height = int(min(pipeUpperLimit, ((screen_height - 200) / 2)))
			flag = 1
		return pipe_height, flag
