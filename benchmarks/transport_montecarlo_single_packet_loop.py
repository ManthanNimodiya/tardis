"""
Basic TARDIS Benchmark.
"""

from benchmarks.benchmark_base import BenchmarkBase
from tardis.transport.montecarlo.modes.classic.packet_propagation import (
    packet_propagation,
)


class BenchmarkTransportMontecarloSinglePacketLoop(BenchmarkBase):
    """
    Class to benchmark the single packet loop function (packet_propagation).
    """

    repeat = 2

    def time_single_packet_loop(self):
        packet_propagation(
            self.packet,
            self.verysimple_numba_radial_1d_geometry,
            self.verysimple_time_explosion,
            self.verysimple_opacity_state,
            self.estimators_bulk,
            self.estimators_line,
            self.verysimple_3vpacket_collection,
            self.rpacket_tracker,
            self.montecarlo_configuration,
        )
