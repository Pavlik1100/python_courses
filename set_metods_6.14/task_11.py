"""

    Напишите программу, которая удаляет из строки все повторяющиеся символы, при этом регистр букв необходимо учитывать

    

Sample Input 1:

hello_world!

Sample Output 1:

helo_wrd!

Sample Input 2:

abc312re542Ab

Sample Output 2:

abc312re54A

Sample Input 3:

123454321123

Sample Output 3:

12345

Sample Input 4:

qqqqqqqqqqqqqqq

Sample Output 4:

q


    
"""

st = input()
sp = set(st)

for i in st:
    if i in sp:
        print(i, end='')
        sp.remove(i)

# s = [i for i in input()]
# a = set(s)
# print(s, a)