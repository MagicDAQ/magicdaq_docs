---
title: 'Install MagicDAQ'
type: 'System'

layout: default
---

### MagicDAQ Hardware
To use this API, you will need the MagicDAQ hardware, which you can find at [magicdaq.com](https://www.magicdaq.com/)

### Python 3 on Windows Only
MagicDAQ must be run with Python 3 on Windows. MagicDAQ is downloaded using pip.

* You can download the latest version of Python [here](https://www.python.org/downloads/)
* Don't forget to [add Python to the Windows PATH](https://datatofish.com/add-python-to-windows-path/)
* MagicDAQ only works on Windows. Linux and Mac are not supported due to hardware driver constraints.

You can test if your system is ready to go by [opening a command prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089) and entering:

`python -m pip`

You are ready to download MagicDAQ if you get back something like the following:
```
Usage:
  C:\Users\srh\AppData\Local\Programs\Python\Python36\py3.exe -m pip <command> [options]

Commands:
```
If you see something different, [please check that pip is installed and working.](https://projects.raspberrypi.org/en/projects/using-pip-on-windows)

If you need a bit of help getting started with MagicDAQ, feel free to email us at: 

> support@magicdaq.com

### Install MagicDAQ with Pip

To install MagicDAQ for the first time, open a command prompt and enter:

`python -m pip install magicdaq`

To upgrade an existing instillation of MagicDAQ, open a command prompt and enter:

`python -m pip install magicdaq --upgrade`

* [MagicDAQ is hosted on PyPi](https://pypi.org/project/magicdaq/). The PyPi page shows the latest version number for the MagicDAQ package. 
* To see install debug output, add `-v` to the end of above command

### Authorize Driver Install

If this is your first time installing MagicDAQ, you will need to allow MagicDAQ to install its driver on your computer.
* During the instillation process, two pop ups will appear - please approve them.

![Alt Text](images/driver_installer_auth.png)

![Alt Text](images/driver_auth.png) 

