import pytest

from NewtestApp.NewtestApp import NewtestApp


def test_NewtestApp_positive_factorial():
    """TODO: replace"""
    try:
        assert NewtestApp(0) == 1
        assert NewtestApp(1) == 1
        assert NewtestApp(5) == 120
        assert NewtestApp(10) == 3628800
    except Exception as e:
        pytest.fail(str(e))


def test_NewtestApp_negative_factorial():
    """TODO: replace"""
    try:
        assert NewtestApp(-5) is None
        assert NewtestApp(-10) is None
    except Exception as e:
        pytest.fail(str(e))
