from lib import get_data, generate

def connect(relations,a,b):
    way = [a]
    while (way != []) and (not b in way):
        if relations[way[len(way)-1]] == []:
            way.pop()
            continue

        next = relations[way[len(way)-1]][0]
        relations[way[len(way)-1]].remove(next)
        way.append(next)

    print(way)
    return b in way


entidades = get_data('./data.txt')
result = connect(entidades, '58','80')
print(result)
