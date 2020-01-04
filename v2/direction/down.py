import sys
sys.path.append("..")
from consts import rightMotor
from stepMotor import stepMotor

motor = stepMotor(rightMotor)
motor.start()
motor.clockwise = False
motor.turnOn()

while(True):
    pass