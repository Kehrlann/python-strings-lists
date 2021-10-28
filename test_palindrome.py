import unittest
from unittest.mock import patch
from io import StringIO
from inspect import cleandoc
from palindrome import palindrome, display_palindrome


class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(palindrome("kayak"))
        self.assertTrue(palindrome("if fi"))
        self.assertFalse(palindrome("tracteur"))

    def test_punctuation(self):
        self.assertTrue(palindrome("Eva, Can I Stab Bats In A Cave?"))

    def test_display(self):
        stdout = StringIO()
        with patch("sys.stdout", new=stdout):
            expected = cleandoc("""
            elle
            elle
            OK""")
            display_palindrome("elle")
            output = stdout.getvalue()
            self.assertEqual(output, expected)

        stdout = StringIO()
        with patch("sys.stdout", new=stdout):
            expected = cleandoc("""
            cuisine
            enisiuc
            ^^   ^^""")
            display_palindrome("cuisine")
            output = stdout.getvalue()
            self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()