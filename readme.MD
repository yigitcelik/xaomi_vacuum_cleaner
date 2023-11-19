# Xiaomi Vacuum Cleaner Robot Auto-Restart Script

## Overview

This Python script is designed to automatically restart Xiaomi vacuum cleaner robots when they encounter failures and stop cleaning, typically due to irrelevant error codes. It accomplishes this by logging into your Xiaomi account, extracting the necessary device information, and then continuously monitoring and restarting the robot until the cleaning process is completed.

## Prerequisites

To use this script, you'll need the following:

- A Xiaomi account with the robot vacuum cleaner added.
- Python 3.x installed on your system.
- The required Python libraries installed, which can be found in the requirements.txt. You can install these using `pip install -r requirements.txt`.

## Usage

1. Clone or download this repository to your local machine.
2. Open the `auto_restart_xiaomi_vacuum.py` file in a text editor.
3. Configure the following variables at the beginning of the script:
   - `username`: Your Xiaomi account username.
   - `password`: Your Xiaomi account password.
   - `floor_area`: The minimum floor area that the vacuum cleaner should clean before stopping (in square meters).
4. Save your changes.
5. Execute the script by running the following command in your terminal:

   ```bash
   python auto_restart_xiaomi_vacuum.py

## virtual env
```bash
#Create a new virtual environment
python3 -m venv venv
#activate
. venv/bin/activate
#install
pip install -r requirements.txt
