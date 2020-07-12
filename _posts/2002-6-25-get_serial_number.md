---
category: Get System Info
title: 'get_serial_number()'
type: 'System'

layout: default
---

Method returns as a string the serial number of the DAQ that is currently open.

* This function must be run *after* `open_daq_device()` is run.

### Definition 

```python
get_serial_number()
```

### Returns

* `str`: the connected DAQ serial number