---
category: Pulse Counter
title: 'enable_pulse_counter()'
type: 'Counter'
url_path: 'CTR0'

layout: default
---

Method enables the pulse counter.
* When the pulse counter is enabled, the pulse count value is re-set to 0.

### Definition 

```python
enable_pulse_counter(edge_type = 0)
```

### Optional Arguments

* `edge_type: int` : The pulse counter may be set for falling edge detection (`edge_type = 0`) or rising edge detection (`edge_type = 1`). By default, falling edge detection is set.
