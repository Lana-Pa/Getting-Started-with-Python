def computepay(h,r):
    extra_hrs = h - 40
    extra_rate = 1.5 * r
    extra_pay = extra_hrs*extra_rate
    return extra_pay

h = raw_input("Enter Hours:")
r = raw_input("Enter Rate:")
hrs = float(h)
rate = float(r)

extra = computepay(hrs, rate)
if hrs > 40:
    gross_pay = 40*rate + extra
else:
	gross_pay = hrs*rate

print "Pay: ",gross_pay