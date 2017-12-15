import unittest
import file_reader as fr


class TestFileReader(unittest.TestCase):

    def test_read_file(self):
        fr.FileReader().read_files()
