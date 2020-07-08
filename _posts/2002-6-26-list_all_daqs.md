---
category: Get System Info
title: 'list_all_daqs()'
type: 'System'

layout: default
---

Function returns a list of the serial numbers for all DAQs connected to the computer. If no DAQs are connected, an empty list [] is returned.

* This function must be run *before* `open_daq_device()` is run.

### Definition 

```python
list_all_daqs()
```

### Returns

* `[str,str]` : list of serial numbers. Serial numbers are in string format.
