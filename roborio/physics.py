#
# See the notes for the physics support in the robotpy-wpilib package
#

import wpilib.simulation
from pyfrc.physics.core import PhysicsInterface


class PhysicsEngine:
    """
    Simulation physics engine for 2027 BioCore robot.
    """

    def __init__(self, physics_controller: PhysicsInterface, robot: "wpilib.TimedRobot"):
        self.physics_controller = physics_controller

    def update_sim(self, now: float, tm_diff: float) -> None:
        """
        Called when the simulation parameters for the program need to be updated.

        :param now: The current time as a float
        :param tm_diff: The amount of time that has passed since the last
                        time that this function was called
        """
        pass
