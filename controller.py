from stepperMotor import stepperMotor

def calibrate(iters = 20):
    leftMotor = stepperMotor([7,11,13,15])
    rightMotor = stepperMotor([31,33,35,37])
    step = 512
    for i in range(iters):
        leftMotor.rotate(step)
        rightMotor.rotate(step)
        leftMotor.rotate(-step)
        rightMotor.rotate(-step)
