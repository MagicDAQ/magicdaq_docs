---
category: Analog Input Stream
title: 'set_streaming_data_buffer_max_rows()'
type: 'Analog-Input'
url_path: 'AI0 - AI7'

layout: default
---

Method sets the maximum number of rows allowed in the streaming data storage buffer. The default (if this function is not used) is 480000 (roughly 0.8Gb if all 8 channels are streamed and the buffer is full). Each row is 192 bytes maximum.
* Most users do not use this method. 
* Only use this method if you need to tightly control the amount of memory your application consumes during runtime.

### Definition 

```python
set_streaming_data_buffer_max_rows(max_rows: int)
```

### Required Arguments

* `max_rows : int` : Maximum number of rows allowed for the streaming data buffer. Valid entries between `1000` and `10000000` inclusive.