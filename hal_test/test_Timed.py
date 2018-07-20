import pytest
from unittest.mock import Mock, call
import time

from ..hal.Timed import *


def get_mock_startable_stoppable():
    mock = Mock()
    return mock

def test_IO_timer_GIVEN_initialized_WHEN_nothing_THEN_returns_not_running():
    mock = get_mock_startable_stoppable()

    io_t = Timed(mock)
    assert io_t.is_running() is False
    assert not mock.on_started.called
    assert not mock.on_stopped.called

def test_IO_timer_GIVEN_initialized_WHEN_stopped_THEN_does_not_stop_returns_not_running():
    mock = get_mock_startable_stoppable()

    io_t = Timed(mock)
    io_t.stop()

    assert io_t.is_running() is False
    assert not mock.on_started.called
    assert not mock.on_stopped.called

def test_IO_timer_GIVEN_initialized_WHEN_started_THEN_starts_and_returns_running():
    mock = get_mock_startable_stoppable()

    io_t = Timed(mock)
    io_t.start(0.5)

    assert mock.on_started.called
    assert not mock.on_stopped.called
    assert io_t.is_running()

def test_IO_timer_GIVEN_initialized_WHEN_started_and_elapsed_THEN_stops_and_returns_not_running():
    mock = get_mock_startable_stoppable()

    io_t = Timed(mock)
    io_t.start(0.5)
    time.sleep(1)

    assert mock.on_stopped.called
    assert not io_t.is_running()

def test_IO_timer_GIVEN_started_WHEN_started_THEN_restarts_and_returns_running():
    mock = get_mock_startable_stoppable()

    io_t = Timed(mock)
    io_t.start(1)
    time.sleep(0.5)

    assert mock.on_started.call_count is 1
    assert mock.on_stopped.call_count is 0
    assert io_t.is_running()

    io_t.start(1)
    time.sleep(0.5)

    assert mock.on_started.call_count is 2
    assert mock.on_stopped.call_count is 0
    assert io_t.is_running()

    time.sleep(1)

    assert mock.on_started.call_count is 2
    assert mock.on_stopped.call_count is 1
    assert not io_t.is_running()