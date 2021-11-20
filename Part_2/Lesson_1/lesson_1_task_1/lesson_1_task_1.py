#  Аргументы: Задание 1 - 30 баллов
import argparse


class FileReaderWriter:
    def __init__(self, domain):
        self.domain = domain
        self.list_emails_1 = list()

    def file_reader(self, target_file="base.txt"):
        with open(target_file, encoding="utf-8") as reader:
            return reader.readlines()

    def filter(self):
        for email in self.file_reader():
            if self.domain == email[email.find(':') -
                                    len(self.domain): email.find(':')]:
                self.list_emails_1.append(email.strip())
        return self.list_emails_1

    def write(self):
        with open(f"email_{self.domain}.txt", "w", encoding="utf-8") as writer:
            for email in self.filter():
                writer.write(email + '\n')


parser = argparse.ArgumentParser(description='parsing emails')
parser.add_argument('domain', type=str, help='email`s domain')
args = parser.parse_args()


def emails():
    FileReaderWriter(args.domain).write()
    print(' Done!')


if __name__ == '__main__':
    emails()

