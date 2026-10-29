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

left_m = "EM1"
right_m = "EM2"

@event.is_press('a')
def main():
    line_follow()
    # mbot2.EM_set_speed(255, left_m) # Left Motor
    # mbot2.EM_set_speed(-255, right_m) # Right Motor


# STOP ALL FUNCTION
@event.is_press('b')
def stop():
    cyberpi.led.off()
    mbot2.EM_stop("all")
    cyberpi.stop_all()

def line_follow():
    # Variables and Tuning parameters
    base_power = 70 #Default speed when on a 'true' straight line
    kp = 30.0 # proportional gain
    ki = 0.0 # integral gain
    kd = 1.0 # derivative gain
    dt = 0.02 # loop period of the PID in seconds

    accumulated_integral = 0.0
    previous_error = 0.0
    last_seen_side = 1 # A value to rember if the line was seen to the left or the right via 

    # Main Line following loop
    while True:
        # This is to get the sensor reading from the line. 
        line_state = mbuild.quad_rgb_sensor.get_line_sta("all", 1)

        # Massive bit bang if the sensors loses the line by looking at the last know position
        if line_state == 0 or str(line_state) in ("0", "0000"):
            accumulated_integral = 0.0
            line_error = 1.0 * last_seen_side
            error_rate = 0.0
        # Main Error calculation
        else:
            # Scaling down the error by 100 
            line_error = mbuild.quad_rgb_sensor.get_offset_track(1) / 100.0
            # This adds the accumulated error over time; 
            # min and max functions prevent the number from growing infinitely large
            accumulated_integral = max(-1.0, min(1.0, accumulated_integral + line_error * dt))
            # Updates the last known position of the line.
            if line_error > 0.05:
                last_seen_side = 1
            elif line_error < -0.05:
                last_seen_side = -1
            # Calculate how fast the Error is changing over time. 
            error_rate = (line_error - previous_error) / dt


        previous_error = line_error
        # This is the calculation of the PID 
        # P = kp * line_error
        # I = ki * accumulated_integral
        # D = kd * error_rate
        steering_correction = (kp * line_error) + (ki * accumulated_integral) + (kd * error_rate)
        # This sets the steering speed bounds 
        total_steering_correction = max(-255.0, min(255.0, steering_correction))

        # Applying the error to the speed of the motors
        left_motor_power = base_power - total_steering_correction
        right_motor_power = -(base_power + total_steering_correction)
        mbot2.drive_power(left_motor_power, right_motor_power)

        time.sleep(dt) 