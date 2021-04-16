---
category: Analog Input Stream
title: 'configure_analog_input_stream()'
type: 'Analog-Input'
url_path: 'AI0 - AI7'

layout: default
---

Method configures single ended analog input stream.
* Streaming supports single ended measurement only (voltage between AI pin and AGND)

### Definition 

```python
configure_analog_input_stream(channels: [int], measurement_frequency: float, decimal_places = 2)
```

### Required Arguments

* `channels: [int]`: List of analog input pin numbers to stream from. For example, to stream from channel 0 only enter `[0]`. To stream from both channel 0 and channel 1, enter `[0,1]`.
* `measurement_frequency: float` : Measurement frequency. Valid range from 1 Hz (`1`) to 48kHz (`48000`). The maximum measurement_frequency possible is contingent on the number of channels being streamed. Expressed as an equation: measurement_frequency * number of channels being streamed <= 48000

### Optional Arguments

* `decimal_places : int` : Number of decimal places the readings are rounded to. `decimal_places = 2` is default. Maximum suggested is 3.