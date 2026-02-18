"""
Basic TARDIS Benchmark.
"""

import functools

from benchmarks.benchmark_base import BenchmarkBase
from tardis.transport.montecarlo.modes.classic.montecarlo_transport import (
    montecarlo_transport,
)


class BenchmarkTransportMontecarloMontecarloMainLoop(BenchmarkBase):
    """
    Class to benchmark montecarlo_transport function (classic mode).
    """

    repeat = 3

    @functools.cache
    def setup(self):
        self.packet_collection = self.transport_state.packet_collection
        self.geometry_state = self.transport_state.geometry_state
        self.time_explosion = self.verysimple_time_explosion
        self.opacity_state = self.transport_state.opacity_state

    def time_montecarlo_transport(self):
        montecarlo_transport(
            self.packet_collection,
            self.geometry_state,
            self.time_explosion,
            self.opacity_state,
            self.montecarlo_configuration,
            self.nb_simulation_verysimple.transport.spectrum_frequency_grid.value,
            self.rpacket_tracker_list,
            self.montecarlo_configuration.NUMBER_OF_VPACKETS,
            show_progress_bars=True,
        )
