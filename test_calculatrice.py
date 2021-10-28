import unittest
from calculatrice import postfix_eval, postfix_eval_typed


class TestCalculatrice(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(postfix_eval("3 5 +", 8))

    def test_multiple_operands(self):
        self.assertEqual("3 5 + 6 8 - *", 16)

    def test_syntax(self):
        pass

    def test_empty_stack(self):
        pass
    def test_unfinished(self):

        pass
#
#    error-syntax si on ne peut pas comprendre l'entrée,
#    error-empty-stack, si on essaie de faire une opération mais que l'on n'a pas les deux opérandes nécessaires,
#    error-unfinished, si on détecte des opérandes non utilisés.

if __name__ == "__main__":
    unittest.main()