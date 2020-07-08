---
category: Getting Started
title: 'MagicDAQ Hello World Example'
type: 'System'
url_path: 'CODE EXAMPLE'

layout: default
---

### Import MagicDAQDevice Object
Every Python script must import the MagicDAQDevice object. 

```python
from magicdaq.api_class import MagicDAQDevice
```

All features of the MagicDAQDevice are accessed by creating a MagicDAQDevice object and calling methods on this object.
* Create `MagicDAQDevice` object
* Open the DAQ with `open_daq_device()`
* Do usefull things with the DAQ by calling methods on the object
* Close the DAQ with `close_daq_device()`

### Hello World Example Code

```python

# Use the USB cable to plug MagicDAQ into your computer

# Import MagicDAQDevice object
from magicdaq.api_class import MagicDAQDevice

# Create daq_one object
daq_one = MagicDAQDevice()

# Connect to the MagicDAQ
daq_one.open_daq_device()

# Do use full things with the DAQ
# For example, you can read a digital pin's state
print ('This is Digital Pin P0.0 State: '+str(daq_one.read_digital_input(0)))

# We are done using the MagicDAQ, so close it
daq_one.close_daq_device()

```

### Expected Output

```
This is Digital Pin P0.0 State: 1
```