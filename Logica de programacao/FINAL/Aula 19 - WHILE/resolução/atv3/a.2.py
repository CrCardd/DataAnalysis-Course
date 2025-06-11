from lib import get_data

def is_connected(relations,a,b):
    way = [a]

    if relations[a] != []:
        way.append(relations[a][0])
        relations[a].remove(relations[a][0])

    while (way != []) and (way[-1] != b or len(way) == 1):
        if relations[way[-1]] == []:
            way.pop()
            continue

        next = relations[way[len(way)-1]][0]
        relations[way[-1]].remove(next)
        way.append(next)

    return b in way

# entidades = get_data('./data.txt')
# print(is_connected(entidades, '6','4'))

