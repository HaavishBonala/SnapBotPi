# SnapBotPi
This repository documents the setup and execution of a Selenium script on a Raspberry Pi without a connected display, using Xvfb (X virtual framebuffer) to increase an account's snapchat score by automatically sending snaps of a blank screen to single / multiple bot account(s). The setup ensures the script runs automatically at startup and can handle multiple instances simultaneously.

---

## **Prerequisites**

Ensure the following are installed on your Raspberry Pi:
- Python 3
- Pip (Python package manager)
- Selenium Python library
- Chromium browser

### Install Required Dependencies:
```bash
sudo apt update
sudo apt install -y python3 python3-pip chromium-browser xvfb fluxbox
pip3 install selenium
```

---

## **Setup**

### **1. Install and Configure Xvfb**
Xvfb is a virtual display server that allows GUI applications to run without a physical monitor.

```bash
sudo apt install -y xvfb
```

### **2. Create Selenium Wrapper Script**

Create a script (`selenium_wrapper.sh`) to manage and run multiple Selenium instances with Xvfb:

```bash
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
```

Make the script executable:
```bash
chmod +x /home/pi/selenium_scripts/selenium_wrapper.sh
```

### **3. Set Up Auto-Startup**
Use `cron` to ensure the script runs at boot.

Edit the crontab:
```bash
crontab -e
```

Add the following line:
```bash
@reboot /home/pi/selenium_scripts/selenium_wrapper.sh >> /home/pi/selenium_scripts/log.txt 2>&1
```

This ensures the wrapper script starts automatically on reboot and logs output to `log.txt`.

---
## **Customizing the Bot Accounts**

On **line 85** of the Python script (`my_selenium_script.py`), you need to add the names of your bot accounts that have been friended both ways. This ensures the script correctly selects and interacts with these accounts.

Example:
```python
bot_names = [
    'Bot1', 'Bot2', 'Bot3', 'Bot4', 'Bot5'
]
```

Replace these names with your bot account names as needed.

---

## **Testing and Monitoring**

### **Reboot and Test**
Reboot the Raspberry Pi to confirm the scripts start automatically:
```bash
sudo reboot
```

### **Verify Logs**
Check the log file to ensure both instances of the Selenium script are running:
```bash
cat /home/pi/selenium_scripts/log.txt
```

### **Check Running Processes**
Use the following command to verify that the Selenium scripts are running:
```bash
ps aux | grep selenium
```

---

## **Run Manually**
If needed, you can manually run the wrapper script to start both instances:
```bash
/home/pi/selenium_scripts/selenium_wrapper.sh
```

---

## **Troubleshooting**

- **Error: Chromium not found**  
  Ensure Chromium is installed:
  ```bash
  sudo apt install -y chromium-browser
  ```

- **Session Not Created Error:**  
  Verify your `chromedriver` matches the installed Chromium version.

- **Log File Empty:**  
  Check the script for errors by running it manually and reviewing the output.

---

## **License**
This project is open-source and licensed under the MIT License.
