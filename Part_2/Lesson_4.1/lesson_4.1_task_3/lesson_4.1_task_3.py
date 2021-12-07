#  Регулярные выражения: Задание 3 - 130 баллов
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

res = re.findall(r'\w+\.jpeg|\w+\.png|\w+\.tiff|\w+\.gif', text)
for file in res:
    print(file)