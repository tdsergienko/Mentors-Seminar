#!/bin/bash

# Создайте скрипт, который выполняет следующие действия:
#     1. Читает данные из файла input.txt.
#     2. Перенаправляет вывод команды wc -l (подсчет строк) в файл output.txt.
#     3. Перенаправляет ошибки выполнения команды ls для несуществующего файла в файл error.log.

# п.1 и п.2
cat input.txt | wc -l > output.txt

# п.3 
ls 29bbe.txt 2> error.log

echo "Содержимое input.txt:"
cat input.txt

echo
echo "Содержимое output.txt:"
cat output.txt

echo
echo "Содержимое error.log:"
cat error.log

# Примеры работы скрипта

# $ /home/tikhon/Study/HSE/Mentors-Seminar/homework_2/task_6.sh
# Содержимое input.txt:
# 1
# 2
# 3
# 4
# 5

# Содержимое output.txt:
# 5

# Содержимое error.log:
# ls: cannot access '29bbe.txt': No such file or directory
