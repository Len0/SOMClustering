import math

class SOMTrainer:

	def __init__(self, matrix):
		self.baseLearningRate = 0.07
		self.learningRate = 0.07
		self.numIterations = 500

		self.latticeW = matrix.width
		self.latticeH = matrix.height
		self.latticeRadius = max(self.latticeW, self.latticeH)/2;
		self.timeConstant = self.numIterations / math.log(self.latticeRadius)


	#function for normalazing RGB values to interval [0,1]
	def normalizeValues(self, color):
		weightVector = [i/255 for i in color]
		return weightVector

	#function for finding best matching unit
	#iterates trough colors that represent sample data
	#for each iteration one color is presented to neuron lattice and BMU is found
	def getBMU(self):
		listLenght = len(self.inputList)
		if listLenght > 0:
			node = self.normalizeValues(self.inputColorList[((self.iteration+listLenght-1)%listLenght)])
			testNode = SOMNode(None,None,3)
			testNode.weights = node;
			node = self.matrix.findBMU(testNode)

	#function for determining radius of neighborhood circle
	def getNeighborhoodRadius(self, iteration):
		return self.latticeRadius * math.exp(-iteration/self.timeConstant)

	#function that sets distance falloff parameter
	def getDistanceFalloff(self, distanceSquared, radius):
		radiusSquared = radius * radius;
		return math.exp(-(distanceSquared)/(2*radiusSquared));

	#function that trains SOM for one epoch
	#uses nbhRadius to determine rectangle sides
	def trainEpoch(self, matrix, iteration, input):
		nbhRadius = self.getNeighborhoodRadius(iteration);
		bmu = matrix.findBMU(input);

		xstart = int(round(bmu.xpos - nbhRadius - 1));
		ystart = int(round(bmu.ypos - nbhRadius - 1));
		xend = int(round(xstart + (nbhRadius * 2) + 1));
		yend = int(round(ystart + (nbhRadius * 2) + 1));
		if (xend > self.latticeW): xend = self.latticeW;
		if (xstart < 0): xstart = 0;
		if (yend > self.latticeH): yend = self.latticeH;
		if (ystart < 0): ystart = 0;

		for x in range(xstart, xend):
			for y in range(ystart, yend):
				temp = matrix.getNode(x,y)
				dist = bmu.distance(temp)
				if (dist <= (nbhRadius * nbhRadius)):
					dFalloff = self.getDistanceFalloff(dist, nbhRadius);
					temp.updateWeights(input, self.learningRate, dFalloff);

		self.learningRate = self.baseLearningRate * math.exp(-iteration/self.numIterations)


