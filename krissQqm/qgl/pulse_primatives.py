# Utheta, Xtheta, Ytheta, X90, Y90, Z, CR, echoCR, rotaryCR, ...)
import numpy as np
from dataclasses import dataclass
from abc import ABC, abstractclass
from typing import Dict, List
from channel_libraries import Channel

@dataclass
class Pulse:
    """ Pulse class represents a microwave pulse. The instance attributes are parameters that is needed to define the pulse.    
    """

    channel: Channel
    amp: float = 0
    phase: float = 0 # in degree
    shape_params: Dict = pulse_shapes.tanh
    frequency: float = 0 # in MHz
    frame_change: float = 0 # unit?

def angle2amp(channel, angle: float):
    """ Convert angle in degree to amp"""

    return angle /360 *2*np.pi * channel.pulse_params['piamp']

def Id(channel, *args, **kwargs):
    pass

def Utheta(channel: Channel, *args, **kwargs):
    return Pulse(channel, *args, **kwargs) 

def Xtheta(channel, *args, **kwargs):
    return Utheta(channel, phase=0)

def X(channel, *args, **kwargs):
    return Xtheta(channel, amp=angle2amp(180))

def Xm
    """ X rotation by -180 degree"""
    return 

def X90m

def X90(channel, *arg, **kwargs):
    return Xtheta(channel, amp=angle2amp(90))

def Ytheta
def Y
def Y90

def Z(channel, pi: float): -> Pulse
    """ Virtual Z rotation.
        Args: 
            channel: Channel instance
            phi:  phi rotation around Z axis in degree
    """
    return Pulse(channel, frame_change=-phi)

def CR(CR_channel: Channel):
    try:
        return 
    
def echoCR
