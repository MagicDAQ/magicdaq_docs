---
category: Analog Input Stream
title: 'get_last_n_streaming_data_samples()'
type: 'Analog-Input'
url_path: 'AI0 - AI7'

layout: default
---

Method returns the most recently acquired n_samples of streamed data. 
* This method does not clear or delete the streaming data buffer.
* The same data as before will be returned by the function if no new streaming data has been acquired since the last time this method has been called.
* Use this method when building a continuously updating display for streamed data.

### Definition 

```python
get_last_n_streaming_data_samples(n_samples:int)
```

### Required Arguments

* `n_samples : int` : Number of samples to return. If n_samples is greater than the length of the streaming_data_buffer, all available data points will be returned. `n_samples` must be >= 1.

### Returns

* `[[float]]` : Last n_samples of streamed data. Data is returned as a list of data lists.
> * For example, streaming only channel 0 might return `[[0.5,0.5,0.5]]`
> * Streaming both channel 0 and chanel 1 might return `[[0.5,0.5,0.5],[1.5,1.5,1.5]]`
> * Channel data is returned in order of increasing channel number. For example, if channel 0 is being streamed it's data list is always returned at index 0. 