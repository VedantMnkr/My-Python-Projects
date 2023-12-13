def spriteResize(oldSprite, pygame, screen_width, screen_height, extraheight=0):
	widthMultiplier = oldSprite.get_width() / 864
	heightMultiplier = oldSprite.get_height() / 756
	newSprite = pygame.transform.scale(oldSprite, (int(widthMultiplier * screen_width), int(heightMultiplier * screen_height+extraheight)))
	return newSprite


def reset_game(pipe_group, flappy, screen_height):
	pipe_group.empty()	
	flappy.rect.x = 100  
	flappy.rect.y = int(screen_height / 2)
	# score = 0
	# return score


def new_game(orglives, pipe_group, flappy, screen_height):
	pipe_group.empty()	
	flappy.rect.x = 100  
	flappy.rect.y = int(screen_height / 2)
	score = 0
	life = orglives
	return score, life


#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y, screen):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y)) 


def check_score(score, pass_pipe, pipe_group, bird_group):
	if len(pipe_group) > 0:	
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False
	return score, pass_pipe