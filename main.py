
from ground import GROUND
from bird import BIRD
from top_pipe import TOPPIPE # from file import class
from bottom_pipe import BOTPIPE
from hill import HILL
import random # able to use random.randint by importing random

import pygame

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Flappy Birds!")

# set up variables for the display
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 580
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


bg = pygame.image.load("background.png")
bird = pygame.image.load("bird_up.png") # upload the bird wings up image

game_finish = pygame.image.load("game_over.png")

#Initailize rectangles
g = GROUND(0,520)
#initailize the bird rectangle and frame
b = BIRD(100,250)


frame = 0

tp = TOPPIPE(230, -200) # the y_position is negative so the pipe can outrude some and not fully
bp = BOTPIPE(230, tp.y + random.randint(550, 600)) # the top pipe y_position + random number between 550 to 600 to make the gap

b_up = pygame.transform.rotate(bird, 20) # rotate my bird 20 degrees upwards

num = random.randint(0,1) # 50 percent chance the hill will come in flipped or not flipped
# if random number is one
if num == 1:
    flip = True # yes flip
    h = HILL(500, 0, flip) # initialize the hill fliped image with the y position to the top of screen to convey its hanging

else:
    flip = False # don't flip
    h = HILL(500, 350, flip) # initialize the original image with the y-position 350 to convey its comming out from the ground

score = 0 # initailize score variable counter
game_over = False # game over boolean
bird_up = False # bird wings up boolean

# render the text for later
score_display = my_font.render("Score:" + str(score), True, (199,255,255)) # initailize my score render


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock() # creating a clock object to keep track of time

while run:

    # 60 FPS
    clock.tick(60) # running at max 60 frames per second
    if frame % 30 == 0: # switch twice every second
        b.switch_image() # switching between bird images


    # the user pressed a key
    keys = pygame.key.get_pressed()
    # if the user presses the space key
    if keys[pygame.K_SPACE]:
        # bird up animation
        bird_up = True
        # bird moves up
        b.move_bird("up")

    # if the user doesn't press the space button
    else:
        # bird moves down
        b.move_bird("down")


    # once the top pipe hits the left of the screen width
    if tp.x == 0:
        print("yes") # checks if the top pipe hits zero
        tp.x = 500 # top pipe resets to the length of the screen_width
        tp.y = -int(random.randint(80, 400)) # the y_position may switch to the top_pipe extruding out more or less

        score += 1 # add a score because the bird didn't hit the pipe
        score_display = my_font.render("Score:" + str(score), True, (99, 155, 255)) # update the score each time through the loop


    # once the bottom pipe hits the width of the screen
    if bp.x == 0:
        bp.x = 500 # bottom pipe resets to the length of the screen_width
        bp.y = tp.y + random.randint(540, 590) # make sure there is a gap between the top and bottom pipe

    # once the hill hits the width of the screen
    if h.x == 0:

        num = random.randint(0,1) # randomize a 50 percent chance the hill will be flipped or not

        # if the random number is 1 the hill will be flipped
        if num == 1:
            flip = True # boolean input
            h.flip_hill(flip) # hill flip function and the boolean as an argument

        # if the random number is 0 the hill will not be flipped
        elif num == 0:
            flip = False# boolean input
            h.flip_hill(flip) # # hill flip function and the boolean as an argument



    # if the bird touches or collides with the bottom or top pipe or the ground or the hill game is over
    if b.rect.colliderect(bp.rect) or b.rect.colliderect(tp.rect) or b.rect.colliderect(h.rect):
        game_over = True

    elif b.rect.colliderect(g.rect):
        game_over = True


    # calls the move() function in my ground class to make the ground move
    g.move()
    # calls the move_pipe() function in my top pipe class to make the top pipe move
    tp.move_pipe() # top pipe animation
    # calls the move_pipe() function in my bottom pipe class to make the bottom pipe move
    bp.move_pipe() # bottom pipe animation
    # calls the move_hill() function in my hill class to make the hill move
    h.move_hill()

    # --- Main event loop ---- #

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False


        # blit background
    if game_over is True:
        screen.blit(game_finish, (150, 300)) # blit game over and everything else stops

    else:
        screen.blit(bg, (0, 0)) # background
        screen.blit(g.image, g.rect) # ground rectangle image
        screen.blit(tp.image, tp.rect) # top pipe rectangle image
        screen.blit(bp.image, bp.rect) # bottom pipe rectangle image
        screen.blit(score_display, (40,40)) # display user score
        screen.blit(h.image, h.rect) # hill rectangle image

        # the bird is going up from the space button being pressed
        if bird_up is True:
            screen.blit(b_up, (b.x, b.y)) # blit the birds wing up in the position of the bird
            bird_up = False # reset the boolean to false because the key space is not pressed

        else:
            screen.blit(b.image, b.rect) # make sure the wings are still flapping


    frame += 1 # helps start the frames per second each loop
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

