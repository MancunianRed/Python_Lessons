#  Классы и ООП часть 2: Задание 1 - 25 баллов
class Movies:
    def __init__(self, title, name, surname):
        if title.strip(' ').count(' ') > 1:
            print('Название фильма должно состоять из одного-двух слов')
        else:
            self.title = title
            self.name = name
            self.surname = surname
            print(f'{self.title} - в главной роли {self.name} {self.surname}')


class MoviesRu(Movies):
    pass


if __name__ == '__main__':
    Movies('Хищник', 'Арнольд', 'Шварценеггер')
    Movies('Красная жара', 'Арнольд', 'Шварценеггер')
    Movies('Кобра', 'Сильвестр', 'Сталоне')
    Movies('Один дома', 'Макалей', 'Калкин')
    Movies('Голый пистолет', 'Лесли', 'Нильсен')
    MoviesRu('Кавказская пленница', 'Александр', 'Демьяненко')
    MoviesRu('Бриллиантовая рука', 'Юрий', 'Никулин')
    MoviesRu('Гений', 'Александр', 'Абдулов')
    MoviesRu('Карнавальная ночь', 'Людмила', 'Гурченко')
    MoviesRu('Спортлото-82', 'Михаил', 'Пуговкин')
