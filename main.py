from SOMMain import SOMMain

import pygame

def main():
	mainApp = SOMMain()
	done = False
	while not done:
		mainApp.GetInput()	
		mainApp.Render()
		pygame.display.update()	
if __name__ == '__main__': main()

