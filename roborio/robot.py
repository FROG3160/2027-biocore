#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
from wpilib import DriverStation
from robotcontainer import RobotContainer


class FROGBot(commands2.TimedCommandRobot):
    """Main robot class for 2027 BioCore"""

    def robotInit(self) -> None:
        """Initialize all robot components and logging"""
        wpilib.DataLogManager.start()
        DriverStation.startDataLog(wpilib.DataLogManager.getLog(), True)

        self.container = RobotContainer()
        self.autonomous_command: commands2.Command | None = None

    def robotPeriodic(self) -> None:
        """Runs periodic tasks across all modes"""
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        self.autonomous_command = self.container.getAutonomousCommand()
        if self.autonomous_command:
            self.autonomous_command.schedule()

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        if self.autonomous_command:
            self.autonomous_command.cancel()

    def teleopPeriodic(self) -> None:
        pass

    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()

    def testPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(FROGBot)
