import re
import os


SEARCH = 'data'

folder_data = "./WikipediaTI"
list_data = os.listdir(folder_data)
metric = len(SEARCH)/2
best_len = 20


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
            p3 = tab[x-1][y-1] + (0 if str1[x-1].lower() == str2[y-1].lower() else 1)
            tab[x][y] = min(p1,p2,p3)

    return tab[s1-1][s2-1]


def process(data):
    scores = []
    for archive in data:
        with open(f'{folder_data}/{archive}', 'r', encoding='utf-8') as arq:
            content = arq.read()
        content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<.*?>', '', content, flags=re.DOTALL)
        lines = content.splitlines()

        
        score = 0
        scored = False
        for line in lines:
            if line.strip() == '':
                continue

            line = line.split(' ')
            for word in line:
                word = word.strip()
                points = levenshteinDistance(SEARCH, word)
                if points <= metric:
                    scored = True
                    points = len(SEARCH) - points / len(SEARCH)
                    score += points
        if scored:
            score = round(score/len(lines) * 100, 2) 
            scores.append((archive, score))

        print(archive)

    sorted_values = sorted(scores, key=lambda item: item[1], reverse=True)
    bests = sorted_values[:best_len]
    return bests



results = process(list_data)
sorted_values = sorted(results, key=lambda item: item[1], reverse=True)
with open('result_simple.txt', 'w', encoding='utf-8') as result:
    for score in sorted_values:
        result.write(f'{score[0].replace(' - Wikipedia.html', '')} \t : {score[1]}\n')