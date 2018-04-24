import wpilib

class Robot:
    '''
    The robot class
    '''
    def __init__(self):
        '''
        Do nothing for the constructor for now
        '''
        pass

    def robotInit(self):
        '''
        This will end up being used as the robot's
        constructor. This is the case for legacy reasons.
        '''
        pass

    def autonomousInit(self):
        '''
        This is what is called when the robot switches from
        any state to its autonomous state.
        '''
        pass

    def autonomousPeriodic(self):
        '''
        This function is called periodically during
        autonomous.
        '''
        pass

    def teleopInit(self):
        '''
        This function is called when to robot switches from
        any state (in practice only from the disabled state)
        to the teleop state.
        '''
        pass

    def teleopPeriodic(self):
        '''
        This function is called periodically during teleop.
        '''
        pass

    def disabledInit(self):
        '''
        This function is called 
        '''
        pass

    def disabledPeriodic(self):
        '''
        '''
        pass

if __name__ == '__main__':
    # Using WPILib we can run our robot with the following
    # command
    wpilib.run(Robot)