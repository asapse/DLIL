import os

import settings


class FileReader:

    @staticmethod
    def read_files():
        for file in os.listdir(settings.TRANS_MAN_DEV_TXT):
            print(file)

    def test(self):
        pass
