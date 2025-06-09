from lib import get_data, generate

def is_connected(relations,a,b):
    way = [a]

    if relations[a] != []:
        way.append(relations[a][0])
        relations[a].remove(relations[a][0])

    while (way != []) and (way[len(way)-1] != b):
        if relations[way[len(way)-1]] == []:
            way.pop()
            continue

        next = relations[way[len(way)-1]][0]
        relations[way[len(way)-1]].remove(next)
        way.append(next)

    print(way)
    return b in way and len(way) > 1

entidades = get_data('./data.txt')
print(is_connected(entidades, '3','3'))

