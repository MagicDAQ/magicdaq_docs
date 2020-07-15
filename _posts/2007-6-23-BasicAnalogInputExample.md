---
category: Basic Analog Input
title: 'Basic Analog Input Example'
type: 'Analog-Input'
url_path: 'CODE EXAMPLE'

layout: default
---

### Example Code

[Source File](https://github.com/MagicDAQ/magicdaq_docs/tree/master/example_python_files)

```python

# Use the USB cable to plug MagicDAQ into your computer

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Connect to the MagicDAQ
daq_one.open_daq_device()

# Single ended analog input voltage measurement on pin AI0
# This voltage will be approximately 0.5V if nothing is connected to the DAQ (pin is 'floating')
pin_0_voltage = daq_one.read_analog_input(0)
print('Single ended analog input voltage measurement on pin AI0: '+str(pin_0_voltage))

# Differential voltage measurement between pin AI1 and AI2
# This voltage should be roughly 0V if nothing is connected to the DAQ (pins are 'floating')
pin_1_pin_2_diff_voltage = daq_one.read_diff_analog_input(1, 2)
print('Differential voltage measurement between pin AI1 and pin AI2: '+str(pin_1_pin_2_diff_voltage))

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()

```

### Expected Output

```
Single ended analog input voltage measurement on pin AI0: 0.51
Differential voltage measurement between pin AI1 and pin AI2: 0.00
```