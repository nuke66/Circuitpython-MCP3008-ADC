"""
This example program connects a MCP3008 analog to digital converter using CircuitPython 
on an Adafruit ItsyBitsy M4 Express. 

MCP3008 Pin   SPI   ItsybitsyM0
------------+-----+----------------
13 (Clk)      SCK    SCK (SCK)
12 (Dout)     MISO   MI  (MISO)
11 (Din)      MOSI   MO  (MOSI)
10 (Cs)       CS     D5  (Any free digital pin)

"""
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5) # chip select
mcp = MCP.MCP3008(spi, cs) 

p7 = AnalogIn(mcp, MCP.P7) # channel 7

while True:
    print('Value:   {:05}'.format(p7.value))
    print('Voltage: {:1.2}V'.format(p7.voltage))
    time.sleep(0.1)
