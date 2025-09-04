"""

    Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.

    Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO

"""
# abracadabra
# cadabraabra

s1, s2 = 'abracadabra', 'cadabraabra'
d1 = {}
d2 = {}

for c in s1:
    if c in d1:
        d1[c] += 1
    else:
        d1[c] = 1

for c in s2:
    if c in d2:
        d2[c] += 1
    else:
        d2[c] = 1

if d1 == d2:
    print('YES')
else:
    print('NO')    
      