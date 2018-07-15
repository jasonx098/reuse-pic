from PIL import Image
from pixel import PixelSq
import time

""" Globals """
size = 40 # size of square width and height
cropSize = (1000, 1000) # size of cropped image (x, y)
numSqX = int(cropSize[0]/size) # number of x coordinate squares
numSqY = int(cropSize[1]/size) # number of y coordinate squares

newTo = Image.new("L", cropSize)
canvas = newTo.load()

for i in range(100):
	for j in range(100):
		canvas[i, j] = 155

newTo.show()