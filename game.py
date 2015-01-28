import cell
import math

class Game:

	def __init__(self, surface, cellSize):
		self.surface = surface
		self.size = cellSize
		self.rows = math.floor(self.surface.get_height()/(self.size))
		self.columns = math.floor(self.surface.get_width()/(self.size))	
		self.cells = []
		self.iterator = self.columns*self.rows;
		for i in range(self.columns):
			self.cells.append([])
			for j in range(self.rows):
				self.cells[i].append(cell.Cell((i,j),self.surface, self, 0))


	def normalize(self,x,y):
		x=x%self.columns;
		y=y%self.rows
		return x,y


	def updateAll(self):
		for i in range(self.columns):
			for j in range(self.rows):
				self.cells[i][j].futureState();
		for i in range(self.columns):
			for j in range(self.rows):
				self.cells[i][j].update();
				
	def drawAll(self):
		for i in range(self.columns):
			for j in range(self.rows):
				self.cells[i][j].draw();

	def getCell(self, x, y):
		x,y = self.normalize(x,y)
		return self.cells[x][y]
		
