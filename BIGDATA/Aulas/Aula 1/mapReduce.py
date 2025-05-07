def map_function(l, cond = lambda p: p==p):
    r = [(p['nome'], 1) if cond(p) else None for p in l]
    return [_ for _ in r if _ is not None]

def shuffle_function(l):
    g = {}
    for w, c in l:
        if w in g:
            g[w].append(c)
        else:
            g[w] = [c]
    return g

def reduce_function(l):
    d = shuffle_function(l)
    return {w : sum(d[w]) for w in d}



pacientes = [
    {'nome': 'João', 'idade': 13},
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Pedro', 'idade': 13},
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Lucas', 'idade': 13}
]

mapped = map_function(pacientes, lambda p: p['idade'] == 13)
reduced = reduce_function(mapped)
print(reduced)



