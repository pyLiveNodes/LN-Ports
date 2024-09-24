"""
TODO: Expand. For now only one test to satisfy CI/CD pipeline.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

from ln_ports import Port_Timeseries


class TestProcessing:

    def test_port_timeseries_valid(self):
        port_ts = Port_Timeseries()
        result, msg = port_ts.check_value(np.arange(100).reshape((20, 5)))
        assert result
        assert msg is None
