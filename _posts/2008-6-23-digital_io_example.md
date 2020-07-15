---
category: Basic Digital I/O
title: 'Digital IO Example'
type: 'Digital-IO'
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

# Read Pin P0.0 State
# If no external voltage is applied to the DAQ, the internal pull up resistor will ensure this pin is HIGH
print ('This is Digital Pin P0.0 State: '+str(daq_one.read_digital_input(0)))

print ('Now setting P0.1 to LOW.')
# Set Pin P0.1 to LOW
daq_one.set_digital_output(1,0)

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()

```

### Expected Output

```
This is Digital Pin P0.0 State: 1
Now setting P0.1 to LOW.
```