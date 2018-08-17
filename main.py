import pygame
from drivetrain import drivetrain
from joystick import joystick, joystickState, joystickEventType
from time import sleep

# main robot application class. Manages the drive train and takes input from the sensors and joystick
#
class App:
    def __init__(self):
        pygame.init()
        self.driveTrain = drivetrain()
        self.interval = .1 # run main loop every .1 seconds
        self.joystick = joystick()
        # set the joystick callbacks
        joystick.addButtonEventHandler(self.joystick,self.buttonCallback)
        joystick.addJoystickEventHandler(self.joystick,self.joystickMoveCallback)

    def main(self):
        # main loop
        while True:
            self.joystick.checkInput() # function will call us back if something happened
            sleep(self.interval)


    def buttonCallback(self, state, buttonNumber) :
        print str(buttonNumber) + ' changed to ' + str(state)
        if buttonNumber == 7:
            #cleanup the drive train and exit.
            drivetrain.shutdown(self.driveTrain)
            exit()

    def joystickMoveCallback(self,direction):
        print 'joystick moved to ' + str(direction)
        if direction == joystickState.center:
            drivetrain.stop(self.driveTrain)
        elif direction == joystickState.up:
            drivetrain.forward(self.driveTrain)
        elif direction == joystickState.down:
            drivetrain.reverse(self.driveTrain)
        elif direction == joystickState.left:
            drivetrain.leftSpin(self.driveTrain)
        elif direction == joystickState.right:
            drivetrain.rightSpin(self.driveTrain)
        else:
            print 'unknown state'

app=App()
app.main()