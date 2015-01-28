import pygame

class Slider(object):
    def __init__(self, x,y,size,value=0):
        self.x = x 
        self.y = y 
        self.pos = (self.x,self.y+size[1])
        self.height = 10
        self.bar_length = 20
        self.width = 275
        self.bar = pygame.Surface((self.width,self.height))
        self.bar.fill((200,200,200))
        self.slider = pygame.Surface((self.bar_length,self.height))
        self.slider.fill((230,230,230))
        pygame.draw.rect(self.bar, (0,0,0), (0,0,self.width,self.height), 1)
        pygame.draw.rect(self.slider, (0,0,0), (0,0,self.bar_length,self.height), 1)
        self.clicked = False
        self.value = value
        

    def update(self,mpos, mpress, mrel):
        if (mpos[0] > (self.pos[0]+self.value)) and (mpos[0] < (self.pos[0]+self.value)+self.bar_length):
            if mpos[1]>self.pos[1] and mpos[1] < self.pos[1]+self.height:
                if mpress[0]:
                    self.clicked = True
        if not mpress[0]:
            self.clicked = False
        if self.clicked:
            self.value += mrel[0]
        if self.value < 0: self.value = 0
        if self.value > 255: self.value = 255

    def render(self, surface):
        self.surface = surface
        surface.blit(self.bar,(self.x,self.y))
        surface.blit(self.slider,(self.x+self.value,self.y))

