def levenshteinDistance(str1, str2):
    s1 = len(str1) + 1
    s2 = len(str2) + 1
    tab = [[0 for _ in range (s2)] for _ in range(s1)]
    for x in range(s1):
        tab[x][0] = x
    for y in range(s2):
        tab[0][y] = y

    for x in range(1,s1):
        for y in range(1, s2):
            p1 = tab[x][y-1] + 1
            p2 = tab[x-1][y] + 1
            p3 = tab[x-1][y-1] + (0 if str1[x-1] == str2[y-1] else 1)
            tab[x][y] = min(p1,p2,p3)
        
    return tab[s1-1][s2-1]




search = 'pepita'
metric = len(search)/2
scores = []
for _ in range (1,11):
    with open(f'.\\data\\{_}.txt', 'r') as arq:
        scored = False
        score = 0
        for line in arq:
            line = line.strip('\n')
            points = levenshteinDistance(search, line)
            if points <= metric:
                scored = True
                score += points
        if scored:
            scores.append((f'{_}.txt', score))



sorted_values = sorted(scores, key=lambda item: item[1])
best_five = sorted_values[:5]
print(best_five)





            
    