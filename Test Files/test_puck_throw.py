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
    if not mbuild.quad_rgb_sensor.get_line_sta("all", 1):
        mbot2.drive_power(255, -255)
    else:
        mbot2.drive_power(0, 0)
     


@event.is_press('b')
def stop():
    cyberpi.led.off()
    mbot2.EM_stop("all")
    cyberpi.stop_all()