import unittest
from unittest.mock import patch
from io import StringIO
from inspect import cleandoc


class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        from palindrome import palindrome
        self.assertIsInstance(palindrome(
            "kayak"), bool, "la fonction palindrome(...) doit renvoyer un bool, par exemple \"return True\"")
        self.assertTrue(palindrome("kayak"))
        self.assertTrue(palindrome("if fi"))
        self.assertFalse(palindrome("tracteur"))

    def test_punctuation(self):
        from palindrome import palindrome
        self.assertIsInstance(palindrome(
            "kayak"), bool, "la fonction palindrome(...) doit renvoyer un bool, par exemple \"return True\"")
        self.assertTrue(palindrome("Eva, Can I Stab Bats In A Cave?"))

    def test_display_ok(self):
        from palindrome import display_palindrome
        stdout = StringIO()
        with patch("sys.stdout", new=stdout):
            display_palindrome("elle")
            output = stdout.getvalue().strip("\n")
            self.assertGreater(len(
                output), 0, "la fonction display_palindrome(...) doit afficher des resultats, par exemple \"print(chaine)\"")
            expected = cleandoc("""
            elle
            elle
            OK""")
            self.assertEqual(output, expected)

    def test_display_difference(self):
        from palindrome import display_palindrome
        stdout = StringIO()
        with patch("sys.stdout", new=stdout):
            display_palindrome("cuisine")
            output = stdout.getvalue().strip("\n")
            self.assertGreater(len(
                output), 0, "la fonction display_palindrome(...) doit afficher des resultats, par exemple \"print(chaine)\"")
            expected = cleandoc("""
            cuisine
            enisiuc
            ^^   ^^""")
            self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
