import pygame
import random
import time
from pygame.math import Vector2

############################## GLOBAL CONSTANSTS #########################
SCREEN_WIDTH = 1280 # currently no use
SCREEN_HEIGHT = 720 # currently no use
CELL_SIZE = 40      # Defines the cell size in terms of pixel //  Also defines the size the food and block size of snake
CELL_NUMBER = 20    # No. of blocks in the gird // i.e it will have CELL_NUMBER of blocks of size CELL_SIZE.    
# SO BASICALLY IF YOU WANT TO INCREASE THE SIZE OF GIRD CHANGE <CELL NUMBER> AND TO CHANGE THE SIZE OF SNAKE CHANGE <CELL SIZE>
# BUT IT WILL AFFECT THE SIZE OF GRID TOO



SNAKE_COLOR = (0, 255, 0) # GREEN
FOOD_COLOR = (255, 0, 0) # RED 
BACKGROUND = (38, 38, 38) # 1 shade of grey
COLOR_HORIZONTAL_FOR_GRID = pygame.Color(51, 51, 51)
COLOR_VERTICAL_FOR_GIRD = pygame.Color(77, 77, 77)



UPDATE_DELAY = 0.001  # while loop delay
UPDATE_RATE = 150     # event call rate
direction  = ((1, 0)) # INITIAL DIRECTION OF MOVEMENT
########################################################################## 


######################## GAME ELEMENTS ##################################

