# Connect one or more MagicDAQs to your system using the USB cables.
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
print('There are '+str(len(daqs_serial_number_list))+' DAQs in total connected to your computer.')
print('')


# If there is at least 1 DAQ, connect to it and read its serial number
if len(daqs_serial_number_list) >= 1:

    # NOTE:
    # For systems that always use the same DAQ units, you can hard code the serial numbers
    # For example:
    # daq_one.open_daq_device(daq_serial_number = '931cd19e')

    daq_one.open_daq_device(daq_serial_num = daqs_serial_number_list[0])
    # Read the DAQ's serial number
    print('daq_one serial number: ', daq_one.get_serial_number())


    # You can now do useful things with daq_one
    # For example, you can set digital I/O pin P0.0 to HIGH
    print('Setting Pin P0.0 HIGH on daq_one')
    daq_one.set_digital_output(0,1)
    

# Is there a 2nd DAQ connected to the System?
# If so, you can simultaneously connect to it and do stuff.
if len(daqs_serial_number_list) >= 2:

    # You need to create another MagicDAQDevice object
    daq_two = MagicDAQDevice()
    # Connect to the 2nd DAQ
    daq_two.open_daq_device(daq_serial_num = daqs_serial_number_list[1])
    # Read the DAQ's serial number
    print('')
    print('daq_two serial number: ', daq_two.get_serial_number())


    # You can now do useful things with daq_two
    # For example, you can set digital I/O pin P0.0 to LOW
    print('Setting Pin P0.0 LOW on daq_two')
    daq_two.set_digital_output(0,0)



# Sleeping for 30 sec so you can measure the DAQ digital output pins with a multimeter
print('')
print('Sleeping for 30 sec so you can measure the digital output pins with a multimeter')
time.sleep(30)

# We need to close the DAQs
if len(daqs_serial_number_list) >= 1:
    daq_one.close_daq_device()
if len(daqs_serial_number_list) >= 2:
    daq_two.close_daq_device()


