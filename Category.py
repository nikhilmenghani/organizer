import os


class Category:

    WHATSAPP_IMAGES = 1
    ZIP_FILE = 2

    def __init__(self, path):
        self.path = str(path)
        self.extn = os.path.splitext(self.path)[1]
        self.target = self.get_category()

    def get_category(self):
        target = ""
        if self.extn == ".jpg":
            if str(self.path).__contains__("WhatsApp/Media/WhatsApp Images"):
                target = "WhatsApp/Media/WhatsApp Images/" + self.get_file_name()
            elif str(self.path).__contains__("WhatsApp/.Shared/") \
                    or str(self.path).__contains__("Media/.Statuses/") \
                    or str(self.path).__contains__("Media/WhatsApp_Statuses/") \
                    or str(self.path).__contains__(".Thumbs/") \
                    or str(self.path).__contains__("DCIM/.thumbnails") \
                    or str(self.path).__contains__("Media/WhatsApp Profile Photos"):
                target = ""
            elif str(self.path).__contains__("Pictures/"):
                target = "Pictures"
            elif str(self.path).__contains__("WhatsApp/Media/WhatsApp Documents/"):
                target = "WhatsApp/Media/WhatsApp Documents/" + self.get_file_name()
            elif str(self.path).__contains__("/DCIM/"):
                target = "DCIM/" + self.get_file_name()
            else:
                target = ""
        return str(target)

    def get_file_name(self):
        return str(os.path.basename(self.path))
