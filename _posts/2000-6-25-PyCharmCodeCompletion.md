---
category: Support
title: 'PyCharm Code Completion'

layout: default
---

[PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) is a commonly used Python IDE.

You can enable automatic code completion for the MagicDAQ API by adding the MagicDAQ directory location as a content root in your PyCharm Python project.

### Find MagicDAQ Directory

Open a command prompt, run Python, and enter the following code.

```python

import site
print(site.getsitepackages())

```

The above code will print out the directory location of site-packages - the location that Python stores all installed libraries.

```
>>>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import site
>>> print(site.getsitepackages())
['C:\\Python3,32bit', 'C:\\Python3,32bit\\lib\\site-packages']
>>>
```

For some [good reasons](https://stackoverflow.com/questions/11924706/how-to-get-rid-of-double-backslash-in-python-windows-file-path-string#:~:text=5%20Answers,-5&text=The%20double%20backslash%20is%20not%20wrong%2C%20python%20represents%20it%20way,to%20imply%20an%20actual%20backslash.&text=And%20in%20this%20printed%20string,by%20the%20letter%20't'.) python prints out directory locations with double slashes.
The directory location we are interested in is the one that contains 'site-packages'. We remove the double slashes to get something like:
```
C:\Python3,32bit\lib\site-packages
```

Add '\magicdaq' to the end of the site-packages location and you have the full path to the MagicDAQ library.
```
C:\Python3,32bit\lib\site-packages\magicdaq
```

### Add Content Root to Project Structure

Add the MagicDAQ library directory as a Content Root in the PyCharm [Project Structure](https://www.jetbrains.com/help/pycharm/configuring-project-structure.html)

File -> Settings -> Project Structure -> Add Content Root
* You can search `project structure` in the settings panel, then click on the Add Content Root button on the right side of the panel.

