from SOMLattice import SOMLattice
from SOMNode import SOMNode
from SOMRenderer import SOMRenderer
from SOMTrainer import SOMTrainer
import pygame
import sys

class SOMMain:

	def __init__(self):
		self.iteration = 0
		self.maxIteration = 500
		self.isRunning = 0
		self.isSteped = 0
		self.isPaused = 0
		self.inputColorList = [(255,0,0), (0,255,0), (0,0,255)]
		self.buttonpress = 0

		#asda
		self.inputNode = SOMNode(None,None,3)
		#Main screen initialization
		self.matrix = SOMLattice(100,100,3);
		self.rend = SOMRenderer(self.matrix, self.inputColorList);
		self.trainer = SOMTrainer(self.matrix)
		self.rend.renderMainScreen();

	def GetInput(self):
		self.key = pygame.key.get_pressed()
		self.mpress = pygame.mouse.get_pressed()
		self.mpos = pygame.mouse.get_pos()
		self.mrel = pygame.mouse.get_rel()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				self.buttonpress = 1
			if event.type == pygame.QUIT or self.key[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()		

	def getButtonEvent(self):
		button = self.rend.action[0]
		if(self.buttonpress):
			if(button == "Pause"):
				self.isPaused = 1
			if(button == "Step"):
				self.isSteped = 1
			if(button == "Train"):
				self.isPaused = 0
				self.isRunning = 1
			if(button == "Stop" and self.isRunning):
				self.isPaused = 0
				self.iteration = 0
				self.isRunning = 0
			if(button == "Add"):
				if len(self.inputColorList)<8:
					color = self.rend.currentSelectedColor
					if(self.inputColorList.count(color)<1):
						self.inputColorList.append(color)
			if(button == "Del"):
				if len(self.inputColorList) > 0:
					self.inputColorList.pop()
			if(button == "Test"):
				self.simulateSelectedColor()
		self.rend.action[0] = "Nan"
		self.buttonpress = 0

	def simulateSelectedColor(self):
		testNode = self.colorToNode(self.rend.currentSelectedColor)
		self.rend.markBMU(self.matrix.findBMU(testNode))

	def getBMU(self):
		listLenght = len(self.inputColorList)
		if listLenght > 0:
			node = self.normalizeValues(self.inputColorList[((self.iteration+listLenght-1)%listLenght)])
			testNode = SOMNode(None,None,3)
			testNode.weights = node;
			node = self.matrix.findBMU(testNode)

			self.rend.markBMU(node)	

	def colorToNode(self, color):
		newNode = SOMNode(None, None, 3)
		newNode.weights = self.normalizeValues(color)
		return newNode

	def normalizeValues(self, color):
		weightVector = [i/255 for i in color]
		return weightVector

	def Render(self):
		self.getButtonEvent()
		if (not self.isPaused and self.isRunning) or self.isSteped:
			listLenght = len(self.inputColorList)
			if(self.iteration < self.maxIteration and listLenght>0):
				self.iteration = self.iteration+1
				inputNode = self.colorToNode(self.inputColorList[((self.iteration+listLenght-1)%listLenght)])
				self.trainer.trainEpoch(self.matrix, self.iteration,inputNode)
			else:
				self.isRunning = False
			self.isSteped = 0
			self.rend.renderMainScreen();
			
			
		
		self.rend.renderStatusScreen(self.mpos, self.mpress, self.mrel,self.iteration, self.inputColorList)

		


