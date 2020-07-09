---
category: Support
title: 'Get API Version'

layout: default
---

You can get the current version of the MagicDAQ API using the following code.

### Example Code

```python

import pkg_resources
print('MagicDAQ API Version: '+pkg_resources.get_distribution("magicdaq").version)

```

### Example Output
```
MagicDAQ API Version: 1.0.0
```