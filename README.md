# reuse-pic
Rearranges small squares from a source image to best fit a target image. Extracts small squares of pixels from a source image and uses a Gale-Shapley matching algorithm to assign each square with a corresponding target square. Overlays the new squares onto the target photo. Done on July 14-15th 2018

### How to use
Dependencies: Python3, Pillow

Add selected images into img directory. Change parameters in reuse.py. Run with `python reuse.py`

### Samples
From Picture: Donald Glover

<img src="img/glovergray.png" height="400" width="400">

To Picture: Frank Ocean

<img src="img/frankgray.png" height="400" width="400">

Result:

<img src="img/newfrank.png" height="400" width="400">
