from dataclasses import dataclass
@dataclass
class Task: id: int; user_id: int; title: str; description: str = None; due_date: str = None; priority: str = 'Medium'; status: str = 'Pending'
