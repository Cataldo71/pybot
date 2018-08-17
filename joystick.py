import time
import pygame
from enum import Enum

# classes and enums to wrap the pygame joystick class and generate callback events for 
# joystick functions.
# NOTE: class assumes that pygame has already been initialized

#
# usage:
# from joystick import joystick, joystickState, joystickEventType
# pygame.init()
# joystick = joystick()
# 
# joystick.addButtonEventHandler(self.joystick,self.buttonCallback)
# joystick.addJoystickEventHandler(self.joystick,self.joystickMoveCallback)
#
#  joystick.checkInput() # function will call appropriate callback if event happened. This should be done in the apps main loop

class joystickState(Enum):
    center = 1
    up = 2
    down = 3
    left = 4
    right = 5

class joystickEventType(Enum):
    joystick = 1
    buttonDown = 2
    buttonUp = 3

class joystickEvent:
    def __init__(self, type, jstickpos, buttonNum):
        self.type = type
        self.joystickPosition = jstickpos
        self.buttonNumber = buttonNum

class joystick:
    def __init__(self):
        self.state = joystickState.center
        self.activeEvent = None
        self.hadEvent = False
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        # Array of button/joystick handlers. These are callback functions that will be called when 
        # a button is pressed or released or joystick is moved
        self.buttonHandlers = []
        self.joystickHandlers = []

    def addButtonEventHandler(self, buttonHandler):
        self.buttonHandlers.append(buttonHandler)

    def addJoystickEventHandler(self, joystickHandler):
        self.joystickHandlers.append(joystickHandler)

    def checkInput(self):
        #send the handler callback into the handler
        # the callback will set the event state / type if there is an event
        self.PygameHandler(pygame.event.get())
        if self.hadEvent == True:
            self.hadEvent = False
            if self.activeEvent.type == joystickEventType.joystick:
                #joystick event
                for f in self.joystickHandlers:
                    f(self.activeEvent.joystickPosition)
            else:
                # Button event - call all button handlers with the type and button number
                print 'call button event handlers'
                for f in self.buttonHandlers:
                    f(self.activeEvent.type, self.activeEvent.buttonNumber)


    def PygameHandler(self,events):
         # Handle each event individually
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                # A joystick has been moved, read axis positions (-1 to +1)
                
                upDown = self.joystick.get_axis(1)
                leftRight = self.joystick.get_axis(0)
                state = None
                # Determine Up / Down values
                if upDown < -0.1:
                    state = joystickState.up
                elif upDown > 0.1:
                    state = joystickState.down
                # Determine Left / Right values
                elif leftRight < -0.1:
                    state = joystickState.left
                elif leftRight > 0.1:
                    state = joystickState.right
                else:
                    state = joystickState.center
                #joystick state has changed state
                if state != self.state:
                    # set the active state and send the event
                    self.hadEvent = True
                    self.state = state
                    self.activeEvent = joystickEvent(joystickEventType.joystick,state,0)
                    #print state
            elif event.type == pygame.JOYBUTTONDOWN:
                self.hadEvent = True
                self.activeEvent = joystickEvent(joystickEventType.buttonDown, self.state, event.button)
                #print event
            elif event.type == pygame.JOYBUTTONUP:
                self.hadEvent = True
                self.activeEvent = joystickEvent(joystickEventType.buttonUp, self.state, event.button)
                #print event
            else:
                print 'other event'