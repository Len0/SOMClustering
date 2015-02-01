from SOMLattice import SOMLattice
from SOMNode import SOMNode
from SOMRenderer import SOMRenderer
import pygame
import sys

class SOMMain:

	def __init__(self):
		self.iteration = 0
		self.isStopped = 0
		self.isPaused = 0
		self.inputColorList = [(200,100,200), (100,100,100), (44,213,23),(100,100,200), (100,123,100), (44,212,23),(202,12,200), (102,120,101)]
		self.buttonpress = 0

		self.isStepActivated = 0
		self.inputNode = SOMNode(None,None,3)
		self.matrix = SOMLattice(10,10,3);
		self.rend = SOMRenderer(self.matrix, self.inputColorList);
		BestNode = self.matrix.findBMU(self.inputNode)
		self.rend.printNode(self.inputNode)
		self.rend.printNode(BestNode)
		self.inputNode.distance(BestNode)

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
				self.isStepActivated = 0
			if(button == "Step"):
				self.iteration = self.iteration + 1
			if(button == "Play"):
				self.isPaused = 0
				self.isStepActivated = 0
			if(button == "Stop"):
				self.isPaused = 1
				self.iteration = 0
				self.isStepActivated = 0
			if(button == "Add"):
				if len(self.inputColorList)<8:
					color = self.rend.currentSelectedColor
					if(self.inputColorList.count(color)<1):
						self.inputColorList.append(color)
			if(button == "Del"):
				if len(self.inputColorList) > 0:
					self.inputColorList.pop()
			if(button == "Test"):
				pass
		self.rend.action[0] = "Nan"
		self.buttonpress = 0

	def Render(self):
		self.getButtonEvent()
		if not self.isPaused:
			self.rend.renderMainScreen();
			self.iteration = self.iteration+1
		self.rend.renderStatusScreen(self.mpos, self.mpress, self.mrel,self.iteration, self.inputColorList)

		


