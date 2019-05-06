import sys
sys.path.append("..")
from consts import rightMotor
from stepMotor import stepMotor

motor = stepMotor(rightMotor)
motor.start()
motor.turnOn()

while(True):
    pass