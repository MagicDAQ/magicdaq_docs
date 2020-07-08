---
category: Basic Analog Input
title: 'Basic Analog Input Example'
type: 'Analog-Input'
url_path: 'CODE EXAMPLE'

layout: default
---

### Example Code

```python

# Create MagicDAQDevice() object
daq_one = MagicDAQDevice()

# Configure sine wave output on AO0 with 500Hz, indefinente operation, and 4V amplitude
daq_one.configure_analog_output_sine_wave(0, 500, amplitude=4)

```

### Expected Output