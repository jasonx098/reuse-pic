from PIL import Image
from pixel import PixelSq
import imageio
import reuse as r
import os
import time
import shutil

# Create the final picture frame given a fromPic and a toPic
def combineImage(fromPic, toPic):
	div = 200
	size = (2*r.cropSize[0] + div, r.cropSize[1])
	comb = Image.new("L", size, color=255)
	comb.paste(fromPic, (0, 0, r.cropSize[0], r.cropSize[1]))
	comb.paste(toPic, (r.cropSize[0] + div, 0, r.cropSize[0] * 2 + div, r.cropSize[1]))
	return comb

# given the temporary pictures, add a new pixel square change
def pixStep(newFrom, newTo, fromMatch, fromPix, i):
	# white square
	white = Image.new("L", (r.size, r.size), color=255)
	toPix = fromMatch[fromPix]
	newTo.paste(fromPix.square, 
		(toPix.x*toPix.size, toPix.y*toPix.size, (toPix.x+1)*toPix.size, (toPix.y+1)*toPix.size))
	newFrom.paste(white, 
		(fromPix.x*fromPix.size, fromPix.y*fromPix.size, (fromPix.x+1)*fromPix.size, (fromPix.y+1)*fromPix.size))
	combineImage(newFrom, newTo).save('out/' + str(i + 2) + '.png')

# Given a mapping and the two images, create a gif in separate directory called out
def makeGif(fromMatch, imgFrom, imgTo):
	if os.path.exists("out"):
		shutil.rmtree("out")
	os.mkdir("out")
	fromPixList = list(fromMatch.keys())
	fromPixList.sort(key = lambda x: x.x + x.y, reverse=True)

	combineImage(imgFrom, imgTo).save('out/0.png')

	newFrom = imgFrom.copy()
	newTo = Image.new("L", r.cropSize, color=255)
	combineImage(newFrom, newTo).save('out/1.png')

	start = time.time()
	for i in range(len(fromPixList)):
		pixStep(newFrom, newTo, fromMatch, fromPixList[i], i)
	end = time.time()
	print("Generating pixels: " + str(end - start))

	start = time.time()
	filenames = os.listdir("out")
	filenames.sort(key = lambda x: int(x.split(".")[0]))
	filepaths = ["out/" + name for name in filenames]
	images = []

	with imageio.get_writer('out/transition.gif', mode='I') as writer:
		for filename in filepaths:
			image = imageio.imread(filename)
			writer.append_data(image)
	end = time.time()
	combineImage(imgTo, newTo).save('out/' + str(len(fromPixList) + 2) + '.png')
	print("Generating gif: " + str(end - start))

	filenames = os.listdir("out")
	savedFiles = ["transition.gif", "0.png", str(len(fromPixList) + 2) + ".png"]
	for file in filenames:
		if file not in savedFiles:
			os.remove("out/" + file) 
	



