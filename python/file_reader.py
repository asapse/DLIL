import os
import settings


class FileReader:

    EXCLUDED = ['excluded_region', 'inter_segment_gap']

    def read_files(self):
        output_file = open(settings.TRANS_MAN + '/dev.csv', 'w')
        labels = open(settings.DEV_LABELS, 'r').read().split('\n')
        for file in os.listdir(settings.TRANS_MAN_DEV_TXT):
            file_path = os.path.join(settings.TRANS_MAN_DEV_TXT, file)
            # print(file_path)
            file_content = open(file_path).read()
            text = ''
            for line in file_content.split('\n'):
                if not line.startswith(";;") and line:
                    parts = line.split('>')
                    infos = parts[0].split()
                    # print(infos)
                    if len(infos) > 2 and infos[2] not in self.EXCLUDED:
                        text += parts[1]
                    # if parts[2] != self.EXCLUDED:
                    #    print(parts)
            # print(infos[0])
            # print(text)

            # get classes
            for elem in labels:
                parts = elem.split('_')
                name = '_'.join(parts[:-1])
                print(name)
                if infos[0] == name:
                    class_val = parts[-1]
            output_file.write('{}\t{}\t{}\n'.format(infos[0], text, class_val))
        output_file.close()

    def test(self):
        pass
