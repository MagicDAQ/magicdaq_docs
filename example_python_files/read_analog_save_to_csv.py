##############################################################
#*** MagicDAQ Demo: Read Analog Inputs and Save to CSV File ***
##############################################################

# This demo shows how to read analog inputs from two pins and save the results in a .csv file
# The .csv file can be opened with excel to create a plot of the data

#*** Documentation Website ***
# MagicDAQ Docs Website:
# https://magicdaq.github.io/magicdaq_docs/

#*** Install MagicDAQ ***
# Download the MagicDAQ python package from pypi
# Run this command in a command prompt:
# python -m pip install magicdaq
# Further docs: https://magicdaq.github.io/magicdaq_docs/#/Install_MagicDAQ
# MagicDAQ is only compatible with Python 3 on Windows.

#*** Using Auto Code Complete With PyCharm ***
# Using a code editor like Pycharm and want to get auto complete working for the MagicDAQ package?
# Docs: https://magicdaq.github.io/magicdaq_docs/#/PyCharmCodeCompletion

##############################################################
#*** Imports ***
##############################################################

import time
import csv

# Import MagicDAQ
from magicdaq.api_class import MagicDAQDevice

#*** Connect to DAQ Device ***

# Create daq_one object
daq_one = MagicDAQDevice()
# Connect to the MagicDAQ
daq_one.open_daq_device()

##############################################################
#*** IMPORTANT: Set Acquisition Type ***
##############################################################

# This script demonstrates two different ways of acquiring data:
# Slowly (using read_analog_input() ) and quickly (using streaming methods)

# If set to True, slow data acquisition demonstrated (read_analog_input() )
# If set to False, fast data acquisition demonstrated (uses streaming methods )
DATA_ACQUIRED_SLOWLY = True

##############################################################
#*** Sample Data: Input Voltage Into Analog 0 and Analog 1 ***
##############################################################

# To test this script out, you might want to input some example voltages into analog 0 and analog 1
# Use two pieces of wire to connect:
# Analog Output 0 (AO0) to Analog Input 0 (AI0)
# Analog Output 1 (AO1) to Analog Input 0 (AI1)

# You can comment out this section if you don't want to use the sample input voltages

# Set output voltages
# 2 volts on Analog Input 0
daq_one.set_analog_output(0,2)
# 4 volts on Analog Input 1
daq_one.set_analog_output(1,4)

##############################################################
#*** Create the CSV File to Save Data To ***
##############################################################

# Create the log file
# You will find this file in the same directory that this script (read_anlog_save_to_csv.py) is located in

# 'w+': Create the file for writing if it does not exist. If file already exists, overwrite it.
# Explanation of file opening parameters:
# https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function

# Need to add: newline="" to prevent the csv writer from inserting a blank row after every row
# https://stackoverflow.com/questions/46057470/python-skips-line-when-printing-to-csv

# IMPORANT: You can not have this CSV file open in a program (Excel) if you are trying to write to it with Python
# This will cause a permissions error. You can wrap this open in a Try Except block with a custom error if you like.
csv_log_file = open('analog_input_data.csv', 'w+', newline="")

# Make a CSV 'writer'
csv_writer = csv.writer(csv_log_file)

# Log file format:
# [current_time, analog_input_1, analog_input_2]
log_file_header = ['Time (Sec)', 'Analog Input 0', 'Analog Input 1']

# Write header to log file
csv_writer.writerow(log_file_header)

##############################################################
#*** Read Analog Inputs: The Slow, Easy Way ***
##############################################################

