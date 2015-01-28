from SOMLattice import SOMLattice
from SOMNode import SOMNode
from SOMRenderer import SOMRenderer
import pygame
import sys

class SOMMain:

	def __init__(self):
		self.inputNode = SOMNode(None,None,3)
		self.matrix = SOMLattice(10,10,3);
		self.rend = SOMRenderer(self.matrix);
		BestNode = self.matrix.findBMU(self.inputNode)
		self.rend.printNode(self.inputNode)
		self.rend.printNode(BestNode)
		self.inputNode.distance(BestNode)
		self.isRunning = False;

	def GetInput(self):
		self.key = pygame.key.get_pressed()
		self.mpress = pygame.mouse.get_pressed()
		self.mpos = pygame.mouse.get_pos()
		self.mrel = pygame.mouse.get_rel()
		for event in pygame.event.get():
		    if event.type == pygame.QUIT or self.key[pygame.K_ESCAPE]:
		        pygame.quit()
		        sys.exit()

	def Render(self):
		self.rend.renderMainScreen();
		self.rend.renderStatusScreen(self.mpos, self.mpress, self.mrel)


