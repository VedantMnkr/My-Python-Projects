# from screeninfo import get_monitors
# for m in get_monitors():
#     x = m

# systemResHeight = x.height
# systemResWidth = x.width
# Screen Resolution
# screen_width = int(8 * 110)
# screen_height = int(7 * 110)
import pygame
from pygame.locals import *

# Screen Resolution
screen_width = 860
screen_height = 820


# window properties
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

#define font
font = pygame.font.SysFont('Bauhaus 93', 60)
font1 = pygame.font.SysFont('Bauhaus 93', 15)


#define game variables
fps = 60 # FPS LIMIT
ground_scroll = 0
flying = False
game_over = False
end_game = False
bonus = False
bugga_drawn = False
bonus_pts = 0
score = 0
pass_pipe = False


#define colours
white = (255, 255, 255)
acc = 0  # to increase the distance through time  between pipes


# Game entites
precision = 15 #!!! Pipe Gap - parameter
pipe_gap = 40 + (precision * 4) # 40 -> bird height + (precision * 4 constant)
scroll_speed = 5
pipe_frequency = (8000 + acc )/ scroll_speed #milliseconds // frequency at which the pipe occurs
last_pipe = pygame.time.get_ticks() - pipe_frequency
speed = 10 #!!! Pipe step size - parameter
pipeHeightIncrement = speed * 4 * 2
lives = 2
orglives = lives
repetations = 200


# angle = 90
angleup  = 90 #!!! Range of Motion - parameter
angledown = 90 #!!! Range of Motion - parameter
pipe_height, flag = 0, 1 # 1 means its going up and 0 means downwards
pipeUpperLimit = -(angleup * 4) #this goes up
pipeLowerLimit = angledown * 4 #this goes down
pipeHeightPiviot = -pipe_height
bugga_angle = 110 #!!! Acceleration parameter 
bugga_y_pos = bugga_angle * 4


# MISCS
previous_score = 0
bugga_generated  = False
run = True
round_restart = 0
piph = []
pipeHit = False

"""
?   - pipes at extreme are not generating correctly after collision.

"""