from dataclasses import dataclass
@dataclass
class Simulation: id: int; user_id: int; expected_gpa: float = None; predicted_score: float = None
