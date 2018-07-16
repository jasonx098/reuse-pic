from PIL import Image
from pixel import PixelSq
import canvas
import gif
from match import getPixelList, mapFromtoTo

""" Globals """
size = 500								# size of square width and height
cropSize = (1000, 1000) 				# size of cropped image (x, y)
numSqX = int(cropSize[0]/size) 			# number of x coordinate squares
numSqY = int(cropSize[1]/size) 			# number of y coordinate squares
pathFrom = "img/glover.jpg"				# From picture
pathTo = "img/frank.jpg" 				# To picture

def main():
	sqLists = getPixelList(pathFrom, pathTo)
	fromMatch = mapFromtoTo(sqLists[0], sqLists[1])
	newTo = canvas.makeCanvas(fromMatch)
	newTo.show()

	# Function to make a gif in directory "out"
	"""gif.makeGif(fromMatch, 
		Image.open(pathFrom).convert("L").resize(cropSize),
		Image.open(pathTo).convert("L").resize(cropSize))
	"""
if __name__ == "__main__":
	main()
