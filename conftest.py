import pytest
from datetime import datetime
from distutils.command.config import config

def pytest_configure(config):
    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
    config.option.log_file = "Logs/test_log." + timestamp + ".log"

    