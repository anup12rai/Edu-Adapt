import unittest
from utils.validator import valid_email
class AuthValidationTests(unittest.TestCase):
    def test_email_validation(self): self.assertTrue(valid_email('student@example.com')); self.assertFalse(valid_email('invalid'))
