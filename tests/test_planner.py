import unittest
from datetime import date
from algorithms.study_planner import build_plan
class PlannerTests(unittest.TestCase):
    def test_high_priority_urgent_task_is_first(self):
        plan=build_plan([{'title':'later','priority':'Low','due_date':date.today()}, {'title':'now','priority':'High','due_date':date.today()}])
        self.assertEqual(plan[0]['task']['title'],'now')
