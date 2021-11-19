#  Аргументы: Задание 1 - 30 баллов
import argparse


class FileReaderWriter:
    def __init__(self, domain):
        self.domain = domain

    def file_reader_writer(self):
        with open("base.txt", encoding="utf-8") as reader, \
                open(f"email_{self.domain.lstrip('.')}.txt", "a",
                     encoding="utf-8") as writer:
            for email in reader:
                if email.find(self.domain) != -1:
                    writer.write(email)


class ArgsParse:
    def __init__(self):
        parser = argparse.ArgumentParser(description='parsing emails')
        parser.add_argument('domain', type=str, help='email`s domain')
        self.args = parser.parse_args()

    def emails(self):
        FileReaderWriter(self.args.domain).file_reader_writer()


if __name__ == '__main__':
    ArgsParse().emails()
