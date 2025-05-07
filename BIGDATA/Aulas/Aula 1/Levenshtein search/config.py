import random as rd

words = [
    'jarro','barracao', 'javaehbom','jardinagem','pepita','ouro','precipicio','preda','pedida','maluco',
    'peppita', 'pepitte', 'pepited', 'brownie', 'nozes', 'naorolanao', 'oloco'
]

for _ in range(1, 11):
    with open(f".\\data\\{_}.txt", "w") as file:
        for v in range(10):
            file.write(f'{words[rd.randint(0, len(words)-1)]}\n')