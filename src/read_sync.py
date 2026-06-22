import json
import os
from dataclasses import dataclass
from typing import Dict

@dataclass
class ReadingProgress:
    book_id: str
    progress: int

class ReadSync:
    def __init__(self, data_dir: str = './data'):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def save_progress(self, progress: ReadingProgress):
        with open(os.path.join(self.data_dir, f'{progress.book_id}.json'), 'w') as f:
            json.dump({'book_id': progress.book_id, 'progress': progress.progress}, f)

    def load_progress(self, book_id: str) -> ReadingProgress:
        try:
            with open(os.path.join(self.data_dir, f'{book_id}.json'), 'r') as f:
                data = json.load(f)
                return ReadingProgress(data['book_id'], data['progress'])
        except FileNotFoundError:
            return ReadingProgress(book_id, 0)

    def sync(self, book_id: str, new_progress: int):
        progress = self.load_progress(book_id)
        progress.progress = new_progress
        self.save_progress(progress)

    def host_sync_server(self, port: int = 8080, book_id: str = None, new_progress: int = None):
        # Simple in-memory sync server for demonstration purposes
        sync_data: Dict[str, ReadingProgress] = {}
        if book_id and new_progress:
            sync_data[book_id] = ReadingProgress(book_id, new_progress)
            print(f"Synced {book_id} to {new_progress}")
        else:
            while True:
                # Simulate receiving a sync request
                book_id = input("Enter book ID: ")
                new_progress = int(input("Enter new progress: "))
                sync_data[book_id] = ReadingProgress(book_id, new_progress)
                print(f"Synced {book_id} to {new_progress}")

    def use_default_instance(self):
        # Simulate using a default sync instance
        print("Using default sync instance")
        # In a real implementation, this would connect to a remote server
        # For demonstration purposes, it just prints a message
