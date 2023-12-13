import pygame
from fb_settings import screen_height, screen_width
from options import spriteResize


#	load images original
bgOrg = pygame.image.load('img/bg.png')
button_img = pygame.image.load('img/restart.png') # w 0.139 h 0.056
ground_imgOrg = pygame.image.load('img/ground.png')
bugga_imgorg = pygame.image.load('img/bugga.png')
heart_imgorg = pygame.image.load('img/heart.png')
# buttonImgResized = pygame.transform.scale(button_img, (int(0.139 * screen_width), int(0.056 * screen_height)))


#	Resized Images
buttonImgResized = spriteResize(button_img, pygame, screen_width, screen_height)
bg = spriteResize(bgOrg, pygame, screen_width, screen_height)
ground_img = spriteResize(ground_imgOrg, pygame, screen_width, screen_height)
bugga_img = pygame.transform.scale(bugga_imgorg, (50, 50))
heart_img = pygame.transform.scale(heart_imgorg, (40, 40))
# print(f'before resizing {button_img.get_width(), button_img.get_height()} after resizing {button_img.get_width() - (screen.get_width() - 864), button_img.get_height() - (screen.get_height() - 756)}')
