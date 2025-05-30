
print("=-=-=-=-=-=-=-=-=-=-=")
print("\tNoite de jogos!")
print("=-=-=-=-=-=-=-=-=-=-=")

leonardo = False

snape = input("snape vai? (S/N)").lower() == "s"
lawliet = input("lawliet vai? (S/N)").lower() == "s"
otavio = input("otavio vai? (S/N)").lower() == "s"
renan = input("renan vai? (S/N)").lower() == "s"
mateus = input("mateus vai? (S/N").lower() == "s"

if(mateus):
    leonardo = False

if(otavio or lawliet):
    leonardo = True

if(not renan and not snape):
    leonardo = True



