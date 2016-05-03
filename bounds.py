def check(x, y):
	left = x
	top = y
	right = x + 16
	bottom = y + 32
	
	if left < 0 or right > 6345:  # beginning and flag
		return False
	elif (top > 365):
		print 'somewhere down low'
		print 'l: ' + str(left)
		print 'r: ' + str(right)	
		if ((left < 2200) or (right > 2263 and left < 2746) or (right > 2843 and left < 4890) or (right > 4950)):  # ground  
			return False
	else:
		return True
