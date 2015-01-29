import pygame
from Slider import Slider
from Button import Button

class SOMRenderer:

	def __init__(self, startingLattice):
		self.lattice = startingLattice
		self.width = 600;
		self.statusHeight = 90
		self.height = 600+self.statusHeight;
		self.cellWidth = self.width/self.lattice.width;
		self.cellHeight = (self.height-self.statusHeight)/self.lattice.height;
		self.action = ['NaN']

		pygame.init()
		pygame.display.set_caption("Self-organizing maps - Color Classification")
		self.screen = pygame.display.set_mode((self.width, self.height))

		self.statusSurface = pygame.Surface((self.width, self.statusHeight))

		self.s1 = Slider(5,30,(self.width, self.height-self.statusHeight))
		self.s2 = Slider(5,40,(self.width, self.height-self.statusHeight))
		self.s3 = Slider(5,50,(self.width, self.height-self.statusHeight))
		self.sliders =[self.s1, self.s2, self.s3]

		self.b1 = Button(120, 5, ((self.width, self.height-self.statusHeight)),"Step",1)
		self.b2 = Button(170, 5, ((self.width, self.height-self.statusHeight)),"Play",2)
		self.b3 = Button(220, 5, ((self.width, self.height-self.statusHeight)),"Pause",3)
		self.b4 = Button(270, 5, ((self.width, self.height-self.statusHeight)),"Stop",4)
		self.b5 = Button(170, 65, ((self.width, self.height-self.statusHeight)),"Test",5)
		self.b6 = Button(220, 65, ((self.width, self.height-self.statusHeight)),"Add",6)
		self.b7 = Button(270, 65, ((self.width, self.height-self.statusHeight)),"Del",7)
		self.buttons = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6,self.b7]
		
		self.formItems = self.sliders + self.buttons
		self.textFont = pygame.font.Font(None,25)

		self.statusSurface.fill((100,100,100))
		

	def renderMainScreen(self):
		#Render main panel with cells
		[[(pygame.draw.rect(self.screen, [i*255 for i in self.lattice.getNode(x,y).weights],
		((y*self.cellWidth, x*self.cellHeight),(self.cellWidth,self.cellHeight)),0),\
		pygame.draw.rect(self.screen, (0,0,0),((y*self.cellWidth, x*self.cellHeight),(self.cellWidth,self.cellHeight)),1)) \
		 for y in range(self.lattice.width)] for x in range(self.lattice.height)]

		
	def renderStatusScreen(self, mpos, mpress, mrel, iterationCount):
		#render statusSurface
		self.statusSurface.fill((100,100,100))
		iterationInfo = self.textFont.render("Iter: " + str(iterationCount), 1, (255,255,255), (100,100,100));
		self.statusSurface.blit(iterationInfo, (5,5))

		[i.update(mpos, mpress, mrel, self.action) for i in self.formItems]
		[i.render(self.statusSurface) for i in self.formItems]	

		pygame.draw.rect(self.statusSurface,(0,0,0),(280,30,30,30),1)
		pygame.draw.rect(self.statusSurface,(self.s1.value,self.s2.value,self.s3.value),(280,30,30,30),0)	

		#Merge everything together
		self.screen.blit(self.statusSurface,(0, self.height-self.statusHeight))

	def printNode(self, node):
		print(node.weights)
		print(node.xpos)
		print(node.ypos)