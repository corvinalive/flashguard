#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       flashguard.py
#       
#       Copyright 2011 Zonov Valerij <corvinalive@yandex.ru>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

#
# Проект flashguard
# Цель - слежение за состоянием файлов на флешке
# Задачи:
# 1. Создать список файлов с контрольными суммами
# 2. При проверки/бэкапе флешки показывать изменившиеся файлы. Если файл
#    не должен был измениться, то восстановить его
# 3. Доп. функция - поиск дублей по контрольным суммам
#


import optparse


usage = u"Мониторинг за целостностью файлов на флешке.\nИспользование: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-i", "--ini-file", dest="ini_file", help=u"Имя ini-файла")
parser.add_option("-o", "--output-file", dest="output_file", help=u"Имя выходного файла")

(options, args) = parser.parse_args()

#if len(args) < 1:
#	parser.error(u"Недостаточно аргументов. Задайте имя dso-файла для распаковки в текстовый файл. Запустите с ключем -h для справки")




# Функция generate_file_list
# создает список файлов и их контрольные суммы
#

#def generate_file_list ():


def main():
	
	return 0

if __name__ == '__main__':
	main()

