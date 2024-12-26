#!/bin/bash

# First instance of Xvfb for the first script
export DISPLAY=:99
Xvfb :99 -screen 0 1920x1080x24 &  # Start the first Xvfb on display :99
fluxbox &                          # Start a lightweight window manager for first script
/usr/bin/python3 /home/pi/selenium_scripts/my_selenium_script.py &  # Run the first instance in background

# Second instance of Xvfb for the second script
export DISPLAY=:100
Xvfb :100 -screen 0 1920x1080x24 &  # Start the second Xvfb on display :100
fluxbox &                           # Start a lightweight window manager for second script
/usr/bin/python3 /home/pi/selenium_scripts/my_selenium_script.py &  # Run the second instance in background
