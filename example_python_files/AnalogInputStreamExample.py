# Use the USB cable to plug MagicDAQ into your computer

# Import standard time module
import time

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Connect to the MagicDAQ
daq_one.open_daq_device()

# Configure analog input stream for pins AI1 and AI2. Sampling frequency of 200 Hz.
# Remember, analog input streaming only supports single ended measurement (measuring between AI1 and AGND for example).
daq_one.configure_analog_input_stream([1,2], 200)

print('Streaming AI1 and AI2 at 200Hz.')

# Start the analog input stream
daq_one.start_analog_input_stream()

# Use a loop to read the incoming data
# This kind of structure could be used to provide data to a continuously updated display
read_cycle_count = 0
while read_cycle_count < 3:

    print('')
    print('Pausing for 1 sec to acquire streamed data')
    time.sleep(1)
    print('')

    # Get the last 20 samples of streamed data
    last_20_samples = daq_one.get_last_n_streaming_data_samples(20)
    print('last_20_samples: '+str(last_20_samples))

    read_cycle_count += 1

# Stop the data stream
daq_one.stop_analog_input_stream()

# Get the entire data buffer
# This method can be used to see all of the data that was gathered while streaming
all_streamed_data = daq_one.get_full_streaming_data_buffer()
print('')
print('all_streamed_data: ' + str(all_streamed_data))

# We no longer need the data in the streaming buffer, so we can delete it
daq_one.delete_streaming_data_buffer()

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()
