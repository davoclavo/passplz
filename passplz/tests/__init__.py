"""Tests for passplz"""

from unittest import TestCase

import passplz


class TestPassword(TestCase):
    """Generate a password and make sure it has length 16."""
    def test_default_length(self):
        """
        Test if the generate_password function of passplz is callable and
        if the returned password has length 16.
        """
        password = passplz.generate_password()
        self.assertEqual(16, len(password))

    def test_various_lengths(self):
        """
        Test if generation of various character long passwords work.
        """
        for i in range(2, 160):
            password = passplz.generate_password(i)
            self.assertEqual(i, len(password))
