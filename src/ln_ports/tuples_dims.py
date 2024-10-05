from livenodes import Ports_collection

from .primitives import *
from .compounds import *
from .compounds_dims import *
from .compounds_typed import Port_ListUnique_Str

# --- Common Constellations ----
class Ports_empty(Ports_collection):
    pass

class Ports_any(Ports_collection):
    any: Port_Any = Port_Any("Any")

class Ports_np(Ports_collection):
    data_np: Port_np_compatible = Port_np_compatible("Data NP")


# --- 1D Tuples ----
class Ports_1D_Number(Ports_collection):
    d1: Port_1D_Number = Port_1D_Number("List")

class Ports_ts_channels(Ports_1D_Number):
    channels: Port_ListUnique_Str = Port_ListUnique_Str("Channel Names")


# --- 2D Tuples ----
class Ports_2D_Number(Ports_collection):
    d2: Port_2D_Number = Port_2D_Number("Time Series")

class Ports_ts_channels(Ports_2D_Number):
    channels: Port_ListUnique_Str = Port_ListUnique_Str("Channel Names")


# --- 3D Tuples ----
class Ports_3D_Number(Ports_collection):
    d3: Port_3D_Number = Port_3D_Number("Batched TS")

class Ports_ts_channels(Ports_3D_Number):
    channels: Port_ListUnique_Str = Port_ListUnique_Str("Channel Names")
