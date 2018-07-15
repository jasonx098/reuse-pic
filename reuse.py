from PIL import Image
from pixel import PixelSq
import canvas
from match import getPixelList, mapFromtoTo

""" Globals """
size = 25 								# size of square width and height
cropSize = (1000, 1000) 				# size of cropped image (x, y)
numSqX = int(cropSize[0]/size) 			# number of x coordinate squares
numSqY = int(cropSize[1]/size) 			# number of y coordinate squares
pathFrom = "img/frank.jpg"				# From picture
pathTo = "img/glover.jpg" 				# To picture

def main():
	sqLists = getPixelList(pathFrom, pathTo)
	fromMatch = mapFromtoTo(sqLists[0], sqLists[1])
	newTo = canvas.makeCanvas(fromMatch)
	newTo.show()

if __name__ == "__main__":
	main()
