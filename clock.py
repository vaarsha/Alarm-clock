import datetime
print "Alarm Clock".center(80)+"\n"
while True:
    hr = raw_input("Enter the hour you want to receive notification: ")
    mn = raw_input("Enter the minute you want to receive notification: ")
    print "You want to receive notification at " \
            + hr+":"+mn+" right?" 
    ipt = raw_input("Enter 'n' to reset values otherwise 'y' to continue\n")
    if ipt == 'y':
        break


