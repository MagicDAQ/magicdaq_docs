# Use the USB cable to plug MagicDAQ into your computer

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Connect to the MagicDAQ
daq_one.open_daq_device()

# Do use full things with the DAQ
# For example, you can read a digital pin's state
print ('This is Digital Pin P0.0 State: '+str(daq_one.read_digital_input(0)))

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()
