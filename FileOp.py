import os


class FileOp:

    WHATSAPP_IMAGES = 1
    ZIP_FILE = 2

    def __init__(self, path):
        self.path = path
        self.extn = os.path.splitext(path)[1]

    def get_extn(self):
        return str(self.extn)

