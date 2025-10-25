#!/bin/bash

# Напишите Bash-скрипт, который выполняет следующие действия:
#    1. Создаёт список всех файлов в текущей директории, указывая их тип (файл, каталог и т.д.).
#    2. Проверяет наличие определённого файла, переданного как аргумент скрипта, и выводит сообщение о его наличии или отсутствии.
#    3. Использует цикл for для вывода информации о каждом файле: его имя и права доступа.

file=$1

echo "1. Cписок всех файлов в текущей директории и их тип"
for item in *; do
    if [ -L "$item" ]; then
        echo "$item symbolic link"
    elif [ -d "$item" ]; then
        echo "$item directory"
    elif [ -f "$item" ]; then
        echo "$item file"
    else
        echo "$item unknown"
    fi
done

echo

echo "2. Проверка наличия файла $file"
if [ -e "$file" ]; then
    echo "Файл $file существует"
else
    echo "Файл $file не существует"
fi

echo

echo "3. Информации о каждом файле"
for item in *; do
    if [ -f "$item" ]; then
        permissions=$(ls -l "$item" | cut -f 1 -d " ")
        echo "$item $permissions"
    fi
done

# Пример работы скрипта
# $ /home/tikhon/Study/HSE/Mentors-Seminar/homework_2/task_1.sh Makefile
# 1. Cписок всех файлов в текущей директории и их тип
# binaries directory
# blockcheck.sh file
# common directory
# config file
# config.default file
# config_link symbolic link
# docs directory
# files directory
# init.d directory
# install_bin.sh file
# install_easy.sh file
# install_prereq.sh file
# ip2net directory
# ipset directory
# Makefile file
# mdig directory
# nfq directory
# tmp directory
# tpws directory
# uninstall_easy.sh file

# 2. Проверка наличия файла Makefile
# Файл Makefile существует

# 3. Информации о каждом файле
# blockcheck.sh -rwxrwxr-x
# config -rw-rw-r--
# config.default -rw-rw-r--
# config_link lrwxrwxrwx
# install_bin.sh -rwxrwxr-x
# install_easy.sh -rwxrwxr-x
# install_prereq.sh -rwxrwxr-x
# Makefile -rw-rw-r--
# uninstall_easy.sh -rwxrwxr-x
