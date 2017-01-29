import datetime
print "Alarm Clock".center(80)+"\n"
while True:
    hr = int(raw_input("Enter the hour you want to receive notification: "))
    mn = int(raw_input("Enter the minute you want to receive notification: "))
    print "You want to receive notification at " \
            " %d : %d right?",(hr,mn) 
    ipt = raw_input("Enter 'n' to reset values otherwise 'y' to continue\n")
    if ipt == 'y':
        break
reqdtime = datetime.datetime.now().time()
if reqdtime.hour > hr and reqdtime.min > mn:
    print "Time has past you cannot set alarm for it!!"
elif reqdtime.hour == hr:
    while reqdtime.min != mn:
        print "You have ",int(reqdtime.min)-mn," minutes left"
        reqdtime = datetime.datetime.now().time()
    print "Alarm"
else:
    while reqdtime.hour != hr and reqdtime.min != mn:
        print "You have ",reqdtime.min-mn," minutes left"
        reqdtime = datetime.datetime.now().time()
    else:
        print "Alarm time"


print datetime.datetime.now().time()


