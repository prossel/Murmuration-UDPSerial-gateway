# Murmuration UDP Serial gateway

![Waveshare Modbus RTU Relay 16 CH and USB to RS458 dongle](<Media/Waveshare Modbus RTU Relay 16 CH and USB to RS458 dongle.jpg>)

Gateway between an URP port and a serial port for the Murmuration project (HEAD - Genève, Media Design MD1 2024).

Receives UDP data to switch relays on a Waveshare Modbus RTU Relay 16CH board.

The data is forwared to the board using a Waveshare USB to RS485 adapter.

Information on the Modbus RTU Relay 16CH and the Modbus RTU protocol:

[https://www.waveshare.com/wiki/Modbus_RTU_Relay_16CH](https://www.waveshare.com/wiki/Modbus_RTU_Relay_16CH)

## Usage

* Connect the serial adapter.
* Run the gateway:

```shell 
python3 Murmuration-UDPSerial.py
```

* Send binary data to the listening UDP port of the gateway (8080 by default).
* The data will be forwarded by the gateway to the serial port
* An immediate reply (if any) will be forwarded to the caller's IP address on the replying port (8081 by default)

## Example

Unity demo to control the relays

[https://github.com/prossel/Unity-Demo-RS485-Relays](https://github.com/prossel/Unity-Demo-RS485-Relays)

