import sys
sys.path.append(".")
sys.path.append("..")
from consts import leftMotor
from stepMotor import stepMotor

motor = stepMotor(leftMotor)
motor.start()
motor.turnOn()

while(True): 
    pass