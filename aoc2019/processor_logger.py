import json
from logging import Filter, Formatter, LogRecord, StreamHandler, getLogger
from pathlib import Path
from typing import List


class FunctionFilter(Filter):
    functions: List[str]
    all: bool = False

    def __init__(self):
        file_path = Path.resolve(Path(__file__))
        configuration_path = Path(file_path.parent, f"{file_path.stem}.json")
        if configuration_path.exists():
            with open(configuration_path) as configuration_file:
                config = json.load(configuration_file)
                self.all = config.get("all", False)
                self.functions = config.get("functions", [])
        else:
            self.functions = []

    def filter(self, record: LogRecord) -> int:
        return record.funcName in self.functions or self.all


def get_processor_logger(name: str):
    logger = getLogger(name)
    logger.propagate = False
    sh = StreamHandler()
    formatter = Formatter("%(levelname)s:%(name)s:%(funcName)s:%(message)s")
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addFilter(FunctionFilter())
    return logger
