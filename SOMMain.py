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
		self.inputColorList = [(200,100,200), (100,100,100), (44,213,23)]
		
		self.isStepActivated = 0
		self.inputNode = SOMNode(None,None,3)
		self.matrix = SOMLattice(10,10,3);
		self.rend = SOMRenderer(self.matrix);
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
		if(button == "Pause"):
			self.isPaused = 1
			self.isStepActivated = 0
		if(button == "Step" and self.buttonpress):
			self.iteration = self.iteration + 1
			self.buttonpress = 0
		if(button == "Play"):
			self.isPaused = 0
			self.isStepActivated = 0
		if(button == "Stop"):
			self.isPaused = 1
			self.iteration = 0
			self.isStepActivated = 0
		self.rend.action[0] = "Nan"

	def Render(self):
		self.getButtonEvent()
		if not self.isPaused:
			self.rend.renderMainScreen();
			self.iteration = self.iteration+1
		self.rend.renderStatusScreen(self.mpos, self.mpress, self.mrel,self.iteration)

		


