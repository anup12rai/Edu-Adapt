import unittest
from utils.validator import one_of
class SubjectTests(unittest.TestCase):
    def test_priority_is_constrained(self): self.assertEqual(one_of('Urgent', {'Low','Medium','High'}, 'Medium'), 'Medium')
