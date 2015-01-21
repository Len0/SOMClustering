import pygame

class SOMRenderer:
	@property
	def height(self):
	    return self._height
	@height.setter
	def height(self, value):
	    self._height = value


	@property
	def width(self):
	    return self._width
	@width.setter
	def width(self, value):
	    self._width = value

	@property
	def lattice(self):
	    return self._lattice
	@lattice.setter
	def lattice(self, value):
	    self._lattice = value

	@property
	def screen(self):
	    return self._screen
	@screen.setter
	def screen(self, value):
	    self._screen = value

	@property
	def statusSurface(self):
	    return self._statusSurface
	@statusSurface.setter
	def statusSurface(self, value):
	    self._statusSurface = value

	@property
	def statusHeight(self):
	    return self._statusHeight
	@statusHeight.setter
	def statusHeight(self, value):
	    self._statusHeight = value

	@property
	def cellWidth(self):
		return self._cellSize
	@cellWidth.setter
	def cellWidth(self, value):
		self._cellWidth = value

	@property
	def cellHeight(self):
	    return self._cellHeight
	@cellHeight.setter
	def cellHeight(self, value):
	    self._cellHeight = value


    


    

	def __init__(self, startingLattice):
		self._lattice = startingLattice
		self._width = 400;
		self._statusHeight = 100
		self._height = 400+self._statusHeight;
		self._cellWidth = self._width/self._lattice.width;
		self._cellHeight = (self._height-self._statusHeight)/self._lattice.height;

		pygame.init()
		pygame.display.set_caption("Self-organizing maps - Color Classification")
		self._screen = pygame.display.set_mode((self._width, self._height))

		self._statusSurface = pygame.Surface((self._width, self._statusHeight))
		self._statusSurface.fill((100,100,100))
		

	def render(self):
		[[(pygame.draw.rect(self._screen, [i*255 for i in self._lattice.getNode(x,y).weights],
		((y*self._cellWidth, x*self._cellHeight),(self._cellWidth,self._cellHeight)),0),\
		pygame.draw.rect(self._screen, (0,0,0),((y*self._cellWidth, x*self._cellHeight),(self._cellWidth,self._cellHeight)),1)) \
		 for y in range(self._lattice.width)] for x in range(self._lattice.height)] 

		self._screen.blit(self._statusSurface,(0, self._height-self._statusHeight))


	def printNode(self, node):
		print(node.weights)
		print(node.xpos)
		print(node.ypos)