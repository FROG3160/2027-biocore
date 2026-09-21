import commands2
import wpilib
from wpilib import SendableChooser, SmartDashboard


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot
    (including subsystems, commands, and trigger mappings) should be declared here.
    """

    def __init__(self) -> None:
        # Autonomous routine chooser
        self.auto_chooser: SendableChooser = SendableChooser()
        self.auto_chooser.setDefaultOption("None", None)
        SmartDashboard.putData("Auto Mode", self.auto_chooser)

        # Configure the button bindings
        self.configureButtonBindings()

    def configureButtonBindings(self) -> None:
        """
        Use this method to define your trigger->command mappings.
        """
        pass

    def getAutonomousCommand(self) -> commands2.Command | None:
        return self.auto_chooser.getSelected()
