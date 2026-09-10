import unittest
from algorithms.risk_prediction import predict
class RiskTests(unittest.TestCase):
    def test_risk_is_bounded(self):
        self.assertEqual(predict(100,0,10000),0)
        self.assertGreaterEqual(predict(0,99,0),0)
        self.assertLessEqual(predict(0,99,0),100)
