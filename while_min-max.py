total = 0
count = 0
minv = None
maxv = None

while True:
    inp= raw_input("Enter a number: ")
    if inp == "done":
        print "Done!"
        break
    try:
        i = float(inp)
        count = count + 1
        total = total + i
        if minv is None or i < minv:
            minv = i
        if maxv is None or i > maxv:
            maxv = i

    except:
        print "Bad input"
print "Count", count
print "Total", total
print "Max", maxv
print "Min", minv
