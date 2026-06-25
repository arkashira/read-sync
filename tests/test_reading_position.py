import pytest
from reading_position import ReadingPosition, ReadingPositionService

def test_save_position():
    service = ReadingPositionService()
    service.save_position("book1", 10)
    assert service.get_position("book1") == 10

def test_get_position():
    service = ReadingPositionService()
    service.save_position("book1", 10)
    assert service.get_position("book1") == 10

def test_push_position():
    service = ReadingPositionService()
    service.push_position("book1", 10)
    assert service.get_position("book1") == 10

def test_pull_position():
    service = ReadingPositionService()
    service.save_position("book1", 10)
    assert service.pull_position("book1") == 10

def test_resolve_conflict():
    service = ReadingPositionService()
    service.save_position("book1", 10)
    new_position = 20
    assert service.resolve_conflict("book1", new_position) == new_position

def test_to_json():
    service = ReadingPositionService()
    service.save_position("book1", 10)
    json_str = service.to_json()
    assert json_str == '{"book1": 10}'

def test_from_json():
    json_str = '{"book1": 10}'
    service = ReadingPositionService.from_json(json_str)
    assert service.get_position("book1") == 10

def test_conflict_resolution_last_write_wins():
    service = ReadingPositionService()
    service.save_position("book1", 10)
    new_position = 20
    service.resolve_conflict("book1", new_position)
    assert service.get_position("book1") == new_position
    older_position = 15
    assert service.resolve_conflict("book1", older_position) == new_position
