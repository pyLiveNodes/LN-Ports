from .primitives import *
from .compounds import *
from .compounds_typed import *


class Ports_empty(NamedTuple):
    pass


class Ports_BTS_data(NamedTuple):
    data: Port_BTS_Number = Port_BTS_Number("Data")


class Ports_any(NamedTuple):
    any: Port_Any = Port_Any("Any")


class Ports_np(NamedTuple):
    data_np: Port_np_compatible = Port_np_compatible("Data NP")


class Ports_BTS_data_channels(NamedTuple):
    data: Port_BTS_Number = Port_BTS_Number("Data")
    channels: Port_List_Str = Port_List_Str("Channel Names")


class Ports_ts(NamedTuple):
    ts: Port_Timeseries = Port_Timeseries("TimeSeries")
