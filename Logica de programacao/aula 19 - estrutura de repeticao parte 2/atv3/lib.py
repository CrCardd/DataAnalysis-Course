import random as rd

def get_data(path):
    e = {}
    with open(path, 'r') as file:
        for line in file.readlines():
            data = line.split(':')

            name      = data[0].strip()
            relations = data[1].strip()

            relations = relations.strip('[')
            relations = relations.strip(']')
            relations = relations.split(',')

            e[name] = relations
    return e


def generate(length):
    e = {i : [] for i in range(length)}

    for i in range(length):
        relations = rd.randint(0,5)
        for _ in range(relations):
            e[i].append(rd.randint(0,length-1))
    with open('data.txt', 'w') as file:
        file.writelines('')
    with open('data.txt', 'a') as file:
        for name in e:
            file.write(f'{name} : {e[name]}\n')
        