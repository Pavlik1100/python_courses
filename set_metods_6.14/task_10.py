"""

    Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

"""

s = input()
g = set()
for c in s:
    if s.count(c)>1 and c.isdigit():
        g.add(c)

if g:
    for c in sorted(g):
        print(c, end = ' ')
else:
    print('NO')        