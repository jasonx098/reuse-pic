from PIL import Image
from pixel import PixelSq
import canvas 
import time

""" Globals """
size = 40 # size of square width and height
cropSize = (1000, 1000) # size of cropped image (x, y)
numSqX = int(cropSize[0]/size) # number of x coordinate squares
numSqY = int(cropSize[1]/size) # number of y coordinate squares

# given an image, return back a list of squares
def squares(img):
	squareList = []
	for i in range(numSqX):
		for j in range(numSqY):
			squareList.append(getSquare(img, i, j))
	squareList.sort(key = lambda x: x.avgGray)

	return squareList

# PixelSq if it is a From square
def getSquare(img, i, j):
	return PixelSq(img.crop((i*size, j*size, (i+1)*size, (j+1)*size)), size, i, j)


# given a pixel and the correspondg list of pixels, return a list of sorted priorities of pixels
def priorities(pix, corPixList):
	priList = corPixList
	priList.sort(key = lambda x: abs(x.avgGray - pix.avgGray))
	return priList


# given a map(pixel, list[pixel]) from priority and a map to priority, match them together, 
# return a hash list of FROM to which TO.
def matching(fromPriorities, toPriorities):
	fromPixList = list(fromPriorities.keys())
	toPixList = list(toPriorities.keys())

	mapAskList = {fromPix: [False] * len(toPriorities) for fromPix in fromPriorities.keys()}
	fromMatch = {fromPix:None for fromPix in fromPriorities.keys()}
	toMatch = {toPix:None for toPix in toPriorities.keys()}

	while (None in fromMatch.values()):
		# could do this faster if for all from pixels kept unique "askList"

		# first asking pix that is not matched
		askingPix = next(fromPix for fromPix in fromPixList if fromMatch[fromPix] is None)

		# first unasked toPix in priority list
		askList = mapAskList[askingPix]
		askInd = askList.index(False)

		askList[askInd] = True

		# if toPix is single
		if (toMatch[toPixList[askInd]] is None):
			toMatch[toPixList[askInd]] = askingPix
			fromMatch[askingPix] = toPixList[askInd]

		else:
			toPix = toPixList[askInd]
			# if toPix prefers askingPix
			toPixPri = toPriorities[toPix]

			# CHECK IF THIS IS THE RIGHT ORDER
			if (toPixPri.index(askingPix) < toPixPri.index(toMatch[toPix])):
				# rejected pixel
				reject = toMatch[toPix]
				fromMatch[reject] = None
				toMatch[toPix] = askingPix
				fromMatch[askingPix] = toPix

	return fromMatch


# Finds which From PixelSqs map to the corresponding To PixelSqs. Returns Map(From, To)
def mapFromtoTo(pathFrom, pathTo):

	imgFrom = Image.open(pathFrom).convert("L").resize(cropSize)
	imgTo = Image.open(pathTo).convert("L").resize(cropSize)

	# sorted list of PixelSq for From pic
	start = time.time()
	sqFrom = squares(imgFrom)
	end = time.time()
	print("sort from pic: " + str(end - start))

	# sorted list of PixelSq for To Pic
	start = time.time()
	sqTo = squares(imgTo)
	end = time.time()
	print("sort to pic: " + str(end - start))

	# generating priority maps
	start = time.time()
	fromPriorities = {pix:priorities(pix, sqTo) for pix in sqFrom}
	toPriorities = {pix:priorities(pix, sqFrom) for pix in sqTo}
	end = time.time()
	print("priorities: " + str(end - start))

	# matching algorithm
	start = time.time()
	fromMatch = matching(fromPriorities, toPriorities)
	end = time.time()
	print("Matching: " + str(end - start))

	# checks for matching bijection
	if (len(fromMatch.keys()) > len(set(fromMatch.keys()))):
		print("NOPE")
	if (len(fromMatch.values()) > len(set(fromMatch.values()))):
		print("NOPE")

	return fromMatch


def main():
	pathFrom = "glover.jpg"
	pathTo = "frank.jpg"

	fromMatch = mapFromtoTo(pathFrom, pathTo)
	canvas.makeCanvas(fromMatch)

if __name__ == "__main__":
	main()





