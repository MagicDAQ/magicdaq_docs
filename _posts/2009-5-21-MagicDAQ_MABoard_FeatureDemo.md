---
category: Demo Scripts
title: 'MagicDAQ / M&A Board Feature Demo'
type: 'System'
url_path: 'CODE EXAMPLE'

layout: default
---

The below script is a guided tour through most of the USB DAQ's features.
If you have an [M&A Board](https://www.magicdaq.com/product/ma-board-full-kit/), you can connect it to the MagicDAQ to test some of its features as well.
* See [page 6 of the M&A Board data sheet](https://www.magicdaq.com/mdaq350datasheet/) for instructions on how to connect the DAQ to the M&A Board.

### Demo Code

[Source File](https://github.com/MagicDAQ/magicdaq_docs/tree/master/example_python_files)

```python

##############################################################
#*** MagicDAQ USB DAQ and M&A Board General Demo Script ***
##############################################################

#*** Websites ***
# MagicDAQ Website:
# https://www.magicdaq.com/
# API Docs Website:
# https://magicdaq.github.io/magicdaq_docs/

#*** Install MagicDAQ ***
# Download the MagicDAQ python package from pypi
# Run this command in a command prompt:
# python -m pip install magicdaq
# Further docs: https://magicdaq.github.io/magicdaq_docs/#/Install_MagicDAQ
# MagicDAQ is only compatible with Python 3 on Windows. It does not work on Linux at the moment. It does not work with Python 2.

#*** Using Auto Code Complete With PyCharm ***
# Using a code editor like Pycharm and want to get auto complete working for the MagicDAQ package?
# Docs: https://magicdaq.github.io/magicdaq_docs/#/PyCharmCodeCompletion

##############################################################
#*** Imports ***
##############################################################

import sys
import time

# Import MagicDAQ
print('*** MagicDAQ Install Check ***')
print('')

try:

    # Import MagicDAQDevice object
    from magicdaq.api_class import MagicDAQDevice

    # Create daq_one object
    daq_one = MagicDAQDevice()
    print('GOOD: MagicDAQ API is installed properly.')

    # Get MagicDAQ Driver Version
    driver_version = daq_one.get_driver_version()

    if driver_version == 1.0:
        print('GOOD: MagicDAQ Driver is installed properly.')
        print('You are ready to use MagicDAQ!')
    else:
        print('ERROR: MagicDAQ Driver version not expected value: '+str(driver_version))
        print('Try installing MagicDAQ using pip again.')
        print('https://magicdaq.github.io/magicdaq_docs/#/Install_MagicDAQ')
        print('Feel free to email MagicDAQ Support at: support@magicdaq.com')

except Exception as exception_text:
    print('Original exception: ')
    print(exception_text)
    print('')
    print('ERROR: Unable to import MagicDAQ API.')
    print('Mostly likely, MagicDAQ has not been properly downloaded and installed using pip.')
    print('Please consult MagicDAQ API Docs: https://magicdaq.github.io/magicdaq_docs/#/Install_MagicDAQ')
    print('Feel free to email MagicDAQ Support at: support@magicdaq.com')
    sys.exit(0)


##############################################################
#*** MagicDAQ USB DAQ MDAQ300 Features Demo ***
##############################################################

# This portion of the script shows off some of the USB DAQ's features
# Hardware docs: https://www.magicdaq.com/product/magic-daq/

print('')
print('*** MagicDAQ USB DAQ Demo ***')
print('Ensure the USB DAQ is plugged into the computer using the USB cable.')
print('The DAQ does not need to be connected to the M&A board.')
print('')
user_input = input('Press any key to continue.')

#*** Open DAQ Device ***

# Remember, the daq_one object has already been created in the above 'Imports' section
# We must open the daq device before performing any hardware feature manipulation
# https://magicdaq.github.io/magicdaq_docs/#/MagicDAQ_Basics
daq_one.open_daq_device()


###############################################################
#*** Analog Output Demo: Constant, Sine, and PWM on AO1 Pin ***
###############################################################

print('')
print('--- Analog Output Demo: Constant, Sine, and PWM Output ---')

# Set constant 3 volt output voltage on AO1 pin
daq_one.set_analog_output(1,3)

print('Using an oscilloscope, place the scope probe on pin AO1 and connect the scope probe GND to one of the USB DAQs AGND pins')
print('You should now observe a constant 3V')
print('')
user_input = input('Press any key to continue.')

# Configure and start 300Hz sine wave with 2V amplitude on AO1 pin
daq_one.configure_analog_output_sine_wave(1,300,amplitude=2)
daq_one.start_analog_output_wave(1)
print('You should now observe a 300Hz sine wave with 2V amplitude.')
print('')
user_input = input('Press any key to continue.')

# Stop previous wave
daq_one.stop_analog_output_wave(1)

# Configure and start PWM wave, 200 Hz, 50% duty cycle, 3.3V amplitude
daq_one.configure_analog_output_pwm_wave(1,200,50,amplitude=3.3)
daq_one.start_analog_output_wave(1)
print('You should now observe a 200Hz PWM wave, 50% duty cycle, with 3.3V amplitude.')
print('')
user_input = input('Press any key to continue.')

# Stop the wave
daq_one.stop_analog_output_wave(1)
print('The wave should now stop. You could set it to GND using set_analog_ouput() if you wanted.')
print('')
user_input = input('Press any key to continue.')


###############################################################
#*** Pulse Counter Pin Demo: PWM waves ***
###############################################################

print('')
print('--- Pulse Counter Pin Demo: PWM Waves ---')

# Configure a 50 KHz frequency, 75% duty cycle, continuous PWM Wave on the counter pin (CTR0)
# Note that unlike the analog output pins, the CTR0 pin always outputs at an amplitude of 3.3v when producing PWM waves
daq_one.configure_counter_pwm(50000,75)
# Start counter wave
daq_one.start_counter_pwm()

print('Place your scope probe on pin CTR0')
print('You should see a 50kHz, 75% duty cycle PWM wave.')
print('')
user_input = input('Press any key to continue.')

# Now stopping the counter PWM wave
daq_one.stop_counter_pwm()
print('The PWM wave will now stop.')
print('')
user_input = input('Press any key to continue.')


###############################################################
#*** Pulse Counter Pin Demo: Pulse Counting ***
###############################################################

print('')
print('--- Pulse Counter Pin Demo: Pulse Counting ---')

print('Use a piece of wire to bridge CTR0 to DGND several times')
print('CTR0 has an internal pull up resistor. You are simulating a pulse pulling the voltage to GND.')
print('You will have 8 sec to simulate some pulses.')
print('')
user_input = input('Press any key when you are ready to start.')

# Start the Pulse Counter
# Pulses will be counted on the falling edge
daq_one.enable_pulse_counter()

# Sleep for 8 sec
time.sleep(8)

# Read number of pulses
print('Number of pulses counted: '+str(daq_one.read_pulse_counter()))
print('You are using a piece of wire, so it is likely bouncing on and off the screw terminal, counting many pulses')

print('')
user_input = input('Stop simulating pulses. Press any key to continue.')
print('')
print('Now clearing the pulse counter')
daq_one.clear_pulse_counter()
print('Pulse count after clearing: '+str(daq_one.read_pulse_counter()))


###############################################################
#*** Digital Pin Demo ***
###############################################################

print('')
print('--- Digital Pin Demo ---')

# Set P0.0 pin LOW
daq_one.set_digital_output(0,0)
print('Place scope probe on pin P0.0, pin should be LOW')
print('')
user_input = input('Press any key to continue.')

# Set P0.0 pin HIGH
daq_one.set_digital_output(0,1)
print('Place scope probe on pin P0.0, pin should be HIGH')
print('')
user_input = input('Press any key to continue.')


###############################################################
#*** Analog Input Pin Demo ***
###############################################################

print('')
print('--- Analog Input Pin Demo ---')

# Single ended voltage measurement
print('Apply voltage to AI0 pin. If you dont have a power supply handy, you can run a wire from the +5V pin to the AI0 pin.')
print('')
user_input = input('Press any key to continue.')
print('Voltage measured at AI0: '+str(daq_one.read_analog_input(0)))
print('If you are using the +5V pin, remember that this voltage is derived from the USB Power supply, so it will be what ever your USB bus ir producing, probably something slightly less than 5V.')

# If you want to perform a differential input measurement
# daq_one.read_diff_analog_input()
# https://magicdaq.github.io/magicdaq_docs/#/read_diff_analog_input


###############################################################
#*** M&A Board Demo ***
###############################################################

# M&A Board hardware spec:
# https://www.magicdaq.com/product/ma-board-full-kit/

print('')
print('*** M&A Board Demo ***')
print('Ensure the USB DAQ is connected to the M&A board using the ribbon cable.')
print('Ribbon cable pin out on page 6 of: ')
print('https://www.magicdaq.com/mdaq350datasheet/')
print('Use the provided power cable to apply power to the M&A board.')

print('')
user_input = input('Press any key to continue.')


###############################################################
#*** Relay Demo ***
###############################################################

print('')
print('--- Relay Demo ---')

print('Setting all relays to closed.')
daq_one.set_digital_output(7, 1)
daq_one.set_digital_output(6, 1)
daq_one.set_digital_output(5, 1)
daq_one.set_digital_output(4, 1)
time.sleep(1)

relay_count = 1
digital_pin_count = 7

while relay_count <= 4:
    print('Relay #: ' + str(relay_count) + ' Digital Pin #: ' + str(digital_pin_count))

    # Set relay to open
    print('Setting relay to OPEN.')
    daq_one.set_digital_output(digital_pin_count, 0)
    time.sleep(1)

    # Increment counters
    relay_count += 1
    digital_pin_count -= 1

    print('')

print('')
user_input = input('Press any key to continue.')


###############################################################
#*** Vout Demo ***
###############################################################

print('')
print('--- Vout Demo ---')
print('Vout provides a variable voltage power output capable of up to 2A')
print('By characterizing your M&A board, or building a feedback loop; voltage accuracy of Vout can be made quite good.')
print('See notes on page 4 of the M&A data sheet.')
print('https://www.magicdaq.com/mdaq350datasheet/')

# See the M&A board data sheet for the equation that describes the Vout to Vout_set (0 and 2.77 here) relationship

print('')
print('Vout_set Set to 0V.')
print('Measure Vout with a multimeter. It should be about 10V')
daq_one.set_analog_output(0, 0)

print('')
user_input = input('Press any key to continue.')

print('Vout_set Set to 2.77V')
print('Measure Vout with a multimeter. It should be about 5V')
daq_one.set_analog_output(0, 2.77)
print('')
user_input = input('Press any key to continue.')


###############################################################
#*** Low Current Measurement Demo: A1 ***
###############################################################
print('')
print('--- A1 Low Current Measurement Demo ---')
print('Use the 3.3V board voltage and a 20K resistor to put 165uA through A1.')
print('')
user_input = input('Press any key to continue.')

# See the M&A board data sheet for the equation that describes the Vout to current relationship

pin_4_voltage = daq_one.read_analog_input(4)
print('Read voltage: ' + str(pin_4_voltage))
calculated_current_amps = pin_4_voltage / (332 * 97.863)
ua_current = round((calculated_current_amps / .000001), 3)
print('Calculated uA current: ' + str(ua_current))


###############################################################
#*** Current Measurement Demo: A2 ***
###############################################################
print('')
print('--- A2 Current Measurement Demo (+/- 5A max) ---')
print('Use an external 5V power supply and 5 ohm power resistor to put 1 Amp through A2.')
print('')
user_input = input('Press any key to continue.')

# See the M&A board data sheet for the equation that describes the Vout to current relationship

pin_5_voltage = daq_one.read_analog_input(5)
print('Read voltage: ' + str(pin_5_voltage))
calculated_current_amps = pin_5_voltage / (.01 * 200)
# ma_current = round((calculated_current_amps / .001), 3)
print('Calculated A current: ' + str(calculated_current_amps))

###############################################################
#*** Current Measurement Demo: A3 ***
###############################################################
print('')
print('--- A3 Current Measurement Demo (+/- 1.5A max) ---')
print('Use an external 5V power supply and 5 ohm power resistor to put 1 Amp through A3.')
print('')
user_input = input('Press any key to continue.')

# See the M&A board data sheet for the equation that describes the Vout to current relationship

pin_6_voltage = daq_one.read_analog_input(6)
print('Read voltage: ' + str(pin_6_voltage))
calculated_current_amps = pin_6_voltage / (.033 * 200)
ma_current = round((calculated_current_amps / .001), 3)
print('Calculated mA current: ' + str(ma_current))


###############################################################
#*** Demo Complete. ***
###############################################################

# Close connection to daq
daq_one.close_daq_device()

```