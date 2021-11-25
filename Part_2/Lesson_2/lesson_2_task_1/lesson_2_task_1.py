#  Модуль OS: Задание 1 - 20 баллов
import os
import stat

codes = {0: '---', 1: '--x', 2: '-w-', 3: '-wx', 4: 'r--', 5: 'r-x', 6: 'rw-', 7: 'rwx'}
current_directory_permission = oct(stat.S_IMODE(os.lstat(os.getcwd()).st_mode))[2:]
print(current_directory_permission)
print('Права текущей дериктории:')
for i in range(3):
    print(codes.get(int(current_directory_permission[i])), end='')
