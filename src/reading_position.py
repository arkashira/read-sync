import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class ReadingPosition:
    book_id: str
    position: int

class ReadingPositionService:
    def __init__(self):
        self.positions = {}

    def save_position(self, book_id: str, position: int):
        self.positions[book_id] = position

    def get_position(self, book_id: str) -> int:
        return self.positions.get(book_id, 0)

    def push_position(self, book_id: str, position: int):
        self.save_position(book_id, position)

    def pull_position(self, book_id: str) -> int:
        return self.get_position(book_id)

    def resolve_conflict(self, book_id: str, new_position: int) -> int:
        current_position = self.get_position(book_id)
        if new_position > current_position:
            self.save_position(book_id, new_position)
            return new_position
        return current_position

    def to_json(self) -> str:
        return json.dumps(self.positions)

    @classmethod
    def from_json(cls, json_str: str):
        service = cls()
        service.positions = json.loads(json_str)
        return service
