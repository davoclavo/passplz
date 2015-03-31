"""Tests for passplz"""

from unittest import TestCase

import passplz


class TestPasswordy(TestCase):
    """Generate a password and make sure it has length 16."""
    def test_is_string(self):
        """
        Test if the generate_password function of passplz is callable and
        if the returned password has length 16.
        """
        password = passplz.generate_password()
        self.assertEqual(16, len(password))
