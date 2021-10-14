# задание 1
print('target_bots_qnt ', 'bots_qnt ', 'bots ',
      'my_answer ', 'answer ', 'input_data')


#  задание 2
#  2.1 Лишняя запятая после  val_6
val_1, val_2, val_3, val_4, val_5, val_6, = "python", "java", "cpp", \
                                            "golang", "fortrain", "basic"
#  2.2 Значение True имеет тип bool. Синтаксическая ошибка
input_value = 'python'

#  2.3 пробел до и после var_1
var_1 = 3
var_2 = 5
print(var_1, var_2)
#  2.4 пропуск пробела после +=, пропус пробелов вокруг > лишний пробел после
#  print. Необьявлена переменная var_1
var_2 = 0
var_2 += 1
print(var_1 > var_2)
#  2.5 пропуск одного пробела перед # и после нее
var_3 = 5

#  задание 3
bots_total = 1000
bots_without_add = bots_total - 30 * 2
bots_add_3 = bots_without_add + 30 * 3
print(bots_add_3, bots_without_add)

#  задание 4
leg_1, leg_2 = 4, 3
hypotenuse = ((leg_1 ** 2 + leg_2 ** 2) ** 0.5) + 3
print('всего необходимо ', hypotenuse, ' метров веревки')

#  задание 5
yura_house = 7 * 9
alex_house = (3.14 * (9 ** 2)) / 4
vlad_house = (6 * 9) + (6 * 2)
print('Дом Юрия самый маленький -',
      yura_house < alex_house and yura_house < vlad_house)

#  задание 6
total_distance = ((30 * 60) * 10) / 1000
total_hours = (total_distance / 4) - 2
print('осталось идти ', total_hours, ' часа')

#  задание 7
total_amount = 11000 * 4
cash = total_amount - (total_amount * 0.4 + 11000)
print('У Пети осталось ', cash)

#  задание 8
print(((60-(14+16))/5) ** (22-19))

#  задание 9
print('fanat > apple', 'fanat' > 'apple')
print('fanat > abracadabra', 'fanat' > 'abracadabra')
print('fanat > Tarantino', 'fanat' > 'Tarantino')
print('fanat > yahoo', 'fanat' > 'yahoo')
print('yahoo > yandex', 'yahoo' > 'yandex')
print('yandex > gool', 'yandex' > 'gool')
print('yandex > logo', 'yandex' > 'logo')
