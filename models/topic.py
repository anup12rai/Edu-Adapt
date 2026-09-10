from dataclasses import dataclass
@dataclass
class Topic: id: int; unit_id: int; topic_name: str; status: str = 'Pending'
