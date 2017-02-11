def check(x, y):
	left = x
	top = y
	right = x + 16
	bottom = y + 32
	
	if left < 0 or right > 6345:  # beginning and flag
		return False

	if (top > 365):
		if ((left > 2200 and right < 2263) or (left > 2746 and right < 2843) or	(left >	4888 and right < 4950)): # gaps
			pass
		else: # ground
			return False


	arrays = [
	# pipes
	[890, 333, 952, 397],
	[1209, 301, 1273, 397],
	[1464, 270, 1528, 396],
	[1816, 270, 1878, 398],
	[5208, 333, 5269, 397],
	[5719, 333, 5782, 397],
	#blocks
	[505, 270, 537, 300],
	[633, 270, 793, 300],
	[697, 140, 729, 173],
	[2456, 270, 2552, 300],
	[2551, 140, 2807, 173],
	[2905, 140, 3032, 173],
	[3000, 270, 3032, 300],
	[3191, 270, 3255, 300],
	[3384, 270, 3415, 300],
	[3480, 270, 3511, 300],
	[3576, 270, 3607, 300],
	[3480, 140, 3511, 173],
	[3768, 270, 3801, 300],
	[3864, 140, 3960, 173],
	[4086, 140, 4215, 173],
	[4119, 270, 4183, 300],
	[5368, 270, 5496, 300],
	[6329, 364, 6362, 397]
	]
	for array in arrays:
		if (right > array[0]) and (left < array[2]):
			if (bottom > array[1]) and (top < array[3]):
				return False
	

	# stairs
	
	# 1st staircase
	if (right > 4280) and (left < 4407):
			if (bottom > 365) and (top < 397):
					return False
	if (right > 4312) and (left < 4407):
			if (bottom > 333) and (top < 397):
					return False
	if (right > 4344) and (left < 4407):
			if (bottom > 300) and (top < 397):
					return False
	if (right > 4376) and (left < 4407):
			if (bottom > 269) and (top < 397):
					return False
	

	# 3rd staircase
	if (right > 4727) and (left < 4888):
			if (bottom > 365) and (top < 397):
					return False
	if (right > 4759) and (left < 4888):
			if (bottom > 333) and (top < 397):
					return False
	if (right > 4791) and (left < 4888):
			if (bottom > 300) and (top < 397):
					return False
	if (right > 4823) and (left < 4888):
			if (bottom > 269) and (top < 397):
					return False
	
	
	# 5th staircase
	if (right > 5784) and (left < 6073):
			if (bottom > 365) and (top < 397):
					return False
	if (right > 5816) and (left < 6073):
			if (bottom > 333) and (top < 397):
					return False
	if (right > 5848) and (left < 6073):
			if (bottom > 300) and (top < 397):
					return False
	if (right > 5880) and (left < 6073):
			if (bottom > 269) and (top < 397):
					return False
	if (right > 5912) and (left < 6073):
			if (bottom > 237) and (top < 397):
					return False
	if (right > 5944) and (left < 6073):
			if (bottom > 205) and (top < 397):
					return False
	if (right > 5976) and (left < 6073):
			if (bottom > 173) and (top < 397):
					return False
	if (right > 6008) and (left < 6073):
			if (bottom > 140) and (top < 397):
					return False
	
	
	# 2nd staircase
	if (right > 4470) and (left < 4599):
			if (bottom > 365) and (top < 397):
					return False
	if (right > 4470) and (left < 4567):
			if (bottom > 333) and (top < 397):
					return False
	if (right > 4470) and (left < 4535):
			if (bottom > 300) and (top < 397):
					return False
	if (right > 4470) and (left < 4503):
			if (bottom > 269) and (top < 397):
					return False

						
	# 4th staircase
	if (right > 4950) and (left < 5080):
			if (bottom > 365) and (top < 397):
					return False
	if (right > 4950) and (left < 5048):
			if (bottom > 333) and (top < 397):
					return False
	if (right > 4950) and (left < 5016):
			if (bottom > 300) and (top < 397):
					return False
	if (right > 4950) and (left < 4984):
			if (bottom > 269) and (top < 397):
					return False
	
	return True
