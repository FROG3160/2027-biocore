# FROG 3160 Developer Guide: Codespaces & RobotPy Simulation

Welcome to the **FROG 3160 (2027-biocore)** development environment! This project is configured with **GitHub Codespaces** and **VS Code Dev Containers** so team members and students can develop, run, test, and simulate robot code directly in the cloud without needing to manually configure Python, drivers, or C++ dependencies locally.

---

## 🛠️ Option 1: Developing in GitHub Codespaces (Recommended for Students)

### 1. Launching the Codespace
1. Navigate to the `2027-biocore` repository on GitHub.
2. Click the green **Code** button at the top right.
3. Select the **Codespaces** tab.
4. Click **Create codespace on main** (or choose an existing codespace).
5. Wait 1–2 minutes while the container builds. The pre-installation script automatically installs:
   - Python 3.12
   - RobotPy & WPILib suite
   - Vendor libraries: CTRE Phoenix 6, PhotonLib, PathPlannerLib, and FROGlib
   - OpenGL / Mesa graphics rendering libraries
   - All recommended VS Code extensions and formatters

---

### 2. Opening the Robot Simulation GUI (noVNC Desktop)

Since GitHub Codespaces runs on a remote cloud server, GUI applications like the WPILib Simulation Window are rendered onto a lightweight virtual desktop (via **noVNC**).

1. In VS Code inside your Codespace, open the **Ports** tab at the bottom panel (next to Terminal / Output).
2. Look for port **`6080` (Robot Simulator Desktop)**.
3. Click the **Open in Browser** icon (the small globe or URL link) next to port `6080`.
4. A new browser tab will open showing the remote desktop viewer. Leave this tab open while developing.

---

### 3. Running the Simulation

#### Using the Terminal:
1. Open the terminal inside VS Code:
   ```bash
   cd roborio
   python robot.py sim
   ```
2. Switch to your **noVNC browser tab (port 6080)**.
3. You will see the **WPILib Simulation GUI (Glass/SimGUI)** window appear on the desktop with:
   - Robot State controls (Autonomous, Teleop, Disabled, Test)
   - Joysticks and System Controllers
   - NetworkTables, SmartDashboard values, and Mechanism 2d visualizations.

#### Using VS Code Tasks:
- Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac) → Type `Tasks: Run Task` → Select **`RobotPy Sim`**.
- Or click the **$(play) Run Simulator** button in the VS Code status bar (bottom right).

#### Using the VS Code Debugger:
1. Open the **Run and Debug** panel (`Ctrl + Shift + D`).
2. Select **`Robot Sim`** from the dropdown at the top.
3. Press `F5` to start debugging with breakpoints, variable inspection, and step-through execution.

---

### 4. Running Unit Tests

Run robot automated tests from the terminal:
```bash
cd roborio
python robot.py test
```
Or run the debugger with the **`Robot Test`** configuration.

---

## 📦 Managing Dependencies with `pyproject.toml`

All RobotPy and vendor dependencies are pinned in [`roborio/pyproject.toml`](roborio/pyproject.toml).

To add or update a vendor library:
1. Edit the `requires` array or `components` list in [`roborio/pyproject.toml`](roborio/pyproject.toml).
2. Run sync from the `roborio` folder:
   ```bash
   python -m robotpy sync
   ```

---

## ⚡ Option 2: Local Development (VS Code Dev Containers / Local Python)

### Using Local Dev Containers (Docker Desktop)
If you have Docker installed on your local computer:
1. Clone the repository locally.
2. Open the folder in VS Code.
3. Click **Reopen in Container** when prompted (or open the Command Palette and select `Dev Containers: Reopen in Container`).

### Using Native Local Python
1. Ensure Python 3.12 is installed on your computer.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Linux/macOS
   # .venv\Scripts\activate    # On Windows
   ```
3. Install dependencies:
   ```bash
   cd roborio
   pip install "robotpy[all,sim]"
   python -m robotpy sync
   ```

---

## 🚀 Deploying to the RoboRIO (Competition & Pit Use)

Deploying code to the physical robot requires a direct network connection (Ethernet, USB-B cable, or Robot Radio Wi-Fi) to the RoboRIO:

1. Connect your laptop to the robot radio Wi-Fi (`3160_...`) or USB cable.
2. From your local environment terminal:
   ```bash
   cd roborio
   python -m robotpy deploy
   ```
3. Enter team number `3160` if prompted.
