import re

with open('.\\teste.html', 'r', encoding='utf-8') as html:
    crocOpen = False
    styleOpen = False
    scriptOpen = False
    for line in html:
        line = line.strip()
        line = re.sub('<[^>]*>', '', line)
        if len(line) > 0:
            print(line)
