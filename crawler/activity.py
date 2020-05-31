from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from section import Section
    from client import Client


class Activity:
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
