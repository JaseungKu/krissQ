# pulse_primitive.py
# Jaseung Ku, May 2023


# Here let's do only microwave qubit control
# pulse_primitives: Utheta, Xtheta, Ytheta, X90, Y90, Z, CR, echoCR, rotaryCR, ...)
# gate_primtives: X, Y, Z, CZ, iSWAP, CNOT, ...

# qubit channel: SSB, length, pi2amp, piamp, drag, shape_params(shape, key-value depending on shape)

import numpy as np
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Dict, List
from channel_libraries import IQChannel, MarkerChannel
from functools import lru_cache

# Logical channel means what a set of pulses is used for and defines the catergory of pulses.
# For example, a microwave pulse for qubit control, CR pulse, DC pulse for flux control or coupler,...
# Physical channel is physically existing ports on instrumetn.
# For example, AWG wave port, trigger, marker.

# class PhysicalChannel:
#         address:
    # offset: float = 0
    # amp: float = 1
#
# class LogicalChannel:
#     pass
#
# @dataclass
# class Qubit(LogicalChannel): # make this independant with instrument
#     physical_ch : List
#     frequency: float
#     length: float
#     pi2amp: float = None
#     piamp: float = None
#     drag: float = None
#     shape: str
#     amp_factor: float = 0
#     phase_skew: float = 0
#
#     def __post_init(self):
#         """ Create shape_params based on given 'shape' attribute. For example, gaussian has sampling_rate, sigma,.. """
#         self.create_shape_params(self.shape)
#
#     def create_shape_params(self):
        # if self.shape == 'gaussian':
        #     self.shape_params = {'cutoff': 2}
        # elif self.shape == 'tanh':
        #     self.shape_params = {'sigma': 1e-9}
        # elif self.shape == 'gaussianon':
        #     self.shape_params = {'sigma': 1e-9}

# @dataclasses
# class CR(LogicalChannel):
#         physical_ch
#         frequency:
#         length:
#         amp:
#         phase:
#         shape: 'flat_top_guassian'
#
#     def __post_init(self):
#         """ Create shape_params based on given 'shape' attribute. For example, gaussian has sampling_rate, sigma,.. """
#         self.create_shape_params(self.shape)


@dataclass
class Pulse:
    """ Pulse class represents a microwave pulse. The instance should have enough info to define waveforms in ANY AWG.
    """
    channel: Channel
    length: float # in sec
    amp: float =  0  # unitless
    phase: float = 0 # in degree
    shape_params: Dict # shape, sigma,...
    frame_change: float = 0 # in degree
    frequency: float = 0 # in MHz

def angle2amp(channel, angle: float):
    """ Convert angle in degree to amp in standard """

    return angle /180 *np.pi * channel.piamp]

#########################
# pulse_primitives
#########################
def Utheta(qubit, angle=0, phase=0, **kwargs):
    # kwargs: length, amp or angle, phase, frequency

    try:
        length = kwargs['length']
    except KeyError:
        length = qubit.length

    try:
        frequency = kwargs['frequency']
    except KeyError:
        frequency = qubit.frequency

    try:
        amp = kwargs['amp']
    except KeyError:
        amp = angle / 180 * qubit.piamp

    Pulse(qubit, length, amp, phase, shape_params=qubit.shape_params, frame_change=0, frequency)
def Xtheta(qubit, angle):
    return Utheta(qubit, angle, phase=0)
def CR(targetQ, length):
    pass
def echoCR(controlQ,
           targetQ,
           amp=1,
           phase=0,
           length=200e-9,
           riseFall=20e-9,
           lastPi=True, canc_amp = 0.0, canc_phase=np.pi/2):
           pass

#####################
# gate_primitives
#####################
def Id(qubit, **kwargs ): pass
def X(qubit):
    return Utheta(qubit, angle=180, phase=0)
def X90(qubit):
    return Utheta(qubit, angle=90, phase=0)
def Xm(qubit):
    return Utheta(qubit, angle=-180, phase=0)
def X90m(qubit):
    return Utheta(qubit, angle=-90, phase=0)
def Z(qubit, phase: float):
    """ Virtual Z gate.
        Args:
            channel: Channel instance
            phase:   rotation around Z axis in degree
    """
    return Pulse(channel, frame_change=-phase)
def ZX90_CR(controlQ, targetQ, **kwargs):
    return echoCR(controlQ, targetQ, xxx )
def CNOT(controlQ, targetQ, **kwargs): pass
def iSWAP(qubit1, qubit2, **kwargs): pass
def CZ(qubit1, qubit2, **kwargs): pass
