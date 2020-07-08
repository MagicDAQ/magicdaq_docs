---
category: Basic Analog Input
title: 'read_analog_input()'
type: 'Analog-Input'
url_path: 'AI0 - AI7'

layout: default
---

Method reads an analog input pin and returns the voltage.
* A 'single ended' measurement is performed, meaning voltage is measured between the analog input pin and ground (AGND).
* The maximum input voltage for the analog input pins is +/- 10V (referenced to AGND)

### Definition 

```python
read_analog_input(channel: int, decimal_places = 2)
```

### Required Arguments

* `channel: int` : DAQ pin number. For example, channel 'AI0' is pin number `0`. Must be an integer `0` - `7`.

### Optional Arguments

* `decimal_places : int` : Number of decimal places the reading is rounded to. decimal_places = `2` is default. Maximum suggested is `3`.

### Returns

* `voltage: float` : the voltage measured at the analog input pin specified.