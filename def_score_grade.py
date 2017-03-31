def computegrade(sc):
    try:
        sc = float(sc)
        if 0.0 <= sc <= 1.0:
            if sc >= 0.9:
                return "A"
            elif sc >= 0.8:
                return "B"
            elif sc >= 0.7:
                return "C"
            elif sc >= 0.6:
                return "D"
            else:
                return "F"
        else:
            return "Out of range"
    except:
        return "Bad input"

score = raw_input("Enter Score between 0.0 and 1.0: ")
grade = computegrade(score)
print grade
