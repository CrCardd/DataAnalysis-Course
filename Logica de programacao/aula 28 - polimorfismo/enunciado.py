class MinhaClasse:
    def __init__(self, dados):
        self.dados = dados

    def __getitem__(self, key):
        if isinstance(key, slice):
            print(f"Slice: start={key.start}, stop={key.stop}, step={key.step}")
            return MinhaClasse(self.dados[key])
        else:
            return self.dados[key]

    def __repr__(self):
        return f"MinhaClasse({self.dados})"


a = MinhaClasse([1,3,4,5])
print(a[:3])