if DATA_ACQUIRED_SLOWLY:

    # If you need to read analog inputs at a frequency of less than 1 Hz, we suggest
    # using the read_analog_input() method in a loop. We use this function because it is easier to implement
    # than the analog streaming functions

    #*** Read Two Analog Inputs, Once Every 15 Sec ***

    # Print test header to screen
    print('--- Starting Test (Slow Data Acquisition) ---')
    print('')

    # Total length of test in minutes
    total_test_time_min = 2

    # Time that test started
    # time.time() returns the current time expressed in seconds
    test_start_time = time.time()

    while (time.time() < (test_start_time + (total_test_time_min*60)) ):

        analog_input_0 = daq_one.read_analog_input(0)
        analog_input_1 = daq_one.read_analog_input(1)

        # Calculate the time since starting the test
        # We round the result to single sec. So 15.03 becomes 15
        time_since_start = round(time.time() - test_start_time)

        # Save data to the log
        csv_writer.writerow([time_since_start,analog_input_0,analog_input_1])

        print('Analog Input 0: ',analog_input_0,' Analog Input 1: ',analog_input_1)

        # Time to wait in sec before taking next reading
        pause_time = 15
        print('Waiting for ',pause_time,' sec before taking next reading.' )
        print('')

        # Pause the program for 15 sec
        time.sleep(15)

    #*** The Test is Complete ***

    print('')
    print('--- Test Now Complete ---')

    # Don't forget to close the file
    csv_log_file.close()


##############################################################
#*** Read Analog Inputs: The Fast, Streaming Way ***
##############################################################

if not DATA_ACQUIRED_SLOWLY:

    # If you need to read analog inputs at a frequency of greater than 1 Hz, we suggest
    # using the streaming functionality. This way, the frequency at which samples are taken will be more accurate.

    # Configure the streaming analog input channels
    # On both analog input 0 and 1, acquire 10 samples per sec

    # frequency to stream data at (Hz)
    streaming_frequency = 10

    daq_one.configure_analog_input_stream([0,1],streaming_frequency)

    # Print test header to screen
    print('--- Starting Test (Fast Data Acquisition) ---')
    print('Streaming Frequency (Hz): ', streaming_frequency)
    print('')

    # Total length of test in minutes
    total_test_time_min = 0.5

    # Time that test started
    # time.time() returns the current time expressed in seconds
    test_start_time = time.time()

    # Start stream
    daq_one.start_analog_input_stream()

    # Wait for test to complete
    while (time.time() < (test_start_time + (total_test_time_min *60)) ):

        # Every 5 sec, print out the latest data
        # Remember, this function returns data in the form [[analog_input_0],[analog_input1]]
        # See: https://magicdaq.github.io/magicdaq_docs/#/get_last_n_streaming_data_samples
        latest_samples = daq_one.get_last_n_streaming_data_samples(1)

        # We need to check that latest_samples has some data in it because when the
        # streaming function first starts out, there will be no data in the buffer
        if len(latest_samples[0])>=1 and len(latest_samples[1])>=1:
            print('Analog Input 0: ',latest_samples[0][0],' Analog Input 1: ',latest_samples[1][0])

        # Wait for 5 sec
        print('Will print latest sample in 5 sec.')
        print('')
        time.sleep(5)

    # The test has now completed.

    # Stop the analog input stream.
    daq_one.stop_analog_input_stream()

    # Total length of test
    print('Total Test Time (sec): ', round((time.time() - test_start_time),3) )

    #*** Save the Data To The CSV ***

    # Get the entire streaming data buffer
    # Remember, this function returns data in the form [[analog_input_0],[analog_input1]]
    # https://magicdaq.github.io/magicdaq_docs/#/get_full_streaming_data_buffer
    all_streaming_data = daq_one.get_full_streaming_data_buffer()

    print('Number of data points gathered for each analog input: ', len(all_streaming_data[0]))

    data_index = 0
    while data_index < len(all_streaming_data[0]):
        # Calculate time at this data point (sec)
        time_at_data_point = round((data_index *(1/streaming_frequency)),3)

        # Save data to the log
        csv_writer.writerow([time_at_data_point, all_streaming_data[0][data_index], all_streaming_data[1][data_index]])

        data_index += 1

    print('')
    print ('--- Test Complete ---')

    # Don't forget to close the file
    csv_log_file.close()
