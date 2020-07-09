---
category: Analog Output
title: 'configure_analog_output_pwm_wave()'
type: 'Analog-Output'
url_path: 'AO0 - AO1'

layout: default
---

Method configures analog output PWM wave.

### Definition 

```python
configure_analog_output_pwm_wave(channel: int, pwm_frequency: float, pwm_duty_cycle: float, total_cycle_count=0, amplitude=5)
```

### Required Arguments

* `channel: int` DAQ pin number. For example, channel 'AO0' is Analog Output pin `0`. There are two channels: `0` and `1`.
* `sine_frequency: float` The frequency of the sine waveform in Hz. Valid range from 1 Hz (`1`) to 31.25kHz (`31250`)
* `pwm_duty_cycle: float` : The duty cycle of the PWM waveform. Valid range from 0% (`0`) to 100% (`100`) duty cycle.

### Optional Arguments

* `total_cycle_count: int` The total number of cycles you want to output after a single start command.
    * Valid range from 1 cycle (`1`) to 10000 cycles (`10000`).
    * Omit this optional parameter if you want the PWM waveform to continue until stopped with a stop command.  
* `amplitude: float` The sine wave will range from 0V to the maximum amplitude you specify.
    * Valid range from 0.1V (`0.1`) to 5V (`5`).
    * Omitting this optional parameters will result in the sine wave ranging between 0 and 5 volts.
