from PIL import Image
from pixel import PixelSq
import time
import reuse as r

# given an image, return back a list of squares
def squares(img):
	squareList = []
	for i in range(r.numSqX):
		for j in range(r.numSqY):
			squareList.append(getSquare(img, i, j))

	return squareList


# PixelSq if it is a From square
def getSquare(img, i, j):
	return PixelSq(img.crop((i*r.size, j*r.size, (i+1)*r.size, (j+1)*r.size)), r.size, i, j)


# given a pixel and the correspondg list of pixels, return a list of sorted priorities of pixels
def priorities(pix, corPixList):
	priList = corPixList
	priList.sort(key = lambda x: abs(x.avgGray - pix.avgGray), reverse = True)
	return priList


# given a map(pixel, list[pixel]) from priority and a map to priority, match them together, 
# return a hash list of FROM to which TO. Uses Gale Shapley matching algorithm
def matching(fromPriorities, toPriorities):
	fromPixList = list(fromPriorities.keys())
	toPixList = list(toPriorities.keys())

	mapAskList = {fromPix: [False] * len(toPriorities) for fromPix in fromPriorities.keys()}
	fromMatch = {fromPix:None for fromPix in fromPriorities.keys()}
	toMatch = {toPix:None for toPix in toPriorities.keys()}

	while (None in fromMatch.values()):

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
			# if toPix prefers askingPix
			toPix = toPixList[askInd]
			toPixPri = toPriorities[toPix]
			if (toPixPri.index(askingPix) < toPixPri.index(toMatch[toPix])):
				# rejected pixel
				reject = toMatch[toPix]
				fromMatch[reject] = None
				toMatch[toPix] = askingPix
				fromMatch[askingPix] = toPix

	return fromMatch


# Given a sorted list of PixelSq for To and From, Returns one to one Map(From, To)
def mapFromtoTo(sqFrom, sqTo):
	# generating priority maps
	start = time.time()
	fromPriorities = {pix:priorities(pix, sqTo) for pix in sqFrom}
	toPriorities = {pix:priorities(pix, sqFrom) for pix in sqTo}
	end = time.time()
	print("Priorities: " + str(end - start))

	# matching algorithm
	start = time.time()
	fromMatch = matching(fromPriorities, toPriorities)
	end = time.time()
	print("Matching: " + str(end - start))

	return fromMatch


# Given image paths, loads image in gray scale and crops, returns
# a list of PixelSq for To and From pics
def getPixelList(pathFrom, pathTo):
	imgFrom = Image.open(pathFrom).convert("L").resize(r.cropSize)
	imgTo = Image.open(pathTo).convert("L").resize(r.cropSize)

	# list of PixelSq for From and To pic
	start = time.time()
	sqFrom = squares(imgFrom)
	sqTo = squares(imgTo)
	end = time.time()
	print("PixelSq list: " + str(end - start))

	return (sqFrom, sqTo)







