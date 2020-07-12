---
category: Analog Input Stream
title: 'get_full_streaming_data_buffer()'
type: 'Analog-Input'
url_path: 'AI0 - AI7'

layout: default
---

Method returns all data available in the streaming data buffer.

### Definition 

```python
get_full_streaming_data_buffer(only_new_data = True, read_and_delete = False)
```

### Optional Arguments

* `only_new_data: bool` : When only_new_data is set to `True`, this function will only return streaming data acquired since the last time this function was called. In other words, only 'new' data is returned. Default is `only_new_data = True`. 
* `read_and_delete: bool`: When read_and_delete is set to `True`, the data returned by this function will be deleted from the underlying streaming data buffer.
> * Setting `read_and_delete` to `True` reduces the total amount of memory used. However, `get_last_n_streaming_data_samples()` will not be able to return any data that has been previously deleted from the streaming data buffer by this function. Default is `read_and_delete = False`.

### Returns

* `[[float]]` : All data in the streaming data buffer. Data is returned as a list of data lists.
> * For example, streaming only channel 0 might return `[[0.5,0.5,0.5]]`
> * Streaming both channel 0 and chanel 1 might return `[[0.5,0.5,0.5],[1.5,1.5,1.5]]`
> * Channel data is returned in order of increasing channel number. For example, if channel 0 is being streamed it's data list is always returned at index 0. 