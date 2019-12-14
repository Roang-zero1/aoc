from dataclasses import dataclass
from typing import Any, Tuple


@dataclass
class Result:
    result: Any
    comment: str


@dataclass
class ResultReturn:
    results: Tuple[Result, Result]
