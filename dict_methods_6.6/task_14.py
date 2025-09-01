'''
    На вход подается город, определить к какой из стран в словаре он принадлежит

'''

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()

for c in countries.items():     # .items() возвращает все пары «ключ-значение» словаря в виде коллекции кортежей
    if city in c[1]:
        print(f'INFO: {city} is a city in {c[0]}')
        break
else:
    print(f'ERROR: Country for {city} not found')    