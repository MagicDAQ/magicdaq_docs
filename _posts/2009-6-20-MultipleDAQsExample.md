---
category: Getting Started
title: 'Multiple DAQs Example'
type: 'System'
url_path: 'CODE EXAMPLE'

layout: default
---

Example showing how to:

* Find serial numbers of all DAQs connected to the system
* Connect to a specific DAQ using it's serial number

It is possible to use multiple DAQs at the same time.

### Example Code

```python

# Connect 1 or multiple MagicDAQs to your system using the USB cables.
# Feel free to use a USB hub to connect multiple DAQs to your computer.

# Import the standard time module
import time

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Get the serial numbers of all DAQs that are connected to your computer.
daqs_serial_number_list = daq_one.list_all_daqs()
print('List of DAQ Serial Numbers: '+str(daqs_serial_number_list))
print('Thre are '+str(len(daqs_serial_number_list))+' DAQs in total connected to your system.')

# If there is at least 1 DAQ, connect to it and read its serial number
if len(daqs_serial_number_list) >= 1:
    print('Attempting to connect to DAQ serial number: '+str(daqs_serial_number_list[0]))
    daq_one.open_daq_device(daq_serial_number = daqs_serial_number_list[0])
    
    # You can now do useful things with daq_one
    # For example, you can set digital I/O pin P0.0 to HIGH
    print('Setting Pin P0.0 HIGH on daq_one')
    daq_one.set_digital_ouput(0,1)
    
    # We will be sleeping to allow time to measure the P0.0 with a multimeter
    # This flag indicates if the sleep period has been performed
    sleep_has_hapened = False
    
    # Is there a 2nd DAQ connected to the System?
    # If so, you can simultaneously connect to it and do stuff.
    if len(daqs_serial_number_list) >= 2:
        print('Attempting to connect to DAQ serial number: '+str(daqs_serial_number_list[1]))
        
        # You need to create another MagicDAQDevice object
        daq_two = MagicDAQDevice()
        # Connect to the 2nd DAQ
        daq_two.open_daq_device(daq_serial_number = daqs_serial_number_list[1])
        
        # You can now do useful things with daq_two
        # For example, you can set digital I/O pin P0.0 to LOW
        print('Setting Pin P0.0 LOW on daq_two')
        daq_two.set_digital_ouput(0,0)
        
        print ('Sleeping for 5 sec. to allow time to measure P0.0 pin with multimeter.')
        time.sleep(5)
        # Set the sleep_has_hapended flag to True so the sleep period is not repeated
        sleep_has_hapened = True
        
        # We are done with daq_two so we can close it
        print('Closing daq_two')
        # Close daq_two
        daq_two.close_daq_device()
    
    # If the sleep period has not already occurred, do it now
    if not sleep_has_hapened:
        print ('Sleeping for 5 sec. to allow time to measure P0.0 pin with multimeter.')
        time.sleep(5)
    
    # We are done with daq_two so we can close it
    print('Closing daq_one')
    # Close daq_one
    daq_one.close_daq_device()

print ('Multiple DAQs Example Script COMPLETED.')

```