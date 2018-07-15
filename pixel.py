from PIL import Image, ImageStat

"""
Class to contain the pixel square as well as information 
needed for the pixel, such as the size, and if necessary, x and y placements.
Also stores the average gray scale value for the pixel square
"""

class PixelSq:
	def avgGray(self):
		pix = self.square.load()
		sumGray = 0
		for i in range(self.size):
			for j in range(self.size):
				sumGray += pix[i, j]
		return int(sumGray / (self.size * self.size))

	def __init__(self, square, size, x = None, y = None):
		self.square = square
		self.x = x
		self.y = y
		self.size = size
		self.avgGray = self.avgGray()

	


