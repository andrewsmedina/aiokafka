from kafka.metrics.stats.sampled_stat import AbstractSampledStat as AbstractSampledStat
from typing import Any

class Max(AbstractSampledStat):
    def __init__(self) -> None: ...
    def update(self, sample: Any, config: Any, value: Any, now: Any) -> None: ...
    def combine(self, samples: Any, config: Any, now: Any): ...
