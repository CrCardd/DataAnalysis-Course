



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
    '</div><section>section sction section </section>',
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

LINHAS = []
# WITH OPEN arq
crocOpen = False
stylOpen = False
scptOpen = False
for line in arq:
    
    new_line = []
    line = line.split()
    for word in line:  
            
        if not stylOpen:
            stylOpen = word == '<style>'
        if stylOpen and word =='</style>':
            stylOpen = False
        if stylOpen or '</style>' in word:
            word = ''
            
        if not scptOpen:
            scptOpen = word == '<script>'
        if scptOpen and word =='</script>':
            scptOpen = False
        if scptOpen or '</script>' in word:
            word = ''
            
        if not crocOpen:
            crocOpen = '<' in word 
        if crocOpen and '>' in word:
            crocOpen = False
        if crocOpen or '>' in word:
            word = ''
            
            
        if len(word) > 0:
            new_line.append(word)
        
    if len(new_line) > 0:
        LINHAS.append(' '.join(new_line))
        
        

for _ in LINHAS:
    print(_)
    
        
    























