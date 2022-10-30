import unittest
from tempfile import TemporaryDirectory
from comptage import comptage
from shutil import copyfile
from pathlib import Path
from inspect import cleandoc


class TestComptage(unittest.TestCase):

    def setUp(self):
        self.test_dir = TemporaryDirectory(ignore_cleanup_errors=True)
        self.test_path = Path(self.test_dir.name)
        self.input = self.test_path / "lorem_ipsum.txt"
        self.output = self.test_path / "lorem_ipsum_comptage.txt"
        copyfile(Path(".github") / "lorem_ipsum.txt", self.input)
        copyfile(Path(".github") / "romeo_juliet.txt", "romeo_juliet.txt")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_does_not_modify_input(self):
        with open(self.input, "r") as f:
            content = f.read()
        comptage(self.input, self.output)
        after_open_content = ""
        try:
            with open(self.input, "r") as f:
                after_open_content = f.read()
        except:
            pass
        self.assertEqual(content, after_open_content, "la fonction \"comptage\" ne devrait pas changer le contenu du fichier d'entrée")

    def test_writes_output(self):
        expected = cleandoc("""
        1:5:28:Lorem ipsum dolor sit amet,
        2:3:29:consectetur adipiscing elit,
        3:7:43:sed do eiusmod tempor incididunt ut labore
        4:4:24:et dolore magna aliqua.
        """)
        comptage(self.input, self.output)
        with open(self.output, "r") as f:
            content = cleandoc(f.read())
        self.assertEqual(expected, content, "la fonction \"comptage\" ne devrait pas changer le contenu du fichier d'entrée")


if __name__ == "__main__":
    unittest.main()
