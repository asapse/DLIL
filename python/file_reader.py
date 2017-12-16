import os
import settings


class Labels:

    def __init__(self):
        labels = open(settings.DEV_LABELS, 'r').read().split('\n')
        dict_labels = dict()
        for elem in labels:
            parts = elem.split('_')
            name = '_'.join(parts[:-1])
            if name is not '':
                dict_labels[name] = parts[-1]
        self.dict_labels = dict_labels

    def get_label(self, id):
        """
        :param id: Recording identifier.
        :type id: str
        :return: Label of the given recording.
        :rtype str
        """
        return self.dict_labels[id]


class FileReader:

    EXCLUDED = ['excluded_region', 'inter_segment_gap']

    def read_files(self):
        """
        Creates of csv file with 3 columns (ID, TEXT, LABEL), each line represents an audio transcription.
        """
        with open(settings.TRANS_MAN + '/dev.csv', 'w') as output_file:

            labels = Labels()
            for file in os.listdir(settings.TRANS_MAN_DEV_TXT):
                file_path = os.path.join(settings.TRANS_MAN_DEV_TXT, file)
                # print(file_path)
                file_content = open(file_path).read()
                text = ''
                for line in file_content.split('\n'):
                    if not line.startswith(";;") and line:
                        parts = line.split('>')
                        infos = parts[0].split()
                        if len(infos) > 2 and infos[2] not in self.EXCLUDED:
                            text += parts[1]

                output_file.write('{}\t{}\t{}\n'.format(infos[0], text, labels.get_label(infos[0])))
