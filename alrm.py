import thread
import threading

def timeout(prompt, timeout=20.0):
    print "Alarm"  
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        while True:
            print "\a"
            astring = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring
val = ""
while True:
    val = timeout("If awake enter stop to shut the alarm\n")
    if val == "stop":
        break;

print val
        

