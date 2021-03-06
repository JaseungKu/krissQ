Qubit:
attribute:SSB, pulse_params(pulse_shape, length, pi2amp, piamp, drag,..), physical_channel
method: set_physical_channel()
Readout: SSB, pulse_params(pulse_shape, length, amp), physical_channel, set_physical_channel()
CR: controlQ, targetQ, SSB, length, amp, phase
from abs import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class MarkerChannel:
    phy_chan: PhysicalChannel
    length: float
