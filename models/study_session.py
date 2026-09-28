from dataclasses import dataclass
@dataclass
class StudySession: id: int; user_id: int; subject_id: int = None; duration: int = 0
