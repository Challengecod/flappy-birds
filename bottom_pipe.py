import pygame

class BOTPIPE:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("pipe_bottom.png") # upload the pipe bottom image
        self.rescale_image(self.image) # rescale the image from the function
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1]) # make the sprite a reactangle
        self.delta = 1


    def rescale_image(self, image):
        self.image_size = self.image.get_size() # get the image size
        # multiplying the width and height above 0.5 makes the image larger
        scale_size = (self.image_size[0] * .6, self.image_size[1] * .6)
        self.image = pygame.transform.scale(self.image, scale_size) # transforming to your scale

    # moving the pipe to the left towards the bird
    def move_pipe(self):
        # if the x position is not zero we keep subtracting so the sprite moves left
        if self.x != 0:
            self.x = self.x - self.delta

        # if the x position is at zero we set the sprite back to the 500 x_position to restart
        else:
            self.x = 500
        # get the rectangle of the sprite
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
