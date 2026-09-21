#!/usr/bin/env bash
set -e

echo "=== [1/3] Installing OpenGL and GUI rendering dependencies ==="
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    mesa-utils \
    libasound2 \
    libx11-xcb1 \
    libxcb-xinerama0 \
    libxkbcommon-x11-0 \
    git

echo "=== [2/3] Upgrading Python package tooling ==="
python -m pip install --upgrade pip setuptools wheel

echo "=== [3/3] Installing RobotPy and project dependencies ==="
if [ -d "roborio" ]; then
    cd roborio
    pip install "robotpy[all,sim]"
    python -m robotpy sync || true
    cd ..
else
    pip install "robotpy[all,sim]"
fi

echo "=== Codespace environment ready for RobotPy & Simulation! ==="
