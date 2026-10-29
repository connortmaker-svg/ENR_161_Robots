import time 
import event
import cyberpi
import mbot2
import mbuild

@event.start
def setup():
    cyberpi.console.clear()
    cyberpi.console.println("READY") #Prints in the console
    cyberpi.console.clear()
    time.sleep(1)
    cyberpi.display.show_label("PRESS A to Start", 16, 0, 20, 1)
    cyberpi.display.show_label("PRESS B to Stop", 16, 0, 20, 1)

@event.is_press('a')
def main():
    mbot2.EM_set_speed(100, "EM1")
    mbot2.EM_set_speed(-100, "EM2")

@event.is_press('b')
def stop():
    cyberpi.led.off()
    mbot2.EM_stop("all")
    cyberpi.stop_all()