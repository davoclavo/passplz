from unittest import TestCase

import passplz

class TestPasswordy(TestCase):
    def test_is_string(self):
        password = passplz.generate_password()
        self.assertEqual(16, len(password))
