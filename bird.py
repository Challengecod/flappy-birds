import pygame


class BIRD:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["bird_up.png", "bird_mid.png"] # # upload the bird image both the bird up and down
        self.image = pygame.image.load(self.image_list[0]) # load the first image from the list
        self.image_size = self.image.get_size() # get the size
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1]) # make the bird a rectangle
        self.delta = 3 # up and down movement speed
        self.current_direction = "up" # direction later used in the function
        self.up = True # the bird is flapping up


    # swtiching the image between the bird's wings flapping up or down
    def switch_image(self):
        # image switch
        image_number = 0 # start with the image bird up
        # if self.up = not(True) = False
        # if self.up = not(not True) = True
        if not self.up:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number]) # load in the bird_mid png
        self.image_size = self.image.get_size() # get the size of the image
        self.up = not self.up # this varaible helps it get to image_number = 1 and self.up = not True


    def move_bird(self, direction):
        # move the balloon up based on the direction!
        if direction == "up":
            self.current_direction = "up"
            # if the y position of the bird subtracted by delta is less than or equal to zero then we can subtract
            # Otherwise we won't subtract or else the bird will move off the top of the screen
            if self.y - self.delta >= 0:
                self.y -= self.delta  # subtract 3 from the y_position so it can move up the screen when space bar is pressed

        # move the balloon down based on the direction!
        if direction == "down":
            self.current_direction = "down"
            # if the y position of the bird added by delta is greater than or equal to 500 then we can add to the y_position
            # Otherwise we won't qdd or else the bird will move off the bottom of the screen
            if self.y - self.delta <= 500:
                self.y += self.delta # add delta to the  y_position so it can move down the screen when space bar is not pressed

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1]) # get the rectangle of the bird





