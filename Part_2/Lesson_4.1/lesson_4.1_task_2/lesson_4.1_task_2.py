#  Регулярные выражения: Задание 2 - 40 баллов
import re

text = '''Примеры расширений файлов: 
            wald.jpeg 
            wow.mp4 
            book.txt 
            forest.png 
            fox.tiff 
            wood.pdf 
            hub.gif 
            small.zip 
            sound.mp3 '''
res = re.findall(r'\w+\.jpeg|\w+\.png|\w+\.gif|\w+\.tiff', text)
for pics in res:
    print(''.join(pics))

