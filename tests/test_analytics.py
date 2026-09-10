import unittest
from algorithms.readiness import calculate
class AnalyticsTests(unittest.TestCase):
    def test_readiness_is_bounded(self): self.assertGreaterEqual(calculate(0,0,0),0); self.assertLessEqual(calculate(10,10,100),100)
