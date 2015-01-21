import random
from operator import sub, mul

class SOMNode:

	@property
	def weights(self):
	    return self._weights
	@weights.setter
	def weights(self, value):
	    self._weights = value

	@property
	def xpos(self):
	    return self._xpos
	@xpos.setter
	def xpos(self, value):
	    self._xpos = value

	@property
	def ypos(self):
	    return self._ypos
	@ypos.setter
	def ypos(self, value):
	    self._ypos = value

	def __init__(self, x, y, numWeight):
		self._xpos = x
		self._ypos = y
		self._weights = [random.random() for x in range(numWeight)]

	def distance(self, node):
		euclid_distance = map(sub, self._weights, node.weights)
		euclid_distance = [x**2 for x in euclid_distance]
		euclid_distance = sum(euclid_distance)
		return euclid_distance

	def updateWeights(self, inputPair, learningRate, falloff):
		w = self._weights
		p = inputPair.weights
		dw =  map(sub, p, w)
		wt =  map(mul, w, dw)
		self._weights += [x*falloff*learningRate for x in wt]



