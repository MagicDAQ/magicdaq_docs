# Use the USB cable to plug MagicDAQ into your computer

# Import standard time module
import time

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Connect to the MagicDAQ
daq_one.open_daq_device()

# Set constant 2.5V output on pin AO0
daq_one.set_analog_output(0,2.5)
print ('Pausing for 10 sec to allow time to measure pin AO0 (should be constant 2.5V)')
time.sleep(10)

# Configure a 500 Hz frequency, 3.3V amplitude continuous Sine Wave on pin AO0
daq_one.configure_analog_output_sine_wave(0,500, amplitude=3.3)

# Configure a 500 HZ frequency, 50% duty cycle, 5V amplitude, continuous PWM Wave on pin AO1
daq_one.configure_analog_output_pwm_wave(1,500,50)

# Start both AO0 and AO1 waves
daq_one.start_analog_output_wave(0)
daq_one.start_analog_output_wave(1)

print ('Pausing for 10 sec to allow time to observe with oscilloscope waveforms on pins AO0 and AO1')
time.sleep(10)

# Now stopping the output waves
daq_one.stop_analog_output_wave(0)
daq_one.stop_analog_output_wave(1)

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()
