#  Аргументы: Задание 2 - 30 баллов
import click


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
    @click.command()
    @click.argument("domain")
    def __init__(self, domain):
        self.domain = domain
        FileReaderWriter(self.domain).file_reader_writer()
        click.echo(' Done!')


if __name__ == '__main__':
    ArgsParse()
