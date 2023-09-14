from screeninfo import get_monitors
for m in get_monitors():
    x = m

systemResHeight = x.height
systemResWidth = x.width

# Screen Resolution
# screen_width = int(8 * 110)
# screen_height = int(7 * 110)

screen_width = 960
screen_height = 1020

#define colours
white = (255, 255, 255)

# Game entites
precision = 20
pipe_gap = 40 + (precision * 4) # 40 -> bird height + (precision * 4 constant)
scroll_speed = 4
pipe_frequency = 8000 / scroll_speed #milliseconds // frequency at which the pipe occurs
speed = 10
pipeHeightIncrement = speed * 4 * 2

# angle = 90
angleup  = 90
angledown = 90
pipe_height, flag = 0, 1 # 1 means its going up and 0 means downwards
pipeUpperLimit = angledown *4  #this goes down
pipeLowerLimit = -(angleup * 4) #this goes up
pipeHeightPiviot = -pipe_height
