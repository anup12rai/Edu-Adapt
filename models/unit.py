from dataclasses import dataclass
@dataclass
class Unit: id: int; subject_id: int; unit_name: str; completion: float = 0
