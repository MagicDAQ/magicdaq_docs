---
title: 'Install MagicDAQ'

layout: default
---

### MagicDAQ Hardware
To use this API, you will need the MagicDAQ hardware, which you can find at [magicdaq.com](https://www.magicdaq.com/)

### Python 3 on Windows
MagicDAQ must be run with Python 3 on Windows. MagicDAQ is downloaded using pip.

* You can download the latest version of Python [here](https://www.python.org/downloads/)
* Don't forget to [add Python to the Windows PATH](https://datatofish.com/add-python-to-windows-path/)

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

Open a command prompt and enter:

`python -m pip magicdaq`

### Upgrading an Existing Instillation of MagicDAQ

Open a command prompt and enter:

`python -m pip magicdaq --upgrade`

For full debug output enter:

`python -m pip magicdaq --upgrade -v`

### Authorize Driver Install

If this is your first time installing MagicDAQ, you will need to allow MagiDAQ to install it's driver on your computer.
During the instillation process, two pop ups will appear - please approve them.

![Alt Text](images/driver_installer_auth.png)

![Alt Text](images/driver_auth.png)  

[MagicDAQ is hosted on PyPi](https://pypi.org/project/magicdaq/)

