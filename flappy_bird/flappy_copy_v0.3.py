import pygame
from pygame.locals import *
import random
from fb_settings import *

pygame.init()

clock = pygame.time.Clock()
fps = 60 # FPS LIMIT

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define font
font = pygame.font.SysFont('Bauhaus 93', 60)

#define game variables
ground_scroll = 0
flying = False
game_over = False


last_pipe = pipe_frequency
# last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

def spriteResize(oldSprite):
	widthMultiplier = oldSprite.get_width() / 864
	heightMultiplier = oldSprite.get_height() / 756
	newSprite = pygame.transform.scale(oldSprite, (int(widthMultiplier * screen_width), int(heightMultiplier * screen_height)))
	return newSprite


#	load images original
bgOrg = pygame.image.load('img/bg.png')
button_img = pygame.image.load('img/restart.png') # w 0.139 h 0.056
ground_imgOrg = pygame.image.load('img/ground.png')

# buttonImgResized = pygame.transform.scale(button_img, (int(0.139 * screen_width), int(0.056 * screen_height)))

#	Resized Images
buttonImgResized = spriteResize(button_img)
bg = spriteResize(bgOrg)
ground_img = spriteResize(ground_imgOrg)

# print(f'before resizing {button_img.get_width(), button_img.get_height()} after resizing {button_img.get_width() - (screen.get_width() - 864), button_img.get_height() - (screen.get_height() - 756)}')


#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y)) 

def reset_game():
	pipe_group.empty()	
	flappy.rect.x = 100  
	flappy.rect.y = int(screen_height / 2)
	score = 0
	return score


class Bird(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range (1, 4):
			imgOrg = pygame.image.load(f"img/bird{num}.png")
			img = spriteResize(imgOrg)
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



class Pipe(pygame.sprite.Sprite):

	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.imageOrg = pygame.image.load("img/pipe.png")
		self.image = spriteResize(self.imageOrg)
		self.rect = self.image.get_rect()
		#position variable determines if the pipe is coming from the bottom or top
		#position 1 is from the top, -1 is from the bottom
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
		elif position == -1:
			self.rect.topleft = [x, y + int(pipe_gap / 2)]


	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill()



class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action



pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)

#create restart button instance
button = Button(screen_width // 2 , screen_height // 2 , buttonImgResized)


run = True
while run:

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))

	pipe_group.draw(screen)
	bird_group.draw(screen)
	bird_group.update()

	#draw and scroll the ground
	screen.blit(ground_img, (ground_scroll, screen_height - (screen_height // 12)))

	#check the score
	if len(pipe_group) > 0:
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False
	draw_text(str(score), font, white, int(screen_width / 2), 20)


	#look for collision
	if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
		game_over = True
	#once the bird has hit the ground it's game over and no longer flying
	if flappy.rect.bottom >= 768:
		game_over = True
		flying = False


	if flying == True and game_over == False:
		# * generate new pipes
		time_now = pygame.time.get_ticks()
		if time_now - last_pipe > pipe_frequency:

			# ? pipe_height = random.randint(-100, 100)  # random method to generate pipe_height
			if pipe_height >= -200 and flag == 1:
				pipe_height -= 100 #	method to generate systematic pipes 
				if pipe_height == -200:
					flag = 0
			elif pipe_height <= 200 and flag == 0:
				pipe_height += 100
				if pipe_height == 200:
					flag = 1

			btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

		pipe_group.update()

		ground_scroll -= scroll_speed
		if abs(ground_scroll) > 35:
			ground_scroll = 0
	

	#check for game over and reset
	if game_over == True:
		if button.draw():
			game_over = False
			score = reset_game()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
			flying = True

	pygame.display.update()

pygame.quit()
