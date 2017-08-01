numbers = []

for i in range(0, 6):
    print "The number is %d" % i
    numbers.append(i)
    print "The numbers is: ", numbers

n = 0
number = []

if n < 3:
    print "The num. is %d" % n
    number.append(n)
    print "The num. is: ", number
    n += 1

    if n < 3:
        print "The num. is %d" % n
        number.append(n)
        print "The num. is: ", number
        n += 1

        if n < 3:
            print "The num. is %d" % n
            number.append(n)
            print "The num. is: ", number
            n += 1

            if n < 3:
                print "The num. is %d" % n
                number.append(n)
                print "The num. is: ", number
                n += 1
            else:
                print "End."
else:
    print "End."
