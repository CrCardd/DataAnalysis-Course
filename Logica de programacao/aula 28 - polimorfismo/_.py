from math import pi

class PoligonoRegular():
    def __init__(self):
        pass

    def get_area(self):
        pass
    
    def get_perimetro(self):
        pass

class Triangulo(PoligonoRegular):
    def __init__(self, a, b, c):
        self._lado_a = a
        self._lado_b = b
        self._lado_c = c

    def get_area(self):
        # FORMULA DE HERON
        s = (self._lado_a + self._lado_b + self._lado_c) / 2
        return (s*(s-self._lado_a)*(s-self._lado_b)*(s-self._lado_c)) ** 0.5
    
    def get_perimetro(self):
        return self._lado_a + self._lado_b + self._lado_c

class Retangulo(PoligonoRegular):
    def __init__(self, a, b):
        self._lado_a = a
        self._lado_b = b

    def get_area(self):
        return self._lado_a * self._lado_b
    
    def get_perimetro(self):
        return 2*self._lado_a + 2*self._lado_b

class Circulo(PoligonoRegular):
    def __init__(self, raio):
        self._raio = raio
    
    def get_area(self):
        return pi*(self._raio**2)

    def get_perimetro(self):
        return 2*pi*self._raio
    

t = Triangulo(3,4,5)
c = Circulo(1)
q = Retangulo(4,5)

print(t.get_area())
print(c.get_area())
print(q.get_area())