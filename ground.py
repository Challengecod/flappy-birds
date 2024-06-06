import pygame

class GROUND:

    def __init__(self, x, y):
        self.x = x  # x_position
        self.y = y  # y_position
        self.image = pygame.image.load("ground.png") # upload the ground image
        self.image_size = self.image.get_size() # get the image size
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1]) # make the ground a rectangle
        self.delta = 1 # movement speed

    # moving the ground
    def move(self):
        # Move Ground
        # once the ground moves a bit off screen like -20, we set the ground back to zero.
        if self.rect.x == -20:
            self.rect.x = 0

        # this moves the ground towards the left
        else:
            self.rect.x -= self.delta






