import RPi.GPIO as GPIO
from consts import halfstep_seq
import time

class stepMotor(object):
    def __init__(self, control_pins):
        GPIO.setmode(GPIO.BOARD)
        self.control_pins = control_pins
        self.running = False
        self.on = False
        self.clockwise = True
        self.freq = 0.001
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    def turn(self):
        for x in range(8):
            if self.clockwise:
                i = x
            else:
                i = 7-x
            self.setOutput(i)
            time.sleep(self.freq)
            if not self.on:
                    break 

    def setOutput(self, halfstep):
        for pin in range(4):
            GPIO.output(self.control_pins[pin], halfstep_seq[halfstep][pin])

    def setDirection(self, clockwise):
        if clockwise:
            self.clockwise = True
        else:
            self.clockwise = False

    def start(self):
        self.on = True

    def stop(self):
        self.on  = False

    def turnOn(self):
        self.running = True
        while(self.running):
            time.sleep(self.freq)
            while(self.on):
               self.turn()
    
    def turnOff(self):
        self.running = False

    def setSpeed(self, s):
        self.freq = 0.001 / s

    def reset(self):
        self.freq = 0.001

    def close(self):
        GPIO.cleanup
