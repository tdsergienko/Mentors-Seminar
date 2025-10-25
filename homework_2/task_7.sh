#!/bin/bash

# Создайте alias для команды ls -la и назовите его ll. 
# Напишите команду, чтобы сделать alias постоянным, и объясните, где она должна быть добавлена. 
# Продемонстрируйте использование автодополнения на примере команды cd.

# Я сделаю alias lll вместо ll, тк ll у меня уже есть в системе
alias lll='ls -la'

# Работа со скриптом
# $ source homework_2/task_7.sh 
# tikhon@tikhon:~/Study/HSE/Mentors-Seminar$ lll
# total 20
# drwxrwxr-x 4 tikhon tikhon 4096 окт 25 14:27 .
# drwxrwxr-x 6 tikhon tikhon 4096 окт 18 14:02 ..
# drwxrwxr-x 8 tikhon tikhon 4096 окт 25 14:32 .git
# drwxrwxr-x 2 tikhon tikhon 4096 окт 25 14:34 homework_2
# -rw-rw-r-- 1 tikhon tikhon  125 окт 18 14:03 README.md

# Чтобы сделать alias постоянным, нужно добавить команду 
# `alias lll='ls -la'` в ~/.bashrc 
# затем котрыть новый терминал либо выполнить `source ~/.bashrc` в текущем

# `cd /h` дополняется до `cd /home/`