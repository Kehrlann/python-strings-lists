import unittest
from calculatrice import postfix_eval


class TestCalculatrice(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(postfix_eval("3 5 +"), 8)

    def test_multiple_operands(self):
        self.assertEqual(postfix_eval("3 5 + 8 6 - *"), 16)

    def test_divide(self):
        self.assertEqual(postfix_eval("5 2 /"), 2)

    def test_syntax(self):
        self.assertEqual(postfix_eval("2 a +"), "error-syntax")

    def test_empty_stack(self):
        self.assertEqual(postfix_eval("+"), "error-empty-stack")
        self.assertEqual(postfix_eval("2 +"), "error-empty-stack")

    def test_unfinished(self):
        self.assertEqual(postfix_eval("1 2 3 +"), "error-unfinished")


if __name__ == "__main__":
    unittest.main()
