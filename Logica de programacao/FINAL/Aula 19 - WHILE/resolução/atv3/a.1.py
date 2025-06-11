from lib import get_data, generate

def is_connected(relations,a,b):
    way = [a]

    while (way != []) and (way[-1] != b):
        if relations[way[-1]] == []:
            way.pop()
            continue

        next = relations[way[len(way)-1]][0]
        relations[way[-1]].remove(next)
        way.append(next)

    return b in way

entidades = get_data('./data.txt')
print(is_connected(entidades, '3','3'))

