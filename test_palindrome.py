import unittest
from unittest.mock import patch
from io import StringIO
from inspect import cleandoc
from palindrome import palindrome, display_palindrome


class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(palindrome("kayak"), "kayak est un palindrome")
        self.assertTrue(palindrome("if fi"), "if fi est un palindrome")
        self.assertFalse(palindrome("tracteur"), "tracteur n'est pas un palindrome")

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
            self.assertEqual(output, expected, "elle est un palindrome")

        stdout = StringIO()
        with patch("sys.stdout", new=stdout):
            expected = cleandoc("""
            cuisine
            enisiuc
            ^^   ^^""")
            display_palindrome("cuisine")
            output = stdout.getvalue()
            self.assertEqual(output, expected, "cuisine n'est pas un palindrome")


if __name__ == "__main__":
    unittest.main()