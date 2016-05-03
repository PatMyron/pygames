def check(x, y):
	left = x
	top = y
	right = x + 16
	bottom = y + 32
	
	if left < 0 or right > 6345:  # beginning and flag
		return False

	elif (top > 365):
		if ((left > 2200 and right < 2263) or (left > 2746 and right < 2843) or	(left >	4890 and right < 4950)):
                        return True
                else:
                        return False
	else:
		return True
