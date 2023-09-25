'''
    - Now pipes dont draw out of the screen.
    - [MAJOR] added a bonus entity "bugga" that can be eaten by the brid to get bonus.
    - it spanwns between 2 pipes at a stipulated time.
    - Now game can be run for certain repetations.
    - and quality of life changes....
'''

import pygame
from pygame.locals import *
import random
from fb_settings import *


# ! ########################################################
# screen_width = 864
# screen_height = 756

# #define colours
# white = (255, 255, 255)
# acc = 0  # to increase the distance through time  between pipes
# # Game entites
# precision = 20
# pipe_gap = 40 + (precision * 4) # 40 -> bird height + (precision * 4 constant)
# scroll_speed = 5
# pipe_frequency = (8000 + acc )/ scroll_speed #milliseconds // frequency at which the pipe occurs
# speed = 10
# pipeHeightIncrement = speed * 4 * 2


# # angle = 90
# angleup  = 90
# angledown = 90
# pipe_height, flag = 0, 1 # 1 means its going up and 0 means downwards
# pipeUpperLimit = -(angleup * 4) #this goes up
# pipeLowerLimit = angledown * 4 #this goes down
# pipeHeightPiviot = -pipe_height
# ! ########################################################


pygame.init()

clock = pygame.time.Clock()
fps = 60 # FPS LIMIT

print(screen_height, screen_width)

screen = pygame.display.set_mode((screen_width, screen_height))
print(screen.get_width(), screen.get_height())

pygame.display.set_caption('Flappy Bird')

#define font
font = pygame.font.SysFont('Bauhaus 93', 60)

#define game variables
ground_scroll = 0
flying = False
game_over = False
bonus = False
bugga_drawn = False
bonus_pts = 0


# last_pipe = 0
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

def spriteResize(oldSprite, extraheight=0):
	widthMultiplier = oldSprite.get_width() / 864
	heightMultiplier = oldSprite.get_height() / 756
	newSprite = pygame.transform.scale(oldSprite, (int(widthMultiplier * screen_width), int(heightMultiplier * screen_height+extraheight)))
	return newSprite


#	load images original
bgOrg = pygame.image.load('img/bg.png')
button_img = pygame.image.load('img/restart.png') # w 0.139 h 0.056
ground_imgOrg = pygame.image.load('img/ground.png')
bugga_imgorg = pygame.image.load('img/bugga.png')
bugga_img = pygame.transform.scale(bugga_imgorg, (50, 50))

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


class Bugga(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = bugga_img
		self.image = spriteResize(self.image)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill() 
		
		global bugga_drawn
		if bugga_drawn == True:
			bugga_drawn = False
			# acc = 0
			# global pipe_frequency
			# pipe_frequency = (8000 + acc )/ scroll_speed

		


class Pipe(pygame.sprite.Sprite):

	def __init__(self, x, y, position,pipeLimit, pipeHeight):
		pygame.sprite.Sprite.__init__(self)
		self.imageOrg = pygame.image.load("img/pipe.png")
		self.image = spriteResize(self.imageOrg)
		self.image = pygame.transform.scale(self.image, (self.image.get_width(), int(screen_height)))
		self.rect = self.image.get_rect()
		#position variable determines if the pipe is coming from the bottom or top
		#position 1 is from the top, -1 is from the bottom
		
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
bugga_group = pygame.sprite.Group()


flappy = Bird(100, int((screen_height - 100) / 2))
print(flappy.image.get_width(), flappy.image.get_height())

bird_group.add(flappy)


#create restart button instance
button = Button(screen_width // 2 , screen_height // 2 , buttonImgResized)

previous_score = 0
bugga_generated  = False
run = True
while run:

	# * checks for certain no. of epochs
	if score == repetations:
		game_over = True
		flying = False

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))

	bugga_group.draw(screen)
	pipe_group.draw(screen)
	bird_group.draw(screen)
	bird_group.update()

	#draw and scroll the ground
	screen.blit(ground_img, (ground_scroll, screen_height + 100))
	
	# for debug
	# if game_over != True:
	# 	print(abs(((flappy.rect.y -  30 ) // 4)-90))

	
		
	
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

	
	current_score = score

	if current_score != previous_score:
		if (current_score + 1) % 5 == 0:
			bonus = True
		else:
			bonus = False
		previous_score = current_score
		print(f'bonus - {bonus}')


	#look for collision
	if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
		game_over = True
	#once the bird has hit the ground it's game over and no longer flying
	if flappy.rect.bottom >= screen_height + 50:
		game_over = True
		flying = False


	if flying == True and game_over == False :
		# * generate new pipes
		time_now = pygame.time.get_ticks()
		if time_now - last_pipe > pipe_frequency and bonus == False:
			print(f'time now {time_now} :::: time_now-lstpipe {time_now - last_pipe}')
			# ? pipe_height = random.randint(-100, 100)  # random method to generate pipe_height
	

			if pipe_height >= pipeUpperLimit and flag == 1:
				pipe_height -= pipeHeightIncrement #	method to generate systematic pipes 
				if pipe_height <= pipeUpperLimit:
					pipe_height = pipeUpperLimit
					# pipe_height = int(max(pipeLowerLimit, -((screen_height - 200) / 2)))
					flag = 0
			elif pipe_height <= pipeLowerLimit and flag == 0:
				pipe_height += pipeHeightIncrement
				if pipe_height >= pipeLowerLimit:
					pipe_height = pipeLowerLimit
					# pipe_height = int(min(pipeUpperLimit, ((screen_height - 200) / 2)))
					flag = 1

			print(f'pipe height = {pipe_height}')
			
			print(f'flag = {flag}')

			btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1,pipeLowerLimit, pipe_height)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1, pipeUpperLimit, pipe_height)
			
			print(f'botm pipe y = {btm_pipe.rect.y}, top pipe y {top_pipe.rect.y}')

			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

		elif time_now - last_pipe > (pipe_frequency // 2) and bonus:
			bugga = Bugga(screen_width, screen_height - 200)
			bugga_group.add(bugga)
			bonus = False
			bugga_generated = False  # Reset the bugga_generated flag when bonus is used
			last_pipe = time_now

		# look for collision
		if pygame.sprite.groupcollide(bird_group, bugga_group, False, True):
			bonus_pts += 1
			
			print(f' BOnus points = = = > {bonus_pts}')
			
		pipe_group.update()
		bugga_group.update()
		
		acc = 0
		pipe_frequency = (8000 + acc )/ scroll_speed
		

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
