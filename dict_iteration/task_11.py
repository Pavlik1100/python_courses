"""

    Напишите программу, которая принимает словарь, где ключами являются строки, 
    а значениями — числа. Необходимо создать "зеркальный" словарь, где ключами будут значения из исходного словаря, 
    а значениями — строки, упорядоченные лексикографически. Если одно и то же число встречается у нескольких строк, объедините их в список.

"""

# data = {'apple': 5, 'banana': 3, 'cherry': 5, 'date': 2}
# data = {'milk': 50, 'bread': 40, 'cheese': 50, 'butter': 70, 'eggs': 40}

data = {'Inception': 2010, 'Interstellar': 2014, 'The Prestige': 2006, 'Dunkirk': 2017, 'Tenet': 2020}

letters = {}

for key, value in data.items():
    letters.setdefault(value, []).append(key)
    
for value in letters.values():
    value.sort()

print(letters)   
