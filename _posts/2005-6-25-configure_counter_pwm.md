---
category: Counter PWM
title: 'configure_counter_pwm()'
type: 'Counter'
url_path: 'CTR0'

layout: default
---

Method configures counter PWM output.
* The PWM waveform is output on the channel labeled 'CTR0' on the DAQ.
* The PWM waveform is 3.3V amplitude

### Definition 

```python
configure_counter_pwm(pwm_frequency: float, pwm_duty_cycle: float, total_cycle_count = 0)
```

### Required Arguments

* `pwm_frequency: float `: The frequency of the PWM waveform in Hz. Valid range from 1 Hz (`1`) to 65.535kHz (`65535`)
* `pwm_duty_cycle: float `: The duty cycle of the PWM waveform. Valid range from 0% (`0`) to 100% (`100`) duty cycle.

### Optional Arguments

* `total_cycle_count: int `: The total number of pulses you want the PWM to output after a single start_pwm_output() command.
    * Valid range from 1 pulse (`1`) to 65535 pulses (`65535`).
    * Omit this optional parameter if you want the PWM waveform to continue until stopped with a stop_pwm_output() command.