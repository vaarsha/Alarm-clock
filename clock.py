from datetime import datetime,timedelta
import alrm
def alarm():
    print "Alarm Time"
    val = ""
    while True:
        val = alrm.timeout()
        if val == "stop":
            break;
    print "Hey, You woke up finally"
    return
 
print "Alarm Clock".center(80)+"\n"
while True:
    hr = int(raw_input("Enter the hour you want to receive notification: "))
    mn = int(raw_input("Enter the minute you want to receive notification: "))
    print "You want to receive notification at " \
            " %d : %d" %(hr,mn)+" right?" 
    ipt = raw_input("Enter 'n' to reset values otherwise 'y' to continue\n")
    if ipt == 'y':
        break
time1 = timedelta(hours=hr,minutes=mn)
reqdtime = datetime.now().time()
time2 = timedelta(hours = reqdtime.hour,minutes = reqdtime.minute,seconds = reqdtime.second)
if time2 > time1:
    print "Time has past you cannot set alarm for it!!"
elif timedelta(hours = reqdtime.hour) == timedelta(hours = hr):
    while timedelta(minutes = reqdtime.minute) != timedelta(minutes = mn):
        left = timedelta(minutes = mn)-timedelta(minutes = reqdtime.minute, seconds = reqdtime.second)
        reqdtime = datetime.now().time()
    alarm()
else:
    while time2!=time1:
        left = timedelta(hours = hr,minutes = mn)-timedelta(hours = reqdtime.hour,minutes = reqdtime.minute)
        reqdtime = datetime.now().time()
    alarm()
