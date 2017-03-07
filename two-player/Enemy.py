import pygame


class Enemy(pygame.sprite.Sprite):
        def __init__(self, gs, character):
            if character == "mario":
                self.chr = "luigi"
            if character == "luigi":
                self.chr = "mario"
            pygame.sprite.Sprite.__init__(self)
            self.gs = gs
            self.sprite = 0
            self.image = pygame.image.load("media/"+self.chr+"/"+self.chr+"-" + str(self.sprite + 1) + ".png")
            self.rect = self.image.get_rect()
            self.rect.x = 450
            self.rect.y = 364

            self.x = 450
            # keep original image to limit resize errors
            self.orig_image = self.image

    # tick and pass parameters
        def tick(self, received, p1):
                self.rect.y = received[1]
                self.x = received[0]
                self.rect.x = self.x + 450 - p1[0]

                self.sprite = (self.sprite + 1) % 3  # incrementing sprite
                self.image = pygame.image.load("media/"+self.chr+"/"+self.chr+"-" + str(self.sprite + 1) + ".png")

                arr = [self.x, self.rect.y]
                return arr
