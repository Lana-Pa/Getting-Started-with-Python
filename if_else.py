score = raw_input("Enter Score between 0.0 and 1.0: ")
sc = float(score)
if 0.0 <= sc <= 1.0:
    if sc >= 0.9: print "A"
    elif sc >= 0.8: print "B"
    elif sc >= 0.7: print "C"
    elif sc >= 0.6: print "D"
    else: print "F"
else:
    print "You are out of range."