"""

    В переменную my_frozen, сохраните объект frozenset , содержащий 77 элементов
    Сами элементы это последовательность из 77-ми следующих чисел: 7, 77, 777, 7777, 77777, 777777, ..... 


"""

my_frozen = frozenset(int(i*'7') for i in range(1, 78))
# print(sorted(my_frozen), len(my_frozen))