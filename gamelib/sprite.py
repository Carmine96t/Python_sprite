import pygame, os
#oggetto che si muove sullo schermo
class Sprite( object ):
	def __init__(self, surf ):
		self._surf = surf

		#immagini animazioni sprite
		self._images = []

		# contatore immagine da mostrare
		self._curr_img = 0.0

		#aggiornamento animazione
		self.update_rate = 0.1

		#coordinate
		self.x = 0
		self.y = 0

		#dimensione dell'oggetto
		self.w = 0 #larghezza
		self.h = 0 #altezza

		#opzione di debug
		self.debug_bounding_box = False

	def load ( self, base_path, images ):
		for img in images:
			self._images.append(
				pygame.image.load( os.path.join (
					base_path, img ) ))

		self.w = self._images[0].get_width()
		self.h = self._images[0].get_height()

	def get_curr_img( self ):
		return self._images[ int (self._curr_img) ]

	def update(self):
		self._curr_img += self.update_rate
		self._curr_img %= len(self._images)

	def blit( self ):
		self._surf.blit(self.get_curr_img(), (self.x, self.y) )

		if self.debug_bounding_box:
			pygame.draw.rect( self.surf, (255, 0, 0),
				(self.x, self.y, self.w, self.h), 1 )
