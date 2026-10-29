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


# The Robot needs to do a Figure at when there are two obstacles at
# 16 inches apart from one another

@event.is_press('a')
def main():
    figure8()

@event.is_press('b')
def stop():
    cyberpi.led.off()
    mbot2.EM_stop("all")
    cyberpi.stop_all()

# RPM Outer = RPM * (1 + Wheelbase / Distance between circles)
# RPM Inner = RPM * (1 - Wheelbase / Distance between Circles)
# Time = (60 * Distance between circles ) / (RPM * Diameter of wheels)
# Diameter of wheels = 6.2cm
# Wheelbase = 12cm
# Distance = 16 in (40.64 cm)

# Speeds in RPM
# speed_em1 = mbot2.encoder_motor.get_speed("EM1")
# speed_em2 = mbot2.encoder_motor.get_speed("EM2")

# Circle one
# Set left motor to V_inner
# Set right motor to V_outer
# Delay for X time

# Circle Two
# Set left motor to V_outer
# Set right motor to V_inner
# Delay for X time

def figure8():
    # Constants
    D = 20.32 # half the distance between circles
    W = 11.95 * 0.5 # Accounting for the WheelBase Distance itself
    d_w = 6.45
    # Motor RPM Calcuations
    base_motor_speed = 255
    max_motor_speed = 225
    max_rpm = 125
    base_RPM = (base_motor_speed * max_rpm) / max_motor_speed
    # Values are 0 to 255; max RPM is 125

    # Rpm Calculation for the inner wheel and outer wheels
    Rpm_inner = base_RPM * (1 - (W/D))
    Rpm_outer = base_RPM * (1 + (W/D))

    # Time calucations
    t = (60 * D) / (base_RPM * d_w)

    # Main Figure 8 Loop
    mbot2.EM_set_speed(Rpm_inner, "EM1")
    mbot2.EM_set_speed(-(Rpm_outer), "EM2")
    time.sleep(t*2)
    mbot2.EM_set_speed(Rpm_outer, "EM1")
    mbot2.EM_set_speed(-(Rpm_inner), "EM2")
    time.sleep(t*2)
    mbot2.EM_set_speed(0, "EM1")
    mbot2.EM_set_speed(0, "EM2")