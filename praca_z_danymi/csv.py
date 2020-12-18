def menu():
    print("####MENU####")
    print(''''1 - Dodaj nowy samochów")
            2 - Usuń samochód")
            3 - Wyjście z zapisem''')
    return int(input("Podaj odpowiedz"))


def show_data(position, name, engine, navi):
    for i in range(0, len(position)):
        print("|", position[i], "|", name[i], "|", engine[i], "|", navi[i])


def delete_car(i):
    del name[i]
    del engine[i]
    del navi[i]
    position.pop()


def add_car():
    position.append(str(len(position)))
    name.append(str(input("Podaj markę i model auta: ")))
    engine.append(str(input("Podaj pojemonść silnika: ")))
    navi.append(str(input("Podaj czy jest nawigacja: ")))


position = []
name = []
engine = []
navi = []

with open("cars_1.csv", "r") as file:
    lines = file.readlines()
    for i in lines:
        position.append(i.split(",")[0])
        name.append(i.split(",")[1])
        engine.append(i.split(",")[2])
        navi.append(i.split(",")[3].strip("\n"))
    file.close()

while 1:
    show_data(position, name, engine, navi)

    a = menu()
    if a == 1:
         add_car()
    elif a == 2:
        pos = int(input("Podaj pozycję: "))
        delete_car(pos)
    elif a == 3:
        print("Zakończono program i zapisano bazę danych")
        break
    else:
        print("Wybrana opcja nie istnieje, spróbuj ponownie")

new_data_row = []
for i in range(0, len(position)):
    new_data_row.append(position[i] + "," + name[i] + "," + engine[i] + "," + navi[i])

new_data = "\n".join(new_data_row)

with open("cars_1.csv", "w") as file:
    file.write(new_data)
    file.close()
