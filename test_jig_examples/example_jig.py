#################################
#*** Example Test Jig Script  ***
#################################

# This is an example test jig script
# It is for demonstration purposes, inputs are simulated (there is no physical PCB being tested)

#*** Required Test Hardware ***

# Binho
# Digital communications would be performed with Bhinho Nova:
# https://binho.io/
# https://support.binho.io/python-libraries

# MagicDAQ
# Analog control and measurement would be performed with MagicDAQ:
# Both the USB DAQ and M&A board would be used
# https://www.magicdaq.com/
# https://magicdaq.github.io/magicdaq_docs/

#*** Imports ***

# IMPORTANT!
# Use this import command to access a real MagicDAQ USB DAQ
#from magicdaq.api_class import MagicDAQDevice

# Simulated MagicDAQ (you do not need a physical MagicDAQ connected to your computer to run this script)
from simulated_daq import MagicDAQDevice

import time
from datetime import datetime

# Need to import binho library here

#################################
#*** Functions  ***
#################################

def print_and_log(text):
    print(text)
    logfile.write(text+'\n')
    return

#################################
#*** Main Script  ***
#################################

#################################
#*** Print Test Header        ***
#################################

print('--- Test Jig ---')
user_input = input('Is the board mounted in the test fixture? Press ENTER to continue.')
print('')

#################################
#*** Create Log File  ***
#################################

# For each PCB tested, you need to save a log file with the results
# This can be a simple .txt file
# The file name should be something unique like: 'PCB under test serial number + current date/time'

# Get PCB under test serial number
# Use binho
# When communicating with an actual board, you will probably want to use some exception logic here (try except)
# to fail gracefully if a board is not physically connected to the test system
simulated_serial = '6e13b88d'

# Get current data and time
current_date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

# Assemble file name
log_file_name = 'serial_'+simulated_serial+'_time_'+current_date+'.txt'

# Create and open the file
# w+ : if the file does not exist, create it. If it already exists, overwrite it
logfile = open(log_file_name, 'w+')

# Write in a file header
logfile.write('--- Test Jig Log File ---'+'\n')
logfile.write('\n')
logfile.write('Board Serial #: '+simulated_serial+'\n')
logfile.write('Date / Time: '+current_date+'\n')

print('Board Serial Number: '+simulated_serial)
print('Current Date / Time: '+current_date)

#################################
#*** Test Voltage Rails       ***
#################################
print_and_log('')
print_and_log('--- Testing Voltage Rails ---')
print_and_log('')

#*** Measure Main Voltage Rail ***

# Create MagicDAQDevice and connect to USB DAQ
daq_one = MagicDAQDevice()
daq_one.open_daq_device()

# Should be 3.3V +/- .2 V
# Read voltage from main voltage rail (AI0 pin being used)
main_rail_voltage = daq_one.read_analog_input(0)
print_and_log('Main Rail Voltage (should be 3.3V): '+str(main_rail_voltage))

if abs(3.3 - main_rail_voltage) > 0.2:
    print_and_log('FAIL: Voltage is off by > 0.2 V')
else:
    print_and_log('PASS')
print_and_log('')

#*** Measure USB Voltage Rail ***

# Should be 5V +/- .5V
usb_voltage = daq_one.read_analog_input(1)
print_and_log('USB Voltage (should be 5.0V): '+str(usb_voltage))

if abs(5 - usb_voltage) > 0.5:
    print_and_log('FAIL: Voltage is off by > 0.5 V')
else:
    print_and_log('PASS')
print_and_log('')

#################################
#*** Main Board Current Test  ***
#################################

print_and_log('--- Testing Current Draw ---')
print_and_log('')

#*** Standard Board Current Draw ***

# Use binho nova to place the board under test in what ever the 'standard' operating condition is
# You will need to wait for little bit to allow the current draw to settle to 'steady state'
# time.sleep(0.1)

# board should draw roughly 1 Amp (+/- 150mA)
# A2 channel on M&A board is connected to AI5 on the USB DAQ
# Page 6
# https://www.magicdaq.com/mdaq350datasheet/

pin_5_voltage = daq_one.read_analog_input(5)
# See the M&A Board data sheet for this calculation
board_current_draw_amps = pin_5_voltage / (.01 * 200)
print_and_log('Board Current Draw - Standard Operation (Should be 1Amp +/- .2A): '+str(board_current_draw_amps))
if abs(1 - board_current_draw_amps) > 0.2:
    print_and_log('FAIL: Current draw is off by > 0.2 A')
else:
    print_and_log('PASS')
print_and_log('')

#*** Turn On Load, Measure Current ***

# Assume that the board powers a resistive heating load
# Let's assume that the load draws 0.5A

# Use a relay on the MA board to connect a resistive dummy load
# Close Relay 1 on the M&A Board
# Page 6
# https://www.magicdaq.com/mdaq350datasheet/

daq_one.set_digital_output(7,1)

# Wait for the current draw to reach steady state
time.sleep(.1)

# Measure the board current while load is on
pin_5_voltage = daq_one.read_analog_input(5)
# See the M&A Board data sheet for this calculation
board_current_draw_amps = pin_5_voltage / (.01 * 200)
print_and_log('Board Current Draw - Load Connected (Should be 1.5Amp +/- .2A): '+str(board_current_draw_amps))
if abs(1 - board_current_draw_amps) > 0.2:
    print_and_log('FAIL: Current draw is off by > 0.2 A')
else:
    print_and_log('PASS')
print_and_log('')

# Turn off load
daq_one.set_digital_output(7,0)

#*** Measure Board Sleep State Current ***

# Use binho to place the board in sleep mode

# Wait for steady state current
time.sleep(.1)

pin_4_voltage = daq_one.read_analog_input(4)
calculated_current_amps = pin_4_voltage / (332 * 97.863)
ua_current = round((calculated_current_amps / .000001), 3)
print_and_log('Board Current Draw - Sleep Mode (Should be 150uA +/- 20uA): '+str(ua_current))

if abs(150 - ua_current) > 20:
    print_and_log('FAIL: Current draw is off by > 20 uA')
else:
    print_and_log('PASS')
print_and_log('')

#*** Testing is Now Complete ***
print_and_log('--- Testing Complete ---')

# Don't forget to close the log file
logfile.close()





