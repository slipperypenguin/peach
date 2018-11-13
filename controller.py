from stepMotor import stepMotor
import time

def calibrate(iters = 20):
    leftMotor = stepMotor([7,11,13,15])
    rightMotor = stepMotor([31,33,35,37])
    step = 512
    for i in range(iters):
        leftMotor.rotate(step)
        rightMotor.rotate(step)
        leftMotor.rotate(-step)
        rightMotor.rotate(-step)

    leftMotor.close()
    rightMotor.close()
