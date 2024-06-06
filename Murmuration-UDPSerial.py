# UDP Serial gateway for Murmuration project.  
# Receive UDP data to switch relays on a waveshare Modbus RTU Relay 16CH board
# The data is forwared to the board using a WaveShare USB to RS485 adapter

# Usage: python3 Murmuration-UDPSerial.py

# Pierre Rossel 2024-06-06

import socket
import time
import serial
from serial.tools import list_ports
import sys

# listening port number
PORT = 8080

# echo sending port number
PORT_ECHO = 8081

# Get the list of serial ports and open the last one
ports = serial.tools.list_ports.comports()
port = ports[-1].device
print("Open the serial port: " + port)
ser = serial.Serial(port, 9600, timeout=0.1)

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
sock.bind(('', PORT))

print(f"Listening on port {PORT}")
print(f"Echoing on port {PORT_ECHO}")

while True:
    # Receive the message
    try:
        data, addr = sock.recvfrom(1024)
    except KeyboardInterrupt:
        print()
        break
    
    # Print the received message
    try:
        print(f"Received message from {addr} : {data.decode()}")
    except UnicodeDecodeError:
        print(f"Received binary data message from {addr} : {data.hex() }")

    # if empty data message, reply with an empty message to let sender know our IP address
    if data == b'':
        # Send the message back to the sender
        sock.sendto(data, (addr[0], addr[1]))
    else:
        # Send the command to switch the relay
        ser.write(data)
        
        response = ser.read(100)
        
        print("Response: ", end="")
        print(response.hex())
        
        # send the response back to the sender
        sock.sendto(response, (addr[0], addr[1]))

    # Wait for 1 second before receiving the next message
    time.sleep(0.1)


print("Closing the serial port")
ser.close()

print("Closing the socket")
sock.close()
