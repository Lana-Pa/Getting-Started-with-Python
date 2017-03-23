largest = None
smallest = None
count = 0
while True:
    nums = raw_input("Enter a number: ")
    if nums == "done": break
    try:
        num = int(nums)

        if largest is None or num > largest:
           largest = num
        if smallest is None or num < smallest:
            smallest = num
        count = count + 1
    except:
       print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest