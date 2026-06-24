import pytest
from src.sync_engine import SyncEngine, ReadingPosition
import time

def test_update_position():
    engine = SyncEngine()
    engine.update_position("device1", 10)
    engine.process_queue()
    assert engine.get_position("device1").position == 10

def test_get_position():
    engine = SyncEngine()
    engine.update_position("device1", 10)
    engine.process_queue()
    assert engine.get_position("device1").position == 10

def test_sync_devices():
    engine = SyncEngine()
    engine.update_position("device1", 10)
    engine.process_queue()
    assert engine.sync_devices("device1", "device2")
    assert engine.get_position("device2").position == 10

def test_sync_devices_no_position():
    engine = SyncEngine()
    assert not engine.sync_devices("device1", "device2")

def test_process_queue_multiple_updates():
    engine = SyncEngine()
    engine.update_position("device1", 10)
    engine.update_position("device1", 20)
    engine.process_queue()
    assert engine.get_position("device1").position == 20

def test_start_sync():
    engine = SyncEngine()
    engine.update_position("device1", 10)
    engine.start_sync()
    time.sleep(1) # wait for the thread to process the queue
    assert engine.get_position("device1") is not None
    assert engine.get_position("device1").position == 10
