import unittest
import csv_generator as gen


class TestLabels(unittest.TestCase):

    def setUp(self):
        self.labels = gen.Labels('dev')

    def test_init(self):
        self.assertEqual(298, len(self.labels.dict_labels))

    def test_get_label_when_id_exists_expect_label(self):
        self.assertEqual('NVGO', self.labels.get_label('20091112_RATP_SCD_0096'))


class TestFileReader(unittest.TestCase):

    def test_read_file_when_folder_txt_not_exist_expect_exception(self):
        with self.assertRaises(Exception):
            gen.CSVGenerator('trans-manu/test').generate()

    def test_read_file(self):
        gen.CSVGenerator('trans-manu/train').generate()
