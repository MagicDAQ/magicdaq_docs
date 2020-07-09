# Use the USB cable to plug MagicDAQ into your computer

# Import standard time module
import time

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Connect to the MagicDAQ
daq_one.open_daq_device()

# Start the Pulse Counter
# Pulses will be counted on the falling edge
daq_one.enable_pulse_counter()

print('Pausing for 15 sec to allow time to read pulses.')
print('Briefly join together pins CTRO and DGND repeatedly to simulate pulses.')
time.sleep(15)

# Read number of pulses
print('Number of pulses counted: '+str(daq_one.read_pulse_counter()))

print('Now clearing the pulse counter')
daq_one.clear_pulse_counter()
print('Pulse count after clearing: '+str(daq_one.read_pulse_counter()))

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()
