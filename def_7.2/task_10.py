"""

    Написать функцию count_letter(text, letter), которая принимает два параметра:

        -text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
     
        -letter – буква, количество которой мы должны посчитать в text.

    Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text

"""

def count_letter(text, letter):

    print(text.count(letter))

count_letter(input('Ввведите строку - '), input('введите букву - '))