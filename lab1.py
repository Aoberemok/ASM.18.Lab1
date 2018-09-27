import st00.main
import st04.main
import st06.main
import st10.main
import st34.main
import st41.main
import st26.main
import st23.main
import st08.main
import st33.main
import st28.main
import st45.main
import st19.main
import st29.main

#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main

MENU = [
        ["[00] Образец", st00.main.main],
	["[04] Василевский", st04.main.main],
        ["[06] Василюк", st06.main.main],
		["[10] Гордиенко", st10.main.main],
        ["[34] Сурков", st34.main.main],
        ["[41] Шнякин", st41.main.main],
        ["[28] Рамазанов", st28.main.main],
    ["[26] Печенкин", st26.main.main_menu],
	["[23] Машуров", st23.main.main],
	["[08] Винокуров", st08.main.main],
	["[33] Смирнов", st33.main.main],
        ["[45] Соанху", st45.main.main],
        ["[19] Левочко", st19.main.main],
        ["[29] Редька", st29.main.main],
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]

def menu():
	print("------------------------------")
	for i, item in enumerate(MENU):
		print("{0:2}. {1}".format(i, item[0]))
	print("------------------------------")
	return int(input())

try:
	while True:
		MENU[menu()][1]()
except Exception as ex:
	print(ex, "\nbye")
