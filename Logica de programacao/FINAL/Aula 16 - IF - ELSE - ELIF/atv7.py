#------------------------------------------------------------------------
#||                     RESPOSTA CORRETA RACHA CUCA                    ||
#------------------------------------------------------------------------
nomes  =    ["Leonardo", "Cristian", "Eduardo", "Nycollas", "Donathan"  ]
filmes =    ["Encanto",  "Barbie",   "Rocky",   "Sonic",    "O Irlandês"]
notas  =    [9,          7,          10,        3,          1           ]
idades =    [8,          15,         20,        19,         23          ]



def play():
    
    if( not (nomes.index("Eduardo") == 2)):
        return "Falhou na regra '1'"
    if( not (notas[idades.index(19)] == 3)):
        return "Falhou na regra '2'"
    if( not (notas[filmes.index("Encanto")] == 9)):
        return "Falhou na regra '3'"
    if( not (filmes[nomes.index("Cristian")] == "Barbie")):
        return "Falhou na regra '4'"
    if( not (notas[nomes.index("Eduardo")] == max(notas))):
        return "Falhou na regra '5'"
    if( not (idades.index(8) == 0 or idades.index(8) == 4)):
        return "Falhou na regra '6'"
    if( not (idades[nomes.index("Donathan")] == max(idades))):
        return "Falhou na regra '7'"
    if( not (idades[filmes.index("Encanto")] == min(idades))):
        return "Falhou na regra '8'"
    if( not (idades.index(min(idades)) < nomes.index("Nycollas"))):
        return "Falhou na regra '9'"
    if( not (filmes[nomes.index("Donathan")] != "Rocky" and filmes[nomes.index("Donathan")] != "Sonic")):
        return "Falhou na regra '10'"
    if( not (notas[nomes.index("Cristian") > notas[nomes.index("Nycollas")]] and notas[nomes.index("Cristian") < notas[nomes.index("Leonardo")]])):
        return "Falhou na regra '11'"
    if( not (idades[nomes.index("Nycollas")] > idades[nomes.index("Cristian")] and idades[nomes.index("Nycollas")] < idades[filmes.index("Rocky")])):
        return "Falhou na regra '12'"
    if( not
       (
        (nomes.index("Nycollas") > nomes.index("Eduardo") and nomes.index("Nycollas") < nomes.index("Donathan")) or 
        (nomes.index("Nycollas") > nomes.index("Donathan") and nomes.index("Nycollas") < nomes.index("Eduardo"))
       )
    ):
        return "13"

    
    return "Resposta correta !!!\n!!!!!!!!!!!!!"

print(play())

    
    