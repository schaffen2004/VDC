import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.utils.logging import Logger

logger = Logger()

def test_log_info():
    logger.log("This is an info message", mode="Info")
    logger.log(["Info message line 1", "Info message line 2"], mode="Info")

test_log_info()