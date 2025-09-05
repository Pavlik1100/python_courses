"""

    создать список кортежей на основании переменных colors и sizes по декартову произведению

    colors = ['red', 'green']
    sizes = ['S', 'M', 'L']

    [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L')]

"""

colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']

list_t = [(i,j) for i in colors for j in sizes]
print(list_t)