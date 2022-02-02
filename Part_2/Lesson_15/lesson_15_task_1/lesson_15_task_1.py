#  EXIF: Задание 1 - 50 баллов

import exifread
import os
import re

filters = "JPEGThumbnail Thumbnail JPEGInterchangeFormatLength " \
          "Interoperability InteroperabilityIndex " \
          "Interoperability InteroperabilityVersion " \
          "Thumbnail JPEGInterchangeFormat"


def get_files_from_dir(path):
    with os.scandir(path) as scan:
        return [f.name for f in scan if f.is_file() and
                      re.match(r".+\.((jpg)|(JPG))", f.name)], path


def meta_data_jpg(data):
    for file in data[0]:
        with open(f"{data[1]}\{file}", "rb") as reader:
            tags_print(reader)


def tags_print(reader):
    tags = exifread.process_file(reader)
    if (str(tags["Image DateTime"]).split(":")[0] == "2019") and (str(
            tags["Image DateTime"]).split(":")[1] == "09"):
        for tag in tags:
            if re.match(r"EXIF.+", tag) is None and tag not in filters:
                print(f"{tag:<25} : {tags[tag]}")


if __name__ == "__main__":
    path = r"C:\Users\proic\Desktop\Python\Part 2\15 - EXIF\photo\photo"
    meta_data_jpg(get_files_from_dir(path))
