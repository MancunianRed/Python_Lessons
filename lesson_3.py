#  Типы данных int, str: Задание 1 20 баллов
language = "Языки программирования: Pyp, Python, Goland, Jaba…"
print(language.replace("Языки программирования: Pyp, Python, Goland, Jaba…",
                       "Языки программирования: PHP, PYTHON, GOLANG, JAVA."))

#  Задание 2 25 баллов
x = 1000/3 + 100/3 + 10/3
print(round(1000/3) + round(100/3) + round(10/3))
print(round(x, 1))
print(round(1000/3) + round(100/3) + round(10/3, 7))

#  Задание 3 20 баллов
print('x=1,', str(bin(1)) + ',', str(hex(1)) + ',', str(oct(1)))
print('y=120,', str(bin(120)) + ',', str(hex(120)) + ',', str(oct(120)))
print('z=100000,', str(bin(100000)) + ',', str(hex(100000)) + ',',
      str(oct(100000)))

#  Задание 4 25 баллов
print('ворон', 'ворон'[::-1], 'ворон'[::-1] == 'ворон')
print('киноник', 'киноник'[::-1], 'киноник'[::-1] == 'киноник')
print('ротатор', 'ротатор'[::-1], 'ротатор'[::-1] == 'ротатор')
print('город', 'город'[::-1], 'город'[::-1] == 'город')
print('тартрат', 'тартрат'[::-1], 'тартрат'[::-1] == 'тартрат')

#  Задание 5* 50 баллов
print('города - масква, лондон, париж, берлин...'[0:-2]
      .replace('масква', 'мoсква').title())

#  Задание 6 60 баллов
history = 'История Python, одного из самых простых языков программирования, ' \
          'началась в 1989 году.'
print(history[32:36] + history[2:5])
print(history[47:50] + history[1:5])
print(history[32:37] + history[-29: -31: -1])
print(history[47:48] + history[33:36] + history[2:3] + history[-4:-31:-26])

#  Задание 7 100 баллов
tool = 'Super-Puper MainTool /v2*'
print(tool[-1]*20)
print(tool.replace('-Puper Main', '').replace(' /v2*', ' v1').center(20, '-'))
print(tool[-1]*20)

#  Задание 8* 100 баллов
#  Небольшой комментарий. Я понимаю что задание со * необходимо сделать в
#  одну строку. То есть в моем случае без обьявления переменных. Но тогда код
#  в строке print будет очень сложно читаться. Однако если все же мое решение
#  не подходит, решается эта задача просто, вместо переменных нужно
#  подставить требуемые строки из условия. Но тогда необходимо соблюдать
#  правило PEP про 79 символов в одной строке
a = 'четырёхсотпятидесятисемимиллиметровое'
b = 'метоксихлордиэтиламинометилбутиламиноакридин'
c = 'автомотовелофототелерадиомонтёр'
d = 'автоэлектростеклоподъемники'
print(a, a[0], a[-1], a.count(a[0]) + a.count(a[-1]), "\n" + b, b[0], b[-1],
      b.count(b[0]) + b.count(b[-1]), '\n' + c, c[0], c[-1], c.count(c[0]) +
        c.count(c[-1]), '\n' + d, d[0], d[-1], d.count(d[0]) + d.count(d[-1]))

#  Задание 9* 120 баллов
print("5qwerty", '=>', int("5qwerty"[0])*("5qwerty"[1]) + "5qwerty"[2:], '\n' +
      "3python", '=>', int("3python"[0])*("3python"[1]) + "3python"[2:], '\n' +
      "9calendar", '=>', int("9calendar"[0])*("9calendar"[1]) +
      "9calendar"[2:])

#  Задание 10**
print('змееед'.count('е')*'змееед ', '\n' + 'припев'.count('е')*'припев ',
      '\n' + 'перепёлка'.count('е')*'перепёлка ', '\n' + 'переезд'.count(
    'е')*'переезд ')

