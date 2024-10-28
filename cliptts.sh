#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(dirname "$0")"

# Activate the virtual environment
source "$SCRIPT_DIR/venv/bin/activate"
python3 "$SCRIPT_DIR/clipTTS.py"

# Deactivate the venv
deactivate