class Snake_class: # snake properties
    def __init__(self):
        self.snake_list = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        

    def draw_snake(self):  
        for blocks in self.snake_list:
            self.xs = int(blocks.x * CELL_SIZE )
            self.ys = int(blocks.y *  CELL_SIZE)
            self.snake_pos = Vector2(self.xs, self.ys)
            self.snake = pygame.Rect((self.xs, self.ys, CELL_SIZE - 2, CELL_SIZE-2))

            pygame.draw.rect(main_game.screen, SNAKE_COLOR, self.snake)            # snake version 1 // Totally fill body
            pygame.draw.rect(main_game.screen, (0, 110, 0), self.snake, CELL_SIZE // 8)         # snake version 2 // body outlines only

    def snake_move(self):
        snake_copy = self.snake_list[:-1]
        snake_copy.insert(0, snake_copy[0] + Vector2(direction))
        self.snake_list = snake_copy

    def snake_grow(self):
        snake_copy = self.snake_list
        snake_copy.append(snake_copy[-1] + Vector2(direction))
        self.snake_list = snake_copy

        print(self.snake_list)
        print("Grew")

class Food: # chewables properties
    def __init__(self):
        self.food_eaten_counter = 0         # KEEPS TRACK OF FRUITS EATEN BY THE SNAKE
        self.randomize() 
       

    def draw_food(self):
        self.food =  pygame.Rect((self.f_x * CELL_SIZE, self.f_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.ellipse(main_game.screen, FOOD_COLOR, self.food)

    def randomize(self): # randomizing food co0rdinates
        self.f_x = random.randint(0, (CELL_NUMBER - 1))
        self.f_y = random.randint(0, (CELL_NUMBER - 1))
        self.food_pos = Vector2(self.f_x, self.f_y)

class Main: # main calls
    def __init__(self):
        self.class_initialization()

    def class_initialization(self):
        self.clock = pygame.time.Clock()
        self.done = True  # while loop condition
        self.screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_NUMBER* CELL_SIZE)) # main screen draw function
        self.new_snake = Snake_class() # snake class object
        self.food = Food() # food class object

    def final_draw(self): # final snake and food draw calls
        self.screen.fill(BACKGROUND)   # background colour
        self.draw_grid_with_strips()
        self.draw_grid_with_lines()
        self.new_snake.draw_snake()
        self.food.draw_food()
        pygame.display.update()

    def interact(self): # snake and food interaction
        if self.food.food_pos == self.new_snake.snake_list[0]:
            self.food.food_eaten_counter += 1
            print(f'{self.food.food_eaten_counter} fruits consumed')
            print("smash")
            self.food.randomize()
            self.food.draw_food()

            #if (self.food.food_eaten_counter % 5 == 0): # SNAKE GROWS ONLY AFTER EATING 5 FRUITS
            self.new_snake.snake_grow() # snake-Complan condition

    def update(self):
        self.new_snake.snake_move()
        self.interact()
        self.snake_5StagesOfGrief() # kys condition
        #self.snake_being_limitless() # PUNISH THE SNAKE FOR GOING " TADDI PARR "
        self.snake_will_be_limitless() # SNAKE IS TRICKED TO " TADDI PARR "


    def draw_grid_with_strips(self):

        

        for x in range(0, CELL_NUMBER* CELL_SIZE, CELL_SIZE*2):
            #for y in range(0, CELL_NUMBER* CELL_SIZE, CELL_SIZE):

            # rect = pygame.Rect(left, top, width, height)
            self.grid_horizontal =  pygame.Rect((x, 0, CELL_SIZE, CELL_SIZE * CELL_NUMBER))
            pygame.draw.rect(self.screen, COLOR_HORIZONTAL_FOR_GRID, self.grid_horizontal)

            self.grid_vertical =  pygame.Rect((0, x, CELL_SIZE * CELL_NUMBER, CELL_SIZE))
            pygame.draw.rect(self.screen, COLOR_VERTICAL_FOR_GIRD, self.grid_vertical)

            

    def draw_grid_with_lines(self): # GRID USING LINES

        for x in range(0, CELL_NUMBER * CELL_SIZE, CELL_SIZE):

            # pygame.draw.line(surface, color, start_pos, end_pos, width=1)
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, CELL_NUMBER * CELL_SIZE), width= 1)

        for y in range(0, CELL_NUMBER * CELL_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, (50, 50, 50), (0, y), (CELL_NUMBER * CELL_SIZE, y), width= 1)


    

    def game_over(self):
        
        main_game.message()
        time.sleep(0.01)
        pygame.quit()     
            
    def snake_5StagesOfGrief(self):
        
        for block in main_game.new_snake.snake_list[1:]:
            if block == main_game.new_snake.snake_list[0]:
                main_game.game_over()   
            
    def snake_being_limitless(self):
        if (main_game.new_snake.snake_list[0].x <= -1 or main_game.new_snake.snake_list[0].x >= 20) or (main_game.new_snake.snake_list[0].y <= -1 or main_game.new_snake.snake_list[0].y >= 20) :
            main_game.game_over()

    def snake_will_be_limitless(self):     
        head = main_game.new_snake.snake_list[0]
        if head.x < 0:
            head.x = CELL_NUMBER - 1
        elif head.x >= CELL_NUMBER:
            head.x = 0
        elif head.y < 0:
            head.y = CELL_NUMBER - 1
        elif head.y >= CELL_NUMBER:
            head.y = 0


    def message(self):
        self.text = "get better kidddddddd"
        self.text_font = pygame.font.SysFont("Arial", 30)
        self.text_col = (255, 0, 255)
        self.img = self.text_font.render(self.text, True, self.text_col)
        self.screen.blit(self.img, ( 400, 400 ))


    def restart(self):
        self.class_initialization()
        self.game_over = False  # Reset the game_over flag


    def game_loop(self):
        global direction
        while self.done:  # Game Loop

            
            self.clock.tick(60)
            self.final_draw()
                        
                        
            ############################################## MOVEMENT #############################################################################

            moved = False  # Flag to track if the snake has already moved in the current frame

            if not moved:
                self.new_snake.snake.move_ip(direction)  # Move the snake

            key = pygame.key.get_pressed() # Key inputs

            if key[pygame.K_a] and direction != (1, 0): # Make sures the snake dont move in opposite direction
                direction = (-1, 0)
            elif key[pygame.K_d] and direction != (-1, 0):
                direction = (1, 0)
            elif key[pygame.K_s] and direction != (0, -1):
                direction = (0, 1)
            elif key[pygame.K_w] and direction != (0, 1):
                direction = (0, -1)

            elif key[pygame.K_q]:                    # QUIT GAME
                self.game_over()
                
            elif key[pygame.K_r]:                    # RESTART GAME
                self.restart_game()

            if not moved:
                self.new_snake.snake.move_ip(direction)  
                moved = True  # Set to True

            #############################################################################################################     


            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    self.done = False
                                
                if event.type == screen_update:
                    self.update()

            

            pygame.display.flip()  

            #time.sleep(UPDATE_DELAY)

        pygame.quit()


    def start_game(self):
        self.game_over_state = False

        while not self.game_over:
            self.final_draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over_state = True
                elif event.type == screen_update:
                    self.update()

            pygame.time.delay(UPDATE_RATE)

        pygame.quit()


    def restart_game(self):            # new restart moduel
        pygame.init()
        self.new_snake = Snake_class()
        self.food = Food()
        self.start_game()

#############################################################################################################################

pygame.init() # PYgame lib. initialization

main_game = Main() # main objects  



screen_update = pygame.USEREVENT 

pygame.time.set_timer(screen_update, UPDATE_RATE )

########################################################################################################################################
main_game.game_loop()
    
