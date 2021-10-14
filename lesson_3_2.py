#  Типы данных - tuple, dictionary, set, none: Задание 1 - 20 баллов
vuln = ('XSS', 'SQL', 'CRLF', 'RCE', 'LFI')
print(', '.join(sorted(vuln)))


#  Типы данных - tuple, dictionary, set, none: Задание 2 - 30 баллов
print(set('моршак'))

#  Типы данных - tuple, dictionary, set, none: Задание 3 - 50 баллов
alles = ('__init__', '127.0.0.1', 'admin', 'SupermAn', 'ClOwN',
         'http://site.com', 'humorist', 'https://example.com', '192.168.12.101',
         12345, 'https://yandex.ru')

alles = alles[0:-2]
alles = sorted(alles)
alles_ip_password = sorted(alles)[0:4]
alles_login_host = sorted(sorted(alles)[4:9], key=len)
print('Login:', alles_login_host[0], alles_login_host[1], alles_login_host[2],
      sep='\n')
print('Password:', alles_ip_password[2], alles_ip_password[3], sep='\n')
print('IP:', alles_ip_password[0], alles_ip_password[1], sep='\n')
print('Host:', alles_login_host[-1], alles_login_host[-2], sep='\n')


#  Типы данных - tuple, dictionary, set, none: Задание 4 - 50 баллов
access = {'admin': 'megapass', 'mazhor': 'goldkey777', 'chuvak': 'all_good',
          'lelik': 'bablo_forever', 'invisible_man': 'a1dfvb5415vD',
          'LOL': 12345}
print('\n'.join(str(access)[1:-1].split(", ")).replace('\'', ''))




#  Типы данных - tuple, dictionary, set, none: Задание 5 - 70 баллов
x = {'sqlmap', 'IronWASP', 'Burp Suite', 'Nikto', 'ATSCAN', 'BruteXSS', 'WFUZZ'}
print(str(sorted(x, reverse=True))[1:-1])


#  Типы данных - tuple, dictionary, set, none: Задание 6 - 100 баллов
my_dict = {'o': 0, 'b': 1, 'k': 2, 'd': 3, 'e': 4, 'f': 5, 'y': 6}
print(''.join(my_dict.keys())[::2])


#  Типы данных - tuple, dictionary, set, none: Задание 7 - 120 баллов
target_dict = {'d': 3, 'o': 9, 'j': 8, 'c': 2, 'x': 6, 'g': 1, 'm': 4, 'z': 0,
               'k': 5, 'q': 7}

print('Сумма значений словаря:', sum(target_dict.values()))
print('Отсортированный список значений словаря:',
      sorted(list(target_dict.values()), reverse=True))
print('Сумма третьих значений словаря:', sum(list(target_dict.values())[::3]))


#  Типы данных - tuple, dictionary, set, none: Задание 8 - 150 баллов
my_dict = {1: ("ладошка", "лошадка"), 2: ("сушилка", "подмена"),
3: ("вязанка", "навязка"), 4: ("каторга", "рогатка"),
5: ("плесень", "полдник")}

print(*my_dict[1], set(my_dict.get(1)[0]) == set(my_dict.get(1)[1]))
print(*my_dict[2], set(my_dict.get(2)[0]) == set(my_dict.get(2)[1]))
print(*my_dict[3], set(my_dict.get(3)[0]) == set(my_dict.get(3)[1]))
print(*my_dict[4], set(my_dict.get(4)[0]) == set(my_dict.get(4)[1]))
print(*my_dict[5], set(my_dict.get(5)[0]) == set(my_dict.get(5)[1]))



