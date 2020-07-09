---
category: Analog Output
title: 'set_analog_output()'
type: 'Analog-Output'
url_path: 'AO0 - AO1'

layout: default
---

Method sets the output voltage of an Analog Output pin.

### Definition 

```python
set_analog_output(channel: int, output_voltage: float)
```

### Required Arguments

* `channel: int` : DAQ pin number. For example, channel 'AO0' is Analog Output pin `0`. There are two channels: `0` and `1`.
* `output_voltage: float` : Voltage to output. May be any voltage between `0` and `5`.