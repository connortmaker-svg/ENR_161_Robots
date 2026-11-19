import time 
import event
import cyberpi
import mbot2
import mbuild

@event.start
def setup():
    cyberpi.display.show_label("A = GO", 16, 0, 0, 0)
    cyberpi.display.show_label("B = STOP", 16, 0, 20, 1)
    cyberpi.display.show_label("JOY DOWN = STOP", 16, 0, 40, 2)

def stop():
    cyberpi.led.off()
    mbot2.EM_stop("all")
    cyberpi.stop_all()
    
@event.is_press('a')
def main():
    stop_on_color()

@event.is_press('b')
def main2():
    stop_25cm_from_obstacle()

def stop_on_color():
    mbot2.drive_speed(50,50)
    while True:
        if mbuild.quad_rgb_sensor.get_color_sta("L1", 1) == "red":
            break
        if cyberpi.controller.is_press("down"):
            break
        time.sleep(0.02)
    stop()

def stop_25cm_from_obstacle():
    mbot2.drive(50,50)
    while True:
        distance = mbuild.ultrasonic2.get(1)
        if 0 < distance <= 25:
            break
        if cyberpi.controller.is_press("down"):
            break
        time.sleep(0.02)
    stop()
