import pygame, os, sys
from gamelib.sprite import Sprite

pygame.init()

screen = pygame.display.set_mode( (800, 600 ),
		pygame.DOUBLEBUF | pygame.HWSURFACE )

pygame.display.set_caption( "Esempio 04" )
surf = pygame.display.get_surface()

sprite = Sprite ( surf )
sprite.load( ".", ["nemico_a_01.png", "nemico_a_02.png"] )

dx = 0
dy= 0

def hendle_events( events ):
	global dx, dy

	for event in events:
		if event.type == pygame.QUIT:
			sys.exit( 0 )
		elif event.type == pygame.KEYDOWN:
			if event.key == 275: #destra
				dx = 2
			elif event.key == 276: #sinistra
				dx = -2
			elif event.key == 274: #giu'
				dy = 2
			elif event.key == 273: #su
				dy = -2
		elif event.type == pygame.KEYUP:
			if event.key in (275, 276):
				dx = 0
			elif event.key in (274, 273):
				dy = 0
		else:
			print (event)

clock = pygame.time.Clock()

while True:
	hendle_events( pygame.event.get() )

	surf.fill( (0, 0, 0) )
	sprite.x += dx
	sprite.y += dy

	sprite.blit()

	clock.tick (60)

	sprite.update()

	pygame.display.flip()
