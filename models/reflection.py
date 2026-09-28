from dataclasses import dataclass
@dataclass
class Reflection: id: int; user_id: int; notes: str = None; mood: str = None
