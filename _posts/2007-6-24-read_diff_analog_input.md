---
category: Basic Analog Input
title: 'read_diff_analog_input()'
type: 'Analog-Input'
url_path: 'AI0 - AI7'

layout: default
---

Method reads the differential voltage between two analog input pins.
* A 'differential' measurement is performed, meaning voltage is measured between two analog input pins.
* The maximum input voltage for each analog input pin is +/- 10V (referenced to AGND)

### Definition 

```python
read_diff_analog_input(channel_p: int, channel_n: int, decimal_places = 2)
```

### Required Arguments

* `channel_p: int` : Positive analog input DAQ pin number. For example, channel 'AI0' is pin number `0`. Must be an integer `0` - `7`.
* `channel_n: int` : Negative analog input DAQ pin number. For example, channel 'AI0' is pin number `0`. Must be an integer `0` - `7`.

### Optional Arguments

* `decimal_places : int` : Number of decimal places the reading is rounded to. decimal_places = `2` is default. Maximum suggested is `3`.

### Returns

* `voltage: float` : the voltage difference between the two analog input pins. Voltage = Vpositive input pin - Vnegative input pin.
