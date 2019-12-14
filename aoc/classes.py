from dataclasses import dataclass
from typing import Any, Tuple


@dataclass
class AoCResult:
    result: Any
    comment: str


@dataclass
class AoCReturn:
    results: Tuple[AoCResult, AoCResult]
