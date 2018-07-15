from PIL import Image
from pixel import PixelSq
import reuse as r

def makeCanvas(fromMatch):
	newTo = Image.new("L", r.cropSize)

	for fromPix in fromMatch:
		toPix = fromMatch[fromPix]
		newTo.paste(fromPix.square, 
			(toPix.x*toPix.size, toPix.y*toPix.size, (toPix.x+1)*toPix.size, (toPix.y+1)*toPix.size))

	return newTo
	