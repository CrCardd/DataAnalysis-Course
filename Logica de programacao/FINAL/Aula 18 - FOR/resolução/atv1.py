lista = []
count = 0
for i in range(10):
    num = int(input("--> "))
    lista.append(num)
    
numero = int(input("Numero --> "))

for i in lista: 
    if i < numero: 
        count += 1
    
print(f'Dentre os numeros digitados, {count} são menor do que {numero}!')