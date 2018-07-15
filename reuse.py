from PIL import Image, ImageStat
from pixel import PixelSq

pathFrom = "glover.jpg"
pathTo = "frank.jpg"

# size of square width and height
size = 40

# size of cropped image (x, y)
cropSize = (1000, 1000)

numSqX = int(cropSize[0]/size)
numSqY = int(cropSize[1]/size)

# given an image, return back a list of squares
def squares(img):
	squareList = []
	for i in range(numSqX):
		for j in range(numSqY):
			squareList.append(
				PixelSq(
					img.crop((i*size, j*size, (i+1)*size, (j+1)*size)),
					size
					)
				)
	return squareList


def reuse(pathFrom, pathTo):

	imgFrom = Image.open(pathFrom).convert("L").resize(cropSize)
	imgTo = Image.open(pathTo).convert("L").resize(cropSize)
	#imgFrom.show()
	#imgTo.show()

	# list of PixelSq
	sqFrom = squares(imgFrom)
	sqTo = squares(imgTo)

reuse(pathFrom, pathTo)



