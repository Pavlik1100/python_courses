'''

    указать в словаре позиции каждой буквы

'''

s = 'котик'

letters = {}

for i in range(len(s)):
    letters.setdefault(s[i], []).append(i)

print(letters)    
