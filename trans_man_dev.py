import subprocess
import SETTINGS


class TransManDev:

    def read_files(self):
        subprocess.Popen(SETTINGS.TRS2STM, shell=True)

	def test(self):
		pass
