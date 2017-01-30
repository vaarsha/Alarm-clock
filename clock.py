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
 
print "Alarm Clock".center(80)+"\n"  #prints text in center of the screen
while True:
    hr = int(raw_input("Enter the hour you want to receive notification: "))
    mn = int(raw_input("Enter the minute you want to receive notification: "))
    print "You want to receive notification at " \
            " %d : %d" %(hr,mn)+" right?" 
    ipt = raw_input("Enter 'n' to reset values otherwise 'y' to continue\n")
    if ipt == 'y':
        break
time1 = timedelta(hours=hr,minutes=mn) #Can do arithmetic operations with it
reqdtime = datetime.now().time() #Take value as current time, it is datetime object
time2 = timedelta(hours = reqdtime.hour,minutes = reqdtime.minute,seconds = reqdtime.second) 
if time2 > time1: #case for if time less than current time
    print "Time has past you cannot set alarm for it!!"
elif timedelta(hours = reqdtime.hour) == timedelta(hours = hr): #within the same hour
    while timedelta(minutes = reqdtime.minute) != timedelta(minutes = mn):
        left = timedelta(minutes = mn)-timedelta(minutes = reqdtime.minute, seconds = reqdtime.second)
        reqdtime = datetime.now().time()
    alarm() #notifies
else:
    while time2!=time1:
        left = timedelta(hours = hr,minutes = mn)-timedelta(hours = reqdtime.hour,minutes = reqdtime.minute)
        reqdtime = datetime.now().time()
    alarm() #notifies
