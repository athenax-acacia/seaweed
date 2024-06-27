# see https://docs.pytest.org/en/latest/example/simple.html#control-skipping-of-tests-according-to-command-line-option

import pytest


def pytest_addoption(parser):
    parser.addoption("--run-slow", action="store_true", default=False, help="run slow tests")
    parser.addoption("--very-verbose",
                     action="count",
                     default=0,
                     dest="verbosity",
                     help="output more details; repeat the option to increase verbosity level")


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(session, config, items):
    run_slow = config.getoption("--run-slow")
    skip_slow = pytest.mark.skip(reason="give --run-slow option to run these tests")

    for item in items:
        if "slow" in item.keywords and not run_slow:
            item.add_marker(skip_slow)


@pytest.fixture
def very_verbose(request):
    return request.config.getoption("--very-verbose")
