---
category: Analog Output
title: 'start_analog_output_wave()'
type: 'Analog-Output'
url_path: 'AO0 - AO1'

layout: default
---

Method starts the analog output wave.

* You must configure the analog output port for a wave before using this command to start the wave.
* See methods `configure_analog_output_sine_wave()` and `configure_analog_output_pwm_wave()`

### Definition 

```python
start_analog_output_wave(channel: int)
```

### Required Arguments

* `channel: int` DAQ pin number. For example, channel 'AO0' is Analog Output pin `0`. There are two channels: `0` and `1`.
