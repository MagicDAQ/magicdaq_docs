---
category: Counter PWM
title: 'Counter PWM Example'
type: 'Counter'
url_path: 'CTR0'

layout: default
---

Method configures analog output sine wave.

### Definition 

```python
configure_analog_output_sine_wave(channel, sine_frequency, total_cycle_count=0, amplitude=5)
```

### Required Arguments

* `channel: int` DAQ pin number. For example, channel 'AO0' is Analog Output pin `0`. There are two channels: `0` and `1`.
* `sine_frequency: float` The frequency of the sine waveform in Hz. Valid range from 1 Hz (`1`) to 31.25kHz (`31250`)

### Optional Arguments

* `total_cycle_count: int` The total number of cycles you want to output after a single start command.
    * Valid range from 1 cycle (`1`) to 10000 cycles (`10000`).
    * Omit this optional parameter if you want the PWM waveform to continue until stopped with a stop command.  
* `amplitude: float` The sine wave will range from 0V to the maximum amplitude you specify.
    * Valid range from 0.1V (`0.1`) to 5V (`5`).
    * Omitting this optional parameters will result in the sine wave ranging between 0 and 5 volts.

### Example Code

```python

# Create MagicDAQDevice() object
daq_one = MagicDAQDevice()

# Configure sine wave output on AO0 with 500Hz, indefinente operation, and 4V amplitude
daq_one.configure_analog_output_sine_wave(0, 500, amplitude=4)

```