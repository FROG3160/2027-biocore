# FROG 3160 - 2027 BioCore

This repository contains the RobotPy-based robot code for Team 3160 (FROG Robotics) for the 2027 FRC season. Built on WPILib's **Commands2** framework, **CTRE Phoenix 6**, and **FROGlib**, this project supports both real-hardware robot deployments and full GUI physics simulations.

---

## 🚀 Quick Start with GitHub Codespaces

You can develop, test, and run robot simulation directly in your browser with zero local installation:

1. Click **Code** → **Codespaces** → **Create codespace on main**.
2. When the Codespace starts up, all extensions, Python 3.12, RobotPy, and system OpenGL libraries are configured automatically.
3. Open the forwarded **Robot Simulator Desktop (Port 6080)** to view the WPILib Simulation GUI in your browser.
4. Run simulation:
   ```bash
   cd roborio
   python robot.py sim
   ```

For detailed instructions, simulation tips, and local setup, see [DEVELOPER.md](DEVELOPER.md).

---

## 🏗️ Architecture & Tech Stack

- **Language & Framework**: [RobotPy](https://robotpy.readthedocs.io/) (Python 3.12 + WPILib Commands2)
- **Hardware Abstraction**: [FROGlib](https://github.com/FROG3160/FROGlib)
- **Motor Control & Odometry**: CTRE Phoenix 6
- **Vision**: PhotonLib / PhotonVision (AprilTag & Object Detection)
- **Autonomous & Path Following**: PathPlannerLib
- **Telemetry & Logging**: WPILib DataLog (`.wpilog`) + CTRE SignalLogger (`.hoot`) + AdvantageScope

---

## 📁 Repository Structure

```text
2027-biocore/
├── .devcontainer/             # GitHub Codespaces & Dev Container configuration
│   ├── devcontainer.json      # Devcontainer settings, extensions, and port forwarding
│   └── post-create.sh         # Automated environment installation script
├── .vscode/                   # Recommended VS Code settings, tasks, and launch configs
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── roborio/                   # Main robot code directory
│   ├── commands/              # Commands and command sequences
│   ├── subsystems/            # Robot subsystems (Chassis, Manipulators, etc.)
│   ├── tests/                 # Unit tests & physics verification
│   ├── constants.py           # CAN IDs, controller ports, robot dimensions
│   ├── physics.py             # RobotPy physics engine simulation hooks
│   ├── pyproject.toml         # RobotPy dependencies and version pinning
│   ├── robot.py               # Main robot entrypoint
│   └── robotcontainer.py      # Subsystem instantiation and button mappings
├── DEVELOPER.md               # Student & developer guide for Codespaces / Simulation
└── README.md                  # Project overview
```
