lugares = ["parque", "cinema", "cafe", "trilha"]

print("---------------------------")
print(f"\t[1] - {lugares[0]}")
print(f"\t[2] - {lugares[1]}")
print(f"\t[3] - {lugares[2]}")
print(f"\t[4] - {lugares[3]}")
print("---------------------------")

lugar = int(input("Insira para onde você deseja ir:\n>> "))
lugar -= 1
chuva = input("\nEsta chovendo? (S/N)\n>> ")

if(lugares[lugar] == lugares[0] and chuva.lower() == "s"):
    print("É melhor não ir...")
elif(lugares[lugar] == lugares[3] and chuva.lower() == "s"):
    print("É melhor não ir...")
else:
    print("Pode ir tranquilo :)")