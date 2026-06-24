import json
import dataclasses
import time
from datetime import datetime, timedelta
from queue import Queue
from threading import Thread

@dataclasses.dataclass
class ReadingPosition:
    device_id: str
    position: int
    timestamp: datetime

class SyncEngine:
    def __init__(self):
        self.queue = Queue()
        self.device_positions = {}

    def update_position(self, device_id, position):
        self.queue.put((device_id, position))

    def process_queue(self):
        while not self.queue.empty():
            device_id, position = self.queue.get()
            self.device_positions[device_id] = ReadingPosition(device_id, position, datetime.now())
            self.queue.task_done()

    def get_position(self, device_id):
        return self.device_positions.get(device_id)

    def start_sync(self):
        thread = Thread(target=self.process_queue)
        thread.daemon = True
        thread.start()

    def sync_devices(self, device_a, device_b):
        position_a = self.get_position(device_a)
        if position_a:
            self.update_position(device_b, position_a.position)
            self.process_queue() # Process the queue immediately
            return True
        return False
