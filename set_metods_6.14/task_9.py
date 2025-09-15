"""

    Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, но при этом отсутствуют во втором. 
    Sample Input:

    1 3 2 5
    4 3 2 6

    Sample Output:

    1 5

"""

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

for c in sorted(s1.difference(s2)):
    print(c, end=' ')