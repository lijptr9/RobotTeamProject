"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

        assert self.left_motor.connected
        assert self.right_motor.connected

        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert self.arm_motor.connected

        self.ir_sensor = ev3.InfraredSensor()
        assert self.ir_sensor

        self.color_sensor = ev3.ColorSensor()
        assert self.color_sensor


        self.touch_sensor = ev3.TouchSensor()
        assert self.touch_sensor

        self.pwr = ev3.PowerSupply()

        self.running = True


    def forward(self, inches, speed=100, stop_action= 'brake'):
        k = 360/4.5
        degrees_for_motor_to_run = k* inches
        self.left_motor.run_to_rel_pos(speed_sp= 8*speed, position_sp= degrees_for_motor_to_run, stop_action= stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=8*speed, position_sp=degrees_for_motor_to_run, stop_action=stop_action)

        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')

    def loop_forever(self):
        self.running = True
        while self.running:
            #   "Self Defense" mode developed by Shengbo Zou
            if self.ir_sensor.proximity < 10:
                self.pinch()
                ev3.Sound.speak("Don't touch me. Now back off").wait()
                time.sleep(1.5)
                self.release()
            time.sleep(0.1)

    def pinch(self):
        self.arm_motor.run_forever(speed_sp=900)
        time.sleep(1.5)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)

    def shut_down(self):
        self.running = False






    
    # DONE: Implement the Snatch3r class as needed when working the sandox exercises
    # (and delete these comments)
    def arm_calibration(self):
        # arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        # assert arm_motor.connected
        #
        # touch_sensor = ev3.TouchSensor()
        # assert touch_sensor

        self.arm_motor.run_forever(speed_sp=900)

        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        ev3.Sound.beep()
        arm_revolutions_for_full_range = 14.2
        self.arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range * 360)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep()
        self.arm_motor.position = 0


    def arm_up(self):
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        ev3.Sound.beep()

    def arm_down(self):
        self.arm_motor.run_to_abs_pos(position_sp=0, speed_sp=900)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Blocks until the motor finishes running
        ev3.Sound.beep()

    def release(self):
        self.arm_motor.run_forever(speed_sp=-900)
        time.sleep(1.5)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)



    def shutdown(self):
        # Modify a variable that will allow the loop_forever method to end. Additionally stop motors and set LEDs green.
        # The most important part of this method is given here, but you should add a bit more to stop motors, etc.
        self.running = False