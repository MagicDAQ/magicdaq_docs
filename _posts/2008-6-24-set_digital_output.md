---
category: Basic Digital I/O
title: 'set_digital_output()'
type: 'Digital-IO'
url_path: 'P0.0 - P0.7'

layout: default
---

Method makes a digital output pin either High or Low.

### Definition 

```python
set_digital_output(channel: int, pin_state: int)
```

### Required Arguments

* `channel: int` DAQ pin number. For example, channel 'P0.0' is pin number `0`. Must be an integer `0` - `7`.
* `pin_state: int `: State of digital output pin. `1` = High (5V) and `0` = Low (0V)