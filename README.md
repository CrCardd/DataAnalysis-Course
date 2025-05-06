```

import re



arq = [
    'bla bla bla bla bla bla bla bla bla bla bla bla',
    'bla bla bla bla bla bla bla bla bla bla bla bla',
    'bla bla bla bla bla bla bla bla bla bla bla bla',
    'bla bla bla bla bla bla bla bla bla bla bla bla',
    '',
    'DIV ESQUISITA',
    '<div',
    'd',
    'd',
    'd',
    '>',
    '</div>',
    'DIV ESQUISITA',
    'STYLE FERROU',
    '<style>',
    's',
    's',
    's',
    '</style>',
    'STYLE FERROU',
    'SCRIPT CARAMBA',
    '<script>',
    's',
    's',
    's',
    '</script>',
    'SCRIPT CARAMBA',
    '',
    'bla bla bla bla bla bla bla bla bla bla bla bla',
    'bla bla bla bla bla bla bla bla bla bla bla bla',
    'bla bla bla bla bla bla bla bla bla bla bla bla',
    'bla bla bla bla bla bla bla bla bla bla bla bla',
]

with open ('test.html', 'r', encoding='utf-8') as arq
    LINHAS = []
    crocOpen = False
    stylOpen = False
    scptOpen = False
    for line in arq:
        LINHAS.extend(line)
        LINHAS.append('-=0=-')
    LINHAS = ''.join(LINHAS)
        
    LINHAS = re.sub('<style>.*?</style>', '', LINHAS)
    LINHAS = re.sub('<script>.*?</script>', '', LINHAS)
    LINHAS = re.sub('<.*?>', '', LINHAS)
    
    LINHAS = LINHAS.split('-=0=-')
    
with open('final.txt', 'a', encoding='utf8') as final:
    for _ in LINHAS:
        final.write(_)







```













