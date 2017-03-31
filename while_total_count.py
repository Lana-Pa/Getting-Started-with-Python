total = 0
count = 0
average = 0
while True:
    inp= raw_input("Enter a number: ")
    if inp == "done":
        print "Done!"
        break
    try:
        i = float(inp)
        count = count + 1
        total = total + i
        average = total / count

    except:
        print "Bad input"
print "Count", count
print "Total", total
print "Average", average