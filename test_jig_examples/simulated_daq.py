# This file simulates the MagicDAQ
# Using this file, you can run the example_jig.py file without a physical MagicDAQ USB DAQ connected to your computer

class MagicDAQDevice:
    def read_analog_input(self, pin):
        # 3.3V
        if pin == 0:
            return 3.1
        # 5V
        elif pin == 1:
            return 4.85
        # 150uA
        elif pin == 4:
            return 4.80
        # 1A
        elif pin == 5:
            return 2.2
        return 3.1

    def set_digital_output(self, pin, state):
        return

    def open_daq_device(self):
        return
