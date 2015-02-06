import pygame
import math
from Slider import Slider
from Button import Button

class SOMRenderer:
	#Propery that represents color selected by sliders
	@property
	def currentSelectedColor(self):
	    return self._currentSelectedColor
	@currentSelectedColor.setter
	def currentSelectedColor(self, value):
	    self._currentSelectedColor = value
	

	def __init__(self, startingLattice, colorList):
		self.lattice = startingLattice
		self.width = 600;
		self.statusHeight = 90
		self.height = 600+self.statusHeight;

		#Determining  cell size for variable number of nodes in lattice
		self.cellWidth = math.floor(self.width/self.lattice.width)
		self.cellHeight = math.floor((self.height-self.statusHeight)/self.lattice.height);
		self.action = ['NaN']
		self.colorList = colorList
		self.currentSelectedColor = (0,0,0)
		self.gridline = False;

		self.distance = 0
		#Initializing GUI
		#Creating main window, divided in mainScreen (lattice), and status screen
		#Adding GUI element, sliders, buttons.
		pygame.init()
		pygame.display.set_caption("Self-organizing maps - Color Classification")
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.statusSurface = pygame.Surface((self.width, self.statusHeight))
		self.colorListSurface = pygame.Surface((260, 30))

		self.s1 = Slider(5,30,(self.width, self.height-self.statusHeight))
		self.s2 = Slider(5,40,(self.width, self.height-self.statusHeight))
		self.s3 = Slider(5,50,(self.width, self.height-self.statusHeight))
		self.sliders =[self.s1, self.s2, self.s3]

		self.b1 = Button(120, 5, ((self.width, self.height-self.statusHeight)),"Step",1)
		self.b2 = Button(170, 5, ((self.width, self.height-self.statusHeight)),"Train",2)
		self.b3 = Button(220, 5, ((self.width, self.height-self.statusHeight)),"Pause",3)
		self.b4 = Button(270, 5, ((self.width, self.height-self.statusHeight)),"Stop",4)
		self.b5 = Button(170, 65, ((self.width, self.height-self.statusHeight)),"Test",5)
		self.b6 = Button(220, 65, ((self.width, self.height-self.statusHeight)),"Add",6)
		self.b7 = Button(270, 65, ((self.width, self.height-self.statusHeight)),"Del",7)
		self.b8 = Button(5, 65, ((self.width, self.height-self.statusHeight)),"Grid",8)
		self.buttons = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6,self.b7, self.b8]
		
		self.formItems = self.sliders + self.buttons
		self.textFont = pygame.font.Font(None,25)

		self.statusSurface.fill((100,100,100))
		self.colorListSurface.fill((100,100,100))
		

	def renderMainScreen(self):
		#Render main panel with cells
		#Rendering of second rectangle borders is optional, depends od button Grid activity
		[[(pygame.draw.rect(self.screen, [i*255 for i in self.lattice.getNode(x,y).weights],((y*self.cellWidth, x*self.cellHeight),(self.cellWidth,self.cellHeight)),0),  \
		pygame.draw.rect(self.screen, (0,0,0),((y*self.cellWidth*self.gridline, x*self.cellHeight*self.gridline),(self.cellWidth*self.gridline,self.cellHeight*self.gridline)),1))  \
		 for y in range(self.lattice.width)] for x in range(self.lattice.height)]

	#function used to mark the results during simulation
	def markBMU(self, BMUNode):
		pygame.draw.circle(self.screen, (1,1,1),(BMUNode.ypos*self.cellWidth+10, BMUNode.xpos*self.cellHeight+10),5,2)
		pygame.draw.circle(self.screen, (0,0,0),(BMUNode.ypos*self.cellWidth+10, BMUNode.xpos*self.cellHeight+10),5,0)

	#rendering status surface
	#rendering iteration info and training controls
	#rendering sliders and current color block
	#rendering colorList and color list controls
	def renderStatusScreen(self, mpos, mpress, mrel, iterationCount, colorList):
		self.statusSurface.fill((100,100,100))
		self.colorListSurface.fill((100,100,100))
		iterationInfo = self.textFont.render("Iter: " + str(iterationCount), 1, (255,255,255), (100,100,100))
		distanceInfo = self.textFont.render("Dist: " + str(self.distance), 1, (255,255,255), (100,100,100))

		[i.update(mpos, mpress, mrel, self.action) for i in self.formItems]
		[i.render(self.statusSurface) for i in self.formItems]	

		pygame.draw.rect(self.statusSurface,(0,0,0),(280,30,30,30),1)
		pygame.draw.rect(self.statusSurface,(self.s1.value,self.s2.value,self.s3.value),(280,30,30,30),0)	
		self.currentSelectedColor = (self.s1.value, self.s2.value, self.s3.value)
		[pygame.draw.circle(self.colorListSurface,(i[0], i[1],i[2]),(colorList.index(i)*30+30,15),15) for i in colorList]
		[pygame.draw.circle(self.colorListSurface,(0,0,0),(colorList.index(i)*30+30,15),15,1) for i in colorList]
		
		#Merge everything together on main window
		self.statusSurface.blit(iterationInfo, (5,5))
		self.statusSurface.blit(distanceInfo, (50,65))
		self.statusSurface.blit(self.colorListSurface, (330,30))
		self.screen.blit(self.statusSurface,(0, self.height-self.statusHeight))

	def displayDistance(self, dist):
		self.distance = round(dist,4)

	def printNode(self, node):
		print(node.weights)
		print(node.xpos)
		print(node.ypos)