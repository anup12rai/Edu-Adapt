from dataclasses import dataclass
@dataclass
class Subject: id: int; user_id: int; subject_name: str; credits: int = 0; priority: str = 'Medium'
