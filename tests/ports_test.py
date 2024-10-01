"""
TODO: Expand. For now only one test to satisfy CI/CD pipeline.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

from ln_ports import *

def _h(port, val):
    result, msg = port.check_value(val)
    assert result, msg

class TestProcessing:
    def test_port_timeseries_valid(self):
        _h(Port_Timeseries(), np.arange(100).reshape((20, 5)))

    def test_Port_np_compatible(self):
        _h(Port_np_compatible(), np.arange(100))
        _h(Port_np_compatible(), np.arange(100).reshape((20, 5)))
        _h(Port_np_compatible(), np.arange(100).reshape((1, 20, 5)))
        _h(Port_np_compatible(), [])
        _h(Port_np_compatible(), [10])
        _h(Port_np_compatible(), [[1], [2]])

        assert Port_np_compatible.can_input_to(Port_Timeseries)
        assert Port_np_compatible.can_input_to(Port_TS_Number)
        assert Port_np_compatible.can_input_to(Port_BTS_Int)
        assert not Port_np_compatible.can_input_to(Port_TS_Str)
