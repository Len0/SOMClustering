import pygame

class Button(object):
    def __init__(self, x,y,size,text,id):
        self.x = x 
        self.y = y 
        self.pos = (self.x,self.y+size[1])
        self.id = id
        self.height = 20
        self.width = 40
        self.button = pygame.Surface((self.width,self.height))
        self.button.fill((200,200,200))
        pygame.draw.rect(self.button, (120,120,0), (0,0,self.width,self.height), 1)
        self.clicked = False
        self.text = text
        self.textFont = pygame.font.Font(None,self.height-2)
        

    def update(self,mpos, mpress, mrel, action):
        if (mpos[0] > (self.pos[0]) and (mpos[0] < self.pos[0]+self.width)):
            if mpos[1]>self.pos[1] and mpos[1] < self.pos[1]+self.height:
                if mpress[0]:
                    self.clicked = True
        if not mpress[0]:
            self.clicked = False
            action[0] = "NaN"
        if self.clicked:
            action[0] = self.text



    def render(self, surface):
        self.surface = surface
        label = self.textFont.render(self.text, 1, (0,0,0), (200,200,200));
        self.button.blit(label, ((self.width-label.get_width())/2,(self.height-label.get_height())/2))
        surface.blit(self.button,(self.x,self.y))
        