"""readme"""
- Store target photos in img directory
- All parameters the user needs to change are in reuse.py
	* Keep the numSqX and numSqY to be <= 40 for reasonable timing (1000x1000) with 40 takes 3 minutes
- Works best with photos of similar background shade
- Try to keep cropSize as a multiple of size for even results

"""Notes"""
initialize picture 
- Iterate through FROM picture and pick out squares, keep these in a list
- Do the same for TO picture 

what I need to do matching:
- Each FROM should have a list of priorities for TO
- Each TO should have a list of priorities for FROM
- Store these in a map(FROM item, List[To item])
- Some datastructure where:
	* if you look up TO, you get married FROM
	* if you look up FROM, you get married TO

when I match:
- Keep going in FROM list until find bachelor, while theyre not all taken
- Check if engaged prefered TO is engaged, 
		* if TO prefers this new engaged, switch and divorce the old FROM
			mark in hash lists?
		* if not prefers, continue down priority list

Should return:
- hashlist of FROM to their preferred TO, can look up coordinates in TO

Setting the picture:
- given this hashlist, create a new picture
- Go through the keys, mark their "value" TO coordinates with the FROM value

"""Open Problems to fix"""
- Slow matching algorithm
- Maybe try finding better library for photos
- Need some better testing
- Maybe averaging gray scale isn't that great
- Move to RGB?

