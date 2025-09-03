"""

    составить фразу расставив буквы из ключей по позициям значений

"""
#letters = {'a': [0, 3, 5, 7, 10], 'b': [1, 8], 'r': [2, 9], 'c': [4], 'd': [6]}
#letters = {'к': [0, 4], 'о': [1], 'т': [2], 'и': [3]}

letters = {
            'h': [0],
            'e': [1],
            'l': [2, 3, 9],
            'o': [4, 7],
            ' ': [5],
            'w': [6],
            'r': [8],
            'd': [10]
}

max_len = max([v for v_v in letters.values() for v in v_v])
final_word = [''] * (max_len + 1)

for char, pos in letters.items():
    for i in pos:
        final_word[i] = char

print(''.join(final_word))