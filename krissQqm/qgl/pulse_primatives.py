# Utheta, Xtheta, Ytheta, X90, Y90, Z, CR, echoCR, rotaryCR, ...)

from dataclasses import dataclass

@dataclass
class Pulse:
    """ Dataclass of Pulse class """

    channel:
    length: Float
    amp: Float
    phase: Float
    shape_params: Dict
    frequency: Float
    frame_change: Float


def Id(channel, *args, **kwargs):
    pass

def Utheta(channel, *args, **kwargs):
    pass
    
def X(channel, *args, **kwargs):
    pass
