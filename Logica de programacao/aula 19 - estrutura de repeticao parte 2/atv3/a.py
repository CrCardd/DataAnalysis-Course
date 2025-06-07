from lib import get_data, generate

def connect(relations,a,b):
    crr = a
    last = a
    way = [crr]

    while (relations[a]!= ['']) and (not b in relations[crr]):
        if relations[crr] == ['']:
            crr = last
            way.pop()
            continue

        last = crr
        crr = relations[crr][0]
        relations[last] = relations[last].remove(crr)
        way.append(crr)
    
    print(way)
    return b in relations[crr]


# entidades = get_data('./data.txt')
# result = connect(entidades, '5','3')
# print(result)
