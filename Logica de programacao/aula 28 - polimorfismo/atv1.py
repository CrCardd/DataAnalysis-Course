from typing import override

def array(lista):
    return Array(lista)

class Array():

    iteracao_atual = 0
    _lista = []

    def __init__(self, E):
        if type(E) == list:
            self.tamanho = len(E)
            self._lista = [None for _ in range(self.tamanho)]
            for i in range(self.tamanho):
                if type(E[i]) == list:
                    self._lista[i] = Array(E[i])
                    continue
                self._lista[i] = E[i]
                

            return
        
        self.tamanho = E
        self._lista = [None for _ in range(E)]

    #=========================================================
    #                       Métodos
    #=========================================================
    def size(self):
        return len([i for i in self._lista if i is not None])

    def sort(self):
        if len(self) <= 1:
            return self

        # lista_none = []
        # lista = []
        # for i in range(len(self)):
        #     if self[i] != int and self[i]!=str:
        #         lista_none.append(self[i])
        #     else:
        #         lista.append(self[i])
        


        pivot = self[0]
        x = 0
        
        for y in range(1, len(self)):
            if self[y] < pivot:
                x += 1  
                self[x], self[y] = self[y], self[x]

        self[0] = self[x]
        self[x] = pivot

        left = self[:x].sort()
        right = self[x+1:].sort()
        
        return left + [pivot] + right
    


    #=========================================================
    #             Acessar por indice e iteração
    #=========================================================
    @override # array[indice]
    def __getitem__(self, key):
        if isinstance(key, slice):
            start = key.start if key.start != None else 0
            end = key.stop if key.stop != None else len(self)
            length = end - start
            sliced = Array(length)
            for i in range(length):
                sliced[i] = self[i+start]
            return sliced

        if key >= self.tamanho or key < 0:
            return None
        return self._lista[key]
    
    @override # array[indice] = X
    def __setitem__(self, index, valor):
        if index >= self.tamanho or index < 0:
            return None
        self._lista[index] = valor

    @override # len(indice)
    def __len__(self):
        return self.tamanho

    @override # for i in >>array<<
    def __iter__(self):
        self.iteracao_atual = 0
        return self
    
    @override # for >>i<< in array
    def __next__(self):
        if self.iteracao_atual >= self.tamanho:
            raise StopIteration
        valor = self._lista[self.iteracao_atual]
        self.iteracao_atual += 1
        return valor



    #=========================================================
    #                     Operações
    #=========================================================

    @override # arrayA + arrayB
    def __add__(self, outro_vetor):
        vetor = Array(len(self) + len(outro_vetor))
        index = 0
        for i in range(len(self)):
            vetor[index] = self[i]
            index += 1
        for i in range(len(outro_vetor)):
            vetor[index] = outro_vetor[i]
            index += 1
        return vetor
    
    @override # arrayA & arrayB
    def __and__(self, outro_vetor):
        lista = []
        for item in self:
            if item in outro_vetor and not item in lista:
                lista.append(item)
        return array(lista)

    @override # arrayA | arrayB
    def __or__(self, outro_vetor):
        lista = []
        for item in self:
            if item in lista:
                continue
            lista.append(item)
        for item in outro_vetor:
            if item in lista:
                continue
            lista.append(item)

        array

        return array(lista)
        


    #=========================================================
    #                Imprimir no terminal
    #=========================================================

    @override # print(array)
    def __str__(self):
        string = '{'
        for i in range(len(self)):
            string += f'{self[i]}{',' if i != len(self)-1 else ''}'
        string += '}'
        return string




A = Array([53,5,1,3,6,4,9,0,20])
B = Array([[53,5,1],3,6,4,9,[[0],20]])
C = Array([i for i in range(10)])
D = Array(10)

for i in range(5):
    D[i] = i

print(B)

# print(A)
# print(B)
# print(C)
# print(D)
# print('=================')
# print(f'len(A)    = {len(A)}')
# print(f'A+C       = {A + C}')
# print(f'A&C       = {A & C}')
# print(f'A|C       = {A | C}')
# print(f'A[:5]     = {A[:5]}')
# print(f'A[5:]     = {A[5:]}')
# print(f'A[:]      = {A[:]}')
# print(f'A.sort()  = {A.sort()}')
# print(f'C.size()  = {C.size()}')