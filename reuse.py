from PIL import Image, ImageStat
from pixel import PixelSq
import time

""" Globals """
size = 500 # size of square width and height
cropSize = (1000, 1000) # size of cropped image (x, y)
numSqX = int(cropSize[0]/size) # number of x coordinate squares
numSqY = int(cropSize[1]/size) # number of y coordinate squares

# given an image, return back a list of squares
def squares(img, to):
	squareList = []
	for i in range(numSqX):
		for j in range(numSqY):
			if (to):
				squareList.append(squareTo(img, i, j))
			else:
				squareList.append(squareFrom(img, i, j))

	squareList.sort(key = lambda x: x.avgGray)

	return squareList

# PixelSq if it is a From square
def squareFrom(img, i, j):
	return PixelSq(img.crop((i*size, j*size, (i+1)*size, (j+1)*size)), size)

# PixelSq if it is a To square
def squareTo(img, i, j):
	return PixelSq(
		img.crop((i*size, j*size, (i+1)*size, (j+1)*size)), size, i, j)

# given a pixel and the correspondg list of pixels, return a list of sorted priorities of pixels
def priorities(pix, corPixList):
	priList = corPixList
	priList.sort(key = lambda x: abs(x.avgGray - pix.avgGray))
	return priList

# given a map(pixel, list[pixel]) from priority and a map to priority, match them together, 
# return a hash list of FROM to which TO.
#def matching(fromPriorities, toPriorities):




# Finds which From PixelSqs map to the corresponding To PixelSqs. Returns Map(From, To)
def mapFromtoTo(pathFrom, pathTo):

	imgFrom = Image.open(pathFrom).convert("L").resize(cropSize)
	imgTo = Image.open(pathTo).convert("L").resize(cropSize)

	# sorted list of PixelSq for From pic
	start = time.time()
	sqFrom = squares(imgFrom, to = False)
	end = time.time()
	print("sort from pic: " + str(end - start))

	# sorted list of PixelSq for To Pic
	start = time.time()
	sqTo = squares(imgTo, to = True)
	end = time.time()
	print("sort to pic: " + str(end - start))

	# generating priority maps
	start = time.time()
	fromPriorities = {pix:priorities(pix, sqTo) for pix in sqFrom}
	toPriorities = {pix:priorities(pix, sqFrom) for pix in sqTo}
	end = time.time()
	print("priorities: " + str(end - start))

	print(fromPriorities)
	# matching algorithm





	#print([sq.avgGray for sq in sqFrom])









def main():
	pathFrom = "glover.jpg"
	pathTo = "frank.jpg"

	mapFromtoTo(pathFrom, pathTo)

if __name__ == "__main__":
	main()





