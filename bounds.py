def check(x, y):
	left = x
	top = y
	right = x + 16
	bottom = y + 32
	
	if left < 0 or right > 6345:  # beginning and flag
		return False

	if (top > 365):
		if ((left > 2200 and right < 2263) or (left > 2746 and right < 2843) or	(left >	4890 and right < 4950)): # gaps
			pass
                else: # ground
                        return False


	# pipes

	if (right > 890) and (left < 952):
# 		print '1st pipe xrange'
		if (bottom > 333) and (top < 397):
#			print '1st pipe'
			return False

        if (right > 1209) and (left < 1273):
                if (bottom > 301) and (top < 397):
#			print '2nd pipe'
                        return False
        if (right > 1464) and (left < 1528):
                if (bottom > 270) and (top < 397):
 #                       print '3rd pipe'
			return False
        if (right > 1816) and (left < 1878):
                if (bottom > 270) and (top < 397):
  #                      print '4th pipe'
			return False
        if (right > 5208) and (left < 5269):
                if (bottom > 333) and (top < 397):
   #                     print '5th pipe'
			return False
        if (right > 5719) and (left < 5782):
                if (bottom > 333) and (top < 397):
    #                    print '6th pipe'			
                        return False




	# blocks

        if (right > 505) and (left < 537):
#		print '1st block xrange'
                if (bottom > 270) and (top < 300):
#                	print '1st block'
                        return False

        if (right > 633) and (left < 793):
                if (bottom > 270) and (top < 300):
#                        print '2nd block'
                        return False
        if (right > 697) and (left < 729):
                if (bottom > 140) and (top < 173):
#                        print '3rd block'
                        return False
        if (right > 2456) and (left < 2552):
                if (bottom > 270) and (top < 300):
#                        print '4th block'
                        return False
        if (right > 2551) and (left < 2807):
                if (bottom > 140) and (top < 173):
#                        print '5th block'
                        return False
        if (right > 2905) and (left < 3032):
                if (bottom > 140) and (top < 173):
#                        print '6th block'
                        return False
        if (right > 3000) and (left < 3032):
                if (bottom > 270) and (top < 300):
#                        print '7 block'
                        return False
                        
        if (right > 3191) and (left < 3255):
                if (bottom > 270) and (top < 300):
#                        print '8rd block'
                        return False
                        
        if (right > 3384) and (left < 3415):
                if (bottom > 270) and (top < 300):
#                        print '9th block'
                        return False
 
        if (right > 3480) and (left < 3511):
                if (bottom > 270) and (top < 300):
#                        print '10th block'
                        return False
 
        if (right > 3576) and (left < 3607):
                if (bottom > 270) and (top < 300):
#                        print '11th block'
                        return False
 
        if (right > 3480) and (left < 3511):
                if (bottom > 140) and (top < 173):
#                        print '12nd block'
                        return False
 
        if (right > 3768) and (left < 3801):
                if (bottom > 270) and (top < 300):
#                        print '13rd block'
                        return False
 
        if (right > 3864) and (left < 3960):
                if (bottom > 140) and (top < 173):
#                        print '14th block'
                        return False
 
        if (right > 4086) and (left < 4215):
                if (bottom > 140) and (top < 173):
#                        print '15th block'
                        return False
 
        if (right > 4119) and (left < 4183):
                if (bottom > 270) and (top < 300):
#                        print '16th block'
                        return False
 
        if (right > 5368) and (left < 5496):
                if (bottom > 270) and (top < 300):
#                        print '17th block'
                        return False
	return True
