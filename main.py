from pathlib import Path
import os

from Category import Category

backup_directory = "/home/nikhil/Desktop/workspace/test"
print(os.getcwd())
extn_list = []

ignore_list = [".crypt12", ".chck", ".tmp", ".webm", ".crypt1", ".wal"]
ignore_list = [".jpg"]
for x in Path(backup_directory).rglob("*"):
    if Path(x).is_dir():
        continue
    extn = os.path.splitext(x)[1]
    if extn in ignore_list:
        c = Category(x)
        if not c.target.__eq__(""):
            print(str(x) + " = " + str(c.target))
    if extn not in extn_list and not extn.__eq__(""):
        extn_list.append(extn)

# .crypt12
# .chck
# .tmp
# .jpg
# .mp4
# .webm
# .enc
# .docx
# .pdf
# .apk
# .opus
# .mp3
# .m4a
# .jpeg
# .webp
# .crypt1
# .zip
# .png
# .wal
# .app
# .dat
# .xml
# .splits
# .extdat
# .wfi
# .gz
# .properties
# .JPG
# .apks
# .wav
# .aac