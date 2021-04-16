# Use the USB cable to plug MagicDAQ into your computer

# Import standard time module
import time

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Connect to the MagicDAQ
daq_one.open_daq_device()

# Configure a 50 KHz frequency, 75% duty cycle, 3.3V amplitude, continuous PWM Wave on the counter pin (CTR0)
daq_one.configure_counter_pwm(50000,75)

# Start the counter PWM wave
daq_one.start_counter_pwm()

print('Pausing for 10 sec to allow time to observe with oscilloscope waveform on pin CTR0')
time.sleep(10)

# Now stopping the counter PWM wave
daq_one.stop_counter_pwm()

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()
