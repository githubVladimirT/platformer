#!/usr/bin/env python

import pygame
import sys
from settings import *
from level import Level


def main():
	# pygame setup
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Platformer")
	clock = pygame.time.Clock()

	level = Level()

	while True:
		# event loop
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        pygame.quit()
		        sys.exit()

		screen.fill(BG_COLOR)
		level.run()

		# drawing logic
		pygame.display.update()
		clock.tick(60)
		
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exit")
