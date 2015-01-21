from SOMLattice import SOMLattice
from SOMNode import SOMNode
from SOMRenderer import SOMRenderer

import pygame


inputNode = SOMNode(2,2,3)
matrix = SOMLattice(50,50,3);
rend = SOMRenderer(matrix);
BestNode = matrix.findBMU(inputNode)
rend.printNode(inputNode)
rend.printNode(BestNode)
inputNode.distance(BestNode)




done = False
pause = True
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True           	
            if event.type == pygame.MOUSEBUTTONDOWN:
            	if event.button == 3:
            		print("MouseClicked")
            	if event.button == 1:
            		print("MouseClicked")
    rend.render()
    pygame.display.update()


