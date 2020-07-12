---
category: Analog Input Stream
title: 'start_analog_input_stream()'
type: 'Analog-Input'
url_path: 'AI0 - AI7'

layout: default
---

Method starts the analog input stream.

### Definition 

```python
start_analog_input_stream()
```

### Returns

* `Returns: float` : Actual sampling frequency. The actual sample frequency may differ slightly from what is specified by the `measurement_frequency` parameter used with the `configure_analog_input_stream()` method due to DAQ hardware timer functionality.

