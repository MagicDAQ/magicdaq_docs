---
category: Basic Digital I/O
title: 'read_digital_input()'
type: 'Digital-IO'
url_path: 'P0.0 - P0.7'

layout: default
---

Method reads a digital input pin and returns either 1 (meaning High) or 0 (meaning Low).
* The digital input pin has an internal pull-up resistor. As such, the pin defaults to High.
* If the digital pin has previously been driven Low by a `set_digital_output()` command, ensure that you run
            the `read_digital_input()` command before applying external voltage. This prevents excessive current being
            shunted to GND, possibly damaging the DAQ.

### Definition 

```python
read_digital_input(channel: int)
```

### Required Arguments

* `channel: int` DAQ pin number. For example, channel 'P0.0' is pin number `0`. Must be an integer `0` - `7`.

### Returns

* pin_status : int : `1` = High, `0` = Low
