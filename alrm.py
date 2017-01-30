import thread
import threading

def timeout(timeout=20.0):
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = raw_input("If awake enter stop to shut the alarm\n")
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring
