import pytest
from unittest.mock import Mock, call
import time

from io_relays.Timed_io import *


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

def test_Timer_drip_GIVEN_initialized_WHEN_nothing_THEN_returns_not_running():
    mock = get_mock_io_irrigation()

    drip = Timed_valve_drip(mock)

    assert drip.is_running() is False

def test_Timer_drip_GIVEN_stopped_WHEN_start_THEN_opens_valve():
    mock = get_mock_io_irrigation()

    drip = Timed_valve_drip(mock)

    drip.start(5)

    mock.set_valve_drip.assert_called_with(True)
    assert drip.is_running() is True

    drip.stop()

def test_Timer_drip_GIVEN_started_WHEN_stopped_THEN_closes_valve():
    mock = get_mock_io_irrigation()

    drip = Timed_valve_drip(mock)

    drip.start(5)
    drip.stop()

    expectations = [call(True),
                    call(False)]

    mock.set_valve_drip.assert_has_calls(expectations, any_order=False)
    assert drip.is_running() is False

    drip.stop()

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

##################

def test_Timer_refill_GIVEN_initialized_WHEN_nothing_THEN_returns_not_running():
    mock = get_mock_io_irrigation()

    refill = Timed_valve_refill(mock)

    assert refill.is_running() is False

def test_Timer_refill_GIVEN_stopped_WHEN_start_THEN_opens_valve():
    mock = get_mock_io_irrigation()

    refill = Timed_valve_refill(mock)

    refill.start(5)

    mock.set_valve_refill.assert_called_with(True)
    assert refill.is_running() is True

    refill.stop()

def test_Timer_refill_GIVEN_started_WHEN_stopped_THEN_closes_valve():
    mock = get_mock_io_irrigation()

    refill = Timed_valve_refill(mock)

    refill.start(5)
    refill.stop()

    expectations = [call(True),
                    call(False)]

    mock.set_valve_refill.assert_has_calls(expectations, any_order=False)
    assert refill.is_running() is False

    refill.stop()


##################

def test_Timer_filter_GIVEN_initialized_WHEN_nothing_THEN_returns_not_running():
    mock = get_mock_io_irrigation()

    filter = Timed_valve_filter(mock)

    assert filter.is_running() is False

def test_Timer_filter_GIVEN_stopped_WHEN_start_THEN_opens_valve():
    mock = get_mock_io_irrigation()

    filter = Timed_valve_filter(mock)

    filter.start(5)

    mock.set_valve_filter.assert_called_with(True)
    assert filter.is_running() is True

    filter.stop()

def test_Timer_filter_GIVEN_started_WHEN_stopped_THEN_closes_valve():
    mock = get_mock_io_irrigation()

    filter = Timed_valve_filter(mock)

    filter.start(5)
    filter.stop()

    expectations = [call(True),
                    call(False)]

    mock.set_valve_filter.assert_has_calls(expectations, any_order=False)
    assert filter.is_running() is False

    filter.stop()




