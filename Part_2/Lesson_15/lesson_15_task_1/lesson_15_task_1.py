#  EXIF: Задание 1 - 50 баллов

import exifread
import os
import re


def get_files_from_dir(path):
    files_list = []
    with os.scandir(path) as i:
        for f in i:
            if f.is_file() and re.match(r".+\.((jpg)|(JPG))", f.name):
                files_list.append(f.name)
    return files_list, path


def meta_data_jpg(data):
    for file in data[0]:
        with open(f"{data[1]}\{file}", "rb") as reader:
            tags = exifread.process_file(reader)
            if (str(tags["Image DateTime"]).split(":")[0] == "2019") and (str(
                    tags["Image DateTime"]).split(":")[1] == "09"):
                for tag in tags:
                    if re.match(r"EXIF.+", tag) is None and tag not in (
                            "JPEGThumbnail",
                            "Thumbnail JPEGInterchangeFormatLength",
                            "Interoperability InteroperabilityIndex",
                            "Interoperability InteroperabilityVersion",
                            "Thumbnail JPEGInterchangeFormat"):
                        print(f"{tag:<25} : {tags[tag]}")


if __name__ == "__main__":
    path = r"C:\Users\proic\Desktop\Python\Part 2\15 - EXIF\photo\photo"
    meta_data_jpg(get_files_from_dir(path))
