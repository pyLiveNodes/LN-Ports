from livenodes import Ports_collection

from .primitives import *
from .compounds import *
from .compounds_typed import *


class Ports_empty(Ports_collection):
    pass


class Ports_BTS_data(Ports_collection):
    data: Port_BTS_Number = Port_BTS_Number("Data")


class Ports_any(Ports_collection):
    any: Port_Any = Port_Any("Any")


class Ports_np(Ports_collection):
    data_np: Port_np_compatible = Port_np_compatible("Data NP")


class Ports_BTS_data_channels(Ports_collection):
    data: Port_BTS_Number = Port_BTS_Number("Data")
    channels: Port_ListUnique_Str = Port_ListUnique_Str("Channel Names")


class Ports_ts(Ports_collection):
    ts: Port_Timeseries = Port_Timeseries("TimeSeries")


class Ports_ts_channels(Ports_collection):
    ts: Port_Timeseries = Port_Timeseries("TimeSeries")
    channels: Port_ListUnique_Str = Port_ListUnique_Str("Channel Names")
