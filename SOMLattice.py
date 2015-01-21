from SOMNode import SOMNode

class SOMLattice:
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def lattice(self):
        return self._lattice
    @lattice.setter
    def lattice(self, value):
        self._lattice = value
    
    def __init__(self, height, width, inputWeightNumber):
    	self._width = width;
    	self._height = height;
    	self._lattice = [[SOMNode(x,y,inputWeightNumber) for y in range(width)] for x in range(height)] 

    def getNode(self, x,y):
        return self._lattice[x][y];

    def findBMU(self, inputPair):
        BMUNode = self._lattice[0][0]
        bestDistance = inputPair.distance(BMUNode)
        currentDistance = 0;
        for x in range(self._height):
            for y in range(self._width):
                currentDistance = inputPair.distance(self._lattice[x][y])
                if currentDistance < bestDistance:
                    bestDistance = currentDistance;
                    BMUNode = self._lattice[x][y];
        return BMUNode


