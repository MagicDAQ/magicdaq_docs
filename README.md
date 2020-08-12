### MagicDAQ Overview

[MagicDAQ](https://www.magicdaq.com/) is a data acquisition and test automation device (USB DAQ) powered by an easy to use [Python API](https://magicdaq.github.io/magicdaq_docs/).

MagicDAQ Key Features:

* 8 Analog inputs, 14 bit resolution, 48 KS/s maximum measurement frequency, -/+ 10V input voltage range
* 8 Digital inputs / outputs, 0 to 5V range
* 2 Analog outputs / PWM outputs / sine wave outputs, 0 to 5V range
* 1 Pulse counter / PWM output, 0 to 3.3V range 
* Electrically isolated - the DAQ ground and the USB power supply ground are not electrically connected. 
    * Isolation improves the accuracy of measurements by preventing electrical noise from the power supply and connected computer from coupling into the measurement circuitry.
* Well documented [Python API](https://magicdaq.github.io/magicdaq_docs/) contains code examples for all functions.

MagicDAQ Hardware Docs:

All hardware documentation can be found at [MagicDAQ.com](https://www.magicdaq.com/product/magic-daq/)

* [Data Sheet](https://www.magicdaq.com/wp-content/uploads/2020/06/MagicDAQDataSheetREV10.pdf)
* [3D Model (.stp)](https://www.magicdaq.com/wp-content/uploads/2020/06/MDAQ300STEPModelREV10.zip)
* [Mechanical Drawing](https://www.magicdaq.com/wp-content/uploads/2020/06/MagicDAQMDAQ300MechanicalDRWREV10.pdf)

### Getting Started with MagicDAQ

You can [install MagicDAQ](https://magicdaq.github.io/magicdaq_docs/#/Install_MagicDAQ) using pip:
```
python -m pip install magicdaq
```

Full API documentation and code examples:

* [MagicDAQ API Docs](https://magicdaq.github.io/magicdaq_docs/)

### Measurement & Automation Board Overview

An extensive set of hardware testing capabilities can be accessed by connecting the MagicDAQ to the [M&A Board](https://www.magicdaq.com/product/ma-board-full-kit/). The M&A Board can be used in conjunction with the MagicDAQ, an alternative USB DAQ, or can be used stand alone.

M&A Board Key Features:

* 3 Current measurement circuits, 5A maximum
* 1 Low current measurement circuit, measures uAs
* 4 Temperature measurement probes, -55C to 125C range
* 4 Switching relays, 10A maximum switching capacity
* 1 Variable voltage power output , 1V to 10V range, 2A maximum current output
* 2 Fixed voltage power outputs, 3.3V and 12V outputs, 2A maximum current output

M&A Board Hardware Docs:

All hardware documentation can be found at [MagicDAQ.com](https://www.magicdaq.com/product/ma-board-full-kit/)

* [Data Sheet](https://www.magicdaq.com/wp-content/uploads/2020/07/MABoardDataSheetREV10.pdf)
* [3D Model (.stp)](https://www.magicdaq.com/wp-content/uploads/2020/07/MABoard3DModels.zip)
* [Mechanical Drawing](https://www.magicdaq.com/wp-content/uploads/2020/07/MABoardMDAQ350MechanicalDRWREV10.pdf)

### API Docs Website Tech Details

You are presently viewing the Github repository behind the [MagicDAQ API documentation website](https://magicdaq.github.io/magicdaq_docs/).

* This website is built for [Github Pages](https://pages.github.com/) and is powered by [Jekyll](https://jekyllrb.com/)
* It is built on top of a modified version of the [Carte Theme](https://github.com/Wiredcraft/carte)
    * Big thank you to the team over at Carte!
* Please feel free to fork this repo and use the underlying structure to document your own projects if you would like.
    * We found and fixed a couple bugs in the Carte Theme while working on this project - you may want to use this repo as a starting place or do a diff between this repo and Carte.