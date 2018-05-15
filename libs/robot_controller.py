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
import time
import math


class Snatch3r(object):

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert self.arm_motor.connected
        self.touch_sensor = ev3.TouchSensor()
        assert self.touch_sensor.connected

    def drive_inches(self, distance, speed):
        assert self.left_motor.connected
        assert self.right_motor.connected

        if distance < 0:
            speed = -speed
            distance = distance * 90
        else:
            distance=distance*90
        self.left_motor.run_to_rel_pos(speed_sp=speed, position_sp=distance)
        self.right_motor.run_to_rel_pos(speed_sp=speed,position_sp=distance)
        """.run_to_rel_pos we dont need the stop action"""
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def turn_degrees(self, degree, speed):
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.left_motor.run_to_rel_pos(position_sp=degree*450/90, speed_sp=speed)
        self.right_motor.run_to_rel_pos(position_sp=-degree*450/90, speed_sp=speed)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def stop(self):
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.right_motor.stop()
        self.left_motor.stop()
        ev3.Sound.beep().wait()

    def arm_calibration(self):
        """calibrate the robot arm """
        assert self.arm_motor.connected
        touch_sensor = ev3.TouchSensor()
        self.arm_motor.run_forever(speed_sp=800)
        while not touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        ev3.Sound.beep().wait()
        self.arm_motor.run_to_rel_pos(position_sp=0, speed_sp=900)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()
        self.arm_motor.position = 0

    def arm_up(self):
        assert self.arm_motor.connected
        touch_sensor = ev3.TouchSensor()
        self.arm_motor.run_forever(speed_sp=900)
        while not touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def arm_down(self):
        assert self.arm_motor.connected
        self.arm_motor.run_to_abs_pos(position_sp=0, speed_sp=-900)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def shutdown(self):
        btn = ev3.Button()
        while btn.backspace:
            self.stop()
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Sound.speak("good game").wait()
            print('Goodbye')

    def go_forward(self, left_motor_speed, right_motor_speed):
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.left_motor.run_forever(speed_sp=left_motor_speed)
        self.right_motor.run_forever(speed_sp=right_motor_speed)

    def go_back(self, left_motor_speed, right_motor_speed):
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.left_motor.run_forever(speed_sp=-left_motor_speed)
        self.right_motor.run_forever(speed_sp=-right_motor_speed)

    def turn_right(self, left_motor_speed, right_motor_speed):
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.left_motor.run_forever(speed_sp=left_motor_speed)
        self.right_motor.run_forever(speed_sp=-right_motor_speed)

    def turn_left(self, left_motor_speed, right_motor_speed):
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.left_motor.run_forever(speed_sp=-left_motor_speed)
        self.right_motor.run_forever(speed_sp=right_motor_speed)

    def  loop_forever(self):
        while True:
            time.sleep(0.01)




