import pygame

class HILL:

    def __init__(self, x, y, flip):
        self.x = x #x_position
        self.y = y #y_position
        self.image = pygame.image.load("hill.png") # upload hill image
        # from our main py if the random number is 1 flip is true
        if flip is True:
            # we flip the image so both true boolean arguments so a flip on both the x and y axis.
            self.image = pygame.transform.flip(self.image, True, True)
        self.image = pygame.transform.flip(self.image, False, False)
        self.rescale_image(self.image) # rescale function
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1]) # making the hill to a rectangle
        self.delta = 1


    def rescale_image(self, image):
        self.image_size = self.image.get_size() # get the image size
        # multiplying the width and height above 0.5 makes the image larger
        scale_size = (self.image_size[0] * .6, self.image_size[1] * 1.5)
        self.image = pygame.transform.scale(self.image, scale_size) # transforming to your scale

    # moving the hill left towards the bird
    def move_hill(self):

        # if the x position is not zero we keep subtracting so the sprite moves left
        if self.x != 0:
            self.x = self.x - self.delta

        # if the x position is at zero we set the sprite back to the 500 x_position to restart
        else:
            self.x = 500
        # get the rectangle of the sprite
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def flip_hill(self, flip):
        # the random num is 1 we flip
        if flip is True:
            self.image = pygame.image.load("hill.png")  # upload hill image
            self.rescale_image(self.image)  # rescale function
            self.image_size = self.image.get_size()
            self.image = pygame.transform.flip(self.image, True, True) # flip on both the x and y axis
            self.x = 500 # the hill starts again from the left towards the bird
            self.y = 0 # comes out from top of the screen

        # the random num is 0 we don't flip
        else:
            self.image = pygame.image.load("hill.png")  # upload hill image
            self.rescale_image(self.image)  # rescale function
            self.image_size = self.image.get_size()
            # copy and paste the same code to use the original image instead of the flipped one
            self.image = pygame.transform.flip(self.image, False, False)
            self.x = 500 # the hill starts again from the left towards the bird
            self.y = 300 # when hill is not flipped the y_pos is poking out from the ground and not too high

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1]) # get the hill rectangle



