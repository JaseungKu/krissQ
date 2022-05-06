# InstrumentBase
# Jaseung Ku
# 5/6/23

import pyvisa
from abc import abstractmethod

class InstrumentBase(object):
    """ """

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
