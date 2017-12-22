import unittest
import file_reader as fr


class TestLabels(unittest.TestCase):

    def setUp(self):
        self.labels = fr.Labels('dev')

    def test_init(self):
        self.assertEqual(298, len(self.labels.dict_labels))

    def test_get_label_when_id_exists_expect_label(self):
        self.assertEqual('NVGO', self.labels.get_label('20091112_RATP_SCD_0096'))


class TestFileReader(unittest.TestCase):

    def test_read_file_when_folder_txt_not_exist_expect_exception(self):
        with self.assertRaises(Exception):
            fr.FileReader('trans-manu/test').read_files()

    def test_read_file(self):
        fr.FileReader('trans-manu/train').read_files()
