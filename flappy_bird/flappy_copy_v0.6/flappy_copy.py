# Copyright (©) 2023 - Vedant 
# MIT License
# -------------------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# -------------------------------------------------------------------------------------
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# -------------------------------------------------------------------------------------

import pygame; pygame.init()
# from icecream import ic
from pygame.locals import *

from fb_settings import *
from game_sprites import *
from options import *

from bird import Bird
from bug import Bugga
from pipe import Pipe, pipeGenerate
from extras import Button, Heart


#	SPRITE GROUPS
pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
bugga_group = pygame.sprite.Group()


#	GAME OBJECTS
flappy = Bird(100, int((screen_height - 100) / 2))
button = Button(screen_width // 2 , screen_height // 2 , buttonImgResized)
hearts = Heart(heart_img, 10, 50)
bird_group.add(flappy)


while run:

	clock.tick(fps)

	# * checks for certain no. of epochs
	if score == repetations:
		game_over = True
		flying = False

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
	score, pass_pipe = check_score(score, pass_pipe, pipe_group, bird_group)

	draw_text(str(score), font, white, int(screen_width / 2), 20, screen)
	draw_text("By Vedant Mankar", font1, (45, 190, 190), int(screen_width / 2.25), 1, screen)

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
			# ic(time_now - last_pipe)
			# ic(pipe_frequency)

			if pipeHit == False:
				pipe_height, flag =  pipeGenerate(pipe_height, pipeUpperLimit, pipeLowerLimit, pipeHeightIncrement, flag)
				# Stores pipe heights and flags
				piph.append((pipe_height, flag)); print(piph)
				
			# if the bird hits pipe the pipe state is reverted to previous where the bird hit
			elif pipeHit == True:
				pipe_height, flag =  pipeGenerate(pipe_height, pipeUpperLimit, pipeLowerLimit, pipeHeightIncrement, flag)
				print(piph, 'pip reverted to -2')
				pipe_height, flag = piph[-2]; pipeHit = False; piph = piph[:-1]
			print(f'{pipe_height = }, {flag= }')

			btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1,pipeLowerLimit, pipe_height)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1, pipeUpperLimit, pipe_height)
			print(f'{btm_pipe.rect.y = }, {top_pipe.rect.y = }')

			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

		elif (time_now - last_pipe) > (pipe_frequency / 4) and bonus:
	
			bugga = Bugga(screen_width, bugga_y_pos, bugga_img)
			bugga_group.add(bugga)
			bonus = False 
			bugga_generated = False  # Reset the bugga_generated flag when bonus is used
			last_pipe = time_now

		# look for collision
		if pygame.sprite.groupcollide(bird_group, bugga_group, False, True):

			bonus_pts += 1
			print(f' BOnus points = = = > {bonus_pts}')
			
		pipe_group.update()
		bugga_group.update(bugga_drawn)
		ground_scroll -= scroll_speed

		if abs(ground_scroll) > 35:
			ground_scroll = 0
	

	#check for game over and reset
	if game_over == True and round_restart == 0:
		lives -= 1 
		round_restart = 1 
		pipeHit = True
		
	elif end_game == False and game_over == True and round_restart == 1:
		game_over = False
		# score = reset_game()
		reset_game(pipe_group, flappy, screen_height)
		round_restart = 0

	elif end_game == True and game_over == True and round_restart == 1 and button.draw(screen):
		score, lives = new_game(orglives, pipe_group, flappy, screen_height)
		round_restart = 0 
		game_over = False 
		end_game = False 

	# print(f'pipe height after {pipe_height}')
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False 
		if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
			flying = True
		if event.type == pygame.KEYDOWN:
			if event.key == K_SPACE and flying == True:
				flying = False
			elif event.key == K_SPACE and flying == False:
				flying = True

	hearts.draw(lives, screen)

	pygame.display.update()
	# print(f'lives {lives}')
	if lives == -1:
		end_game = True
		game_over = True
	
	
pygame.quit()
