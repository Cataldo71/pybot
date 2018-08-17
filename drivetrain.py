import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

Motor1E = 16
Motor1A = 18
Motor1B = 22

Motor2E = 11
Motor2A = 15
Motor2B = 13

# 2 motor drive train class. pins above should be set to the pins connected to the motors on the raspi
#
class drivetrain:
    def __init__(self):
        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)
        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)

    def shutdown(self):
        GPIO.cleanup()

    def stop(self):
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2E, GPIO.LOW)

    def forward(self):
        # left side
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        #right side
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

    def reverse(self):
        # left side
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)
        #right side
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)

    def leftSpin(self):
        # left side reverse
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        #right side forward
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)

    def rightSpin(self):
        # left side forward
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)
        #right side reverse
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)