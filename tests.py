#!python
import unittest
from pathlib import Path

loader = unittest.TestLoader()
start_dir = Path(__file__).parent
suite = loader.discover(str(start_dir))

runner = unittest.TextTestRunner()
runner.run(suite)
