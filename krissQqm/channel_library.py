Qubit:
attribute:SSB, pulse_params(pulse_shape, length, pi2amp, piamp, drag,..), physical_channel
method: set_physical_channel()
Readout: SSB, pulse_params(pulse_shape, length, amp), physical_channel, set_physical_channel()
CR: controlQ, targetQ, SSB, length, amp, phase
from abs import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class PhysicalChannel:
    address:
    offset: float = 0
    amp: float = 1

@dataclass
class IQChannel:
    phy_chan_I: PhysicalChannel
    phy_chan_Q: PhysicalChannel
    length: float 
    SSB: float = 0
    ampfactor: float = 0
    phase_skew: float =0
    shape_params: Dict
    pulse_params: Dict = None
    
@dataclass
class MarkerChannel:
    phy_chan_I: PhysicalChannel
    length: float 

I1 = PhysicalChannel(address)
Q1 = PhysicalChannel(address1)
shape_params = {'shape':'gaussian', 'cutoff':2}
q1 = IQChannnel(PhysicalChannel(xxx)
            , PhysicalChannel(xxx)
            , length=50e-9
            , SSB=-100e6
            , shape_params=shape_params
            )
m1 = IQChanneel(
