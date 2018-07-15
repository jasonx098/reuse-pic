from PIL import Image
from pixel import PixelSq
import time

""" Globals """
size = 25 # size of square width and height
cropSize = (1000, 1000) # size of cropped image (x, y)
numSqX = int(cropSize[0]/size) # number of x coordinate squares
numSqY = int(cropSize[1]/size) # number of y coordinate squares

def makeCanvas(fromMatch):
	newTo = Image.new("L", cropSize)

	for fromPix in fromMatch:
		toPix = fromMatch[fromPix]
		newTo.paste(fromPix.square, 
			(toPix.x*toPix.size, toPix.y*toPix.size, (toPix.x+1)*toPix.size, (toPix.y+1)*toPix.size))

	newTo.show()
	