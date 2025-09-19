"""

    Создать функцию с именем say_hello_world, которая принимает на вход имя человека в виде строки и печатает фразу «{name} говорит hello world!»

"""

def say_hello_world(name):
    print(f'{name} говорит hello world!')

say_hello_world(input('Ввведите имя '))    