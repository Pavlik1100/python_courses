"""

    Напишите генератор словаря, где ключи — буквы английского алфавита, а значения — их порядковые номера.

"""

lowercase = 'abcdefghijklmnopqrstuvwxyz'

dig = {lowercase[i]: ord(lowercase[i])-96 for i in range(len(lowercase))}

print(dig)



