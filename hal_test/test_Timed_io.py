import pytest
from unittest.mock import Mock, call
import time

from hal.Timed_io import *


def get_mock_io_irrigation():
    mock = Mock()
    return mock

def test_Timer_valve_left_GIVEN_initialized_WHEN_nothing_THEN_returns_not_running():
    mock = get_mock_io_irrigation()

    valve_left = Timed_valve_left(mock)

    assert valve_left.is_running() is False

def test_Timer_valve_left_GIVEN_stopped_WHEN_start_THEN_opens_valve():
    mock = get_mock_io_irrigation()

    valve_left = Timed_valve_left(mock)

    valve_left.start(5)

    mock.set_valve_left.assert_called_with(True)
    assert valve_left.is_running() is True

    valve_left.stop()

def test_Timer_valve_left_GIVEN_started_WHEN_stopped_THEN_closes_valve():
    mock = get_mock_io_irrigation()

    valve_left = Timed_valve_left(mock)

    valve_left.start(5)
    valve_left.stop()

    expectations = [call(True),
                    call(False)]

    mock.set_valve_left.assert_has_calls(expectations, any_order=False)
    assert valve_left.is_running() is False

    valve_left.stop()

#############

def test_Timer_valve_right_GIVEN_initialized_WHEN_nothing_THEN_returns_not_running():
    mock = get_mock_io_irrigation()

    valve_right = Timed_valve_right(mock)

    assert valve_right.is_running() is False

def test_Timer_valve_right_GIVEN_stopped_WHEN_start_THEN_opens_valve():
    mock = get_mock_io_irrigation()

    valve_right = Timed_valve_right(mock)

    valve_right.start(5)

    mock.set_valve_right.assert_called_with(True)
    assert valve_right.is_running() is True

    valve_right.stop()

def test_Timer_valve_right_GIVEN_started_WHEN_stopped_THEN_closes_valve():
    mock = get_mock_io_irrigation()

    valve_right = Timed_valve_right(mock)

    valve_right.start(5)
    valve_right.stop()

    expectations = [call(True),
                    call(False)]

    mock.set_valve_right.assert_has_calls(expectations, any_order=False)
    assert valve_right.is_running() is False

    valve_right.stop()

##################

def test_Timer_pump_GIVEN_initialized_WHEN_nothing_THEN_returns_not_running():
    mock = get_mock_io_irrigation()

    pump = Timed_pump(mock)

    assert pump.is_running() is False

def test_Timer_pump_GIVEN_stopped_WHEN_start_THEN_opens_valve():
    mock = get_mock_io_irrigation()

    pump = Timed_pump(mock)

    pump.start(5)

    mock.set_pump.assert_called_with(True)
    assert pump.is_running() is True

    pump.stop()

def test_Timer_pump_GIVEN_started_WHEN_stopped_THEN_closes_valve():
    mock = get_mock_io_irrigation()

    pump = Timed_pump(mock)

    pump.start(5)
    pump.stop()

    expectations = [call(True),
                    call(False)]

    mock.set_pump.assert_has_calls(expectations, any_order=False)
    assert pump.is_running() is False

    pump.stop()







