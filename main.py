def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        return "Napaka: deljenje z 0 ni dovoljeno!"
    return a / b


zgodovina = []

print("Pozdrav! Mini kalkulator")
print("1 = seštevanje")
print("2 = odštevanje")
print("3 = množenje")
print("4 = deljenje")
print("0 = izhod")

izbira = input("Kaj želiš narediti? (0, 1, 2, 3 ali 4): ")

if izbira == "0":
    print("Program se zapira. Nasvidenje!")

elif izbira in ["1", "2", "3", "4"]:
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))

    if izbira == "1":
        rezultat = sestej(x, y)
        zapis = f"{x} + {y} = {rezultat}"

    elif izbira == "2":
        rezultat = odstej(x, y)
        zapis = f"{x} - {y} = {rezultat}"

    elif izbira == "3":
        rezultat = pomnozi(x, y)
        zapis = f"{x} × {y} = {rezultat}"

    elif izbira == "4":
        rezultat = deli(x, y)
        zapis = f"{x} ÷ {y} = {rezultat}"

    print(f"\n{zapis}")

    zgodovina.append(zapis)

    if len(zgodovina) > 3:
        zgodovina.pop(0)

    print("\nZadnji izračuni:")
    for z in zgodovina:
        print(z)

else:
    print("Neveljavna izbira!")
