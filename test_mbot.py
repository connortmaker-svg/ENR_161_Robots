import time 
import event
import cyberpi
import mbot2
import mbuild

@event.start
def setup():
    cyberpi.console.clear()
    cyberpi.console.println("READY") #Prints in the console
    cyberpi.display.show_label("READY", 16, 0, 0, 0)

@event.is_press('a')
def main():
    cyberpi.display.show_label("PRESS A", 16, 0, 20, 1)
    while not cyberpi.controller.is_press('a'):
        pass

    mbot2.EM_set_speed(100, "EM1")
    mbot2.EM_set_speed(100, "EM2")