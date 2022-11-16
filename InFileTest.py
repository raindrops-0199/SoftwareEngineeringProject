import unittest

from InFile import InFile


class InFileTest(unittest.TestCase):

    def test_read_folder(self):
        path = "input/4A"
        infile = InFile(path)
        infile.read_folder()
        files = ["101036360.cpp", "127473352.cpp", "173077807.cpp", "84822638.cpp",
                 "117364748.cpp", "134841308.cpp", "48762087.cpp", "84822639.cpp"]
        files = set(files)
        self.assertEqual(files, set(infile.src_files))

    def test_parse_stdin1(self):
        path = "input/4A"
        infile = InFile(path)
        infile.parse_stdin()
        exp_type = ["int"]
        exp_range = [range(1, 100)]
        self.assertEqual(exp_type, infile.inType)
        self.assertEqual(exp_range, infile.inRange)

    def test_parse_stdin2(self):
        path = "input/50A"
        infile = InFile(path)
        infile.parse_stdin()
        exp_type = ["int", "int"]
        exp_range = [range(1, 16), range(1, 16)]
        self.assertEqual(exp_type, infile.inType)
        self.assertEqual(exp_range, infile.inRange)


if __name__ == '__main__':
    unittest.main()
