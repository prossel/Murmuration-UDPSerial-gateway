#!/bin/bash
 
# This bash script starts the python script
# 
# Add execute permissions to the script with the following command in the terminal:
#
#   chmod +x start.command
# 
# Then double click the script to start the server and launch chrome in kiosk mode
# To stop the server and chrome, close the chrome window
#
# Note: This script is for Mac OS X. It may need to be modified for other operating systems
#
# Note: The script assumes that python3 is installed. If python3 is not installed, 
# it can be installed from https://www.python.org/downloads/
# 
# Written by Pierre Rossel on 2024-06-06
 
 
# change to the directory where the script is located
cd "$(dirname "$0")"

# Run the WebSocket-Serial-Gateway in the background
echo "Starting UDPSerial gateway ..."
python3 Murmuration-UDPSerial.py
 
echo done