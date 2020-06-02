from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client import Client


class Activity:  # 활동
    def serialize(self):
        return {
            'week': self.week,
            'name': self.name,
            'done': self.done
        }

    def __init__(self, week: int, name: str, done: bool):
        self.week: int = week
        self.name: str = name
        self.done: bool = done
