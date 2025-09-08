"""

    вывести на экран количество уникальных слов, длина которых больше 6.

"""


words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error', 
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government', 
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']

dig = {c for c in words if len(c)>6}
print(len(dig))