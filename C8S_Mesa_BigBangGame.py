#encoding:UTF-8
import random

while True:
    aleatorio = random.randrange(0, 5)
    elijePc = ""
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print("4)Lagarto")
    print("5)Spok")
    print("6)Salir del Programa")
    opcion = int(input("Que eliges: "))

    if opcion == 1:
        eligeUsuario = "piedra"
    elif opcion == 2:
        eligeUsuario = "papel"
    elif opcion == 3:
        eligeUsuario = "tijera"
    elif opcion == 4:
        eligeUsuario = "lagarto"
    elif opcion == 5:
        eligeUsuario = "spok"
    elif opcion == 6:
        print ("Nos vemos!")
        break
    else:
        print ("Valor Invalido")
        continue

    print("Tu eliges: ", eligeUsuario)
    if aleatorio == 0:
        eligePc = "piedra"
    elif aleatorio == 1:
        eligePc = "papel"
    elif aleatorio == 2:
        eligePc = "tijera"
    elif aleatorio == 3:
        eligePc = "lagarto"
    elif aleatorio == 4:
        eligePc = "spok"
    print("PC eligio: ", eligePc)
    print("...")

    if eligeUsuario == "papel" and eligePc == "piedra":
        print("Ganaste, papel envuelve a piedra")
    elif eligeUsuario == "papel" and eligePc == "spok":
        print("Ganaste, papel desautoriza a Spok")
    elif eligeUsuario == "piedra" and eligePc == "tijera":
        print("Ganaste, piedra aplasta la tijera")
    elif eligeUsuario == "piedra" and eligePc == "lagarto":
        print("Ganaste, piedra aplasta lagarto")
    elif eligeUsuario == "tijera" and eligePc == "papel":
        print("Ganaste, tijera corta papel")
    elif eligeUsuario == "tijera" and eligePc == "lagarto":
        print("Ganaste, tijera decapita lagarto")
    elif eligeUsuario == "lagarto" and eligePc == "papel":
        print("Ganaste, lagarto devora papel")
    elif eligeUsuario == "lagarto" and eligePc == "spok":
        print("Ganaste, lagarto envenena a Spok")
    elif eligeUsuario == "spok" and eligePc == "tijera":
        print("Ganaste, Spok rompe la tijera")
    elif eligeUsuario == "spok" and eligePc == "piedra":
        print("Ganaste, Spok vaporiza la piedra")

    if eligePc == "papel" and eligeUsuario == "piedra":
        print("Perdiste, papel envuelve la piedra")
    elif eligePc == "papel" and eligeUsuario == "spok":
        print("Perdiste, papel desautoriza a Spok")
    elif eligePc == "piedra" and eligeUsuario == "tijera":
        print("Perdiste, piedra aplasta la tijera")
    elif eligePc == "piedra" and eligeUsuario == "lagarto":
        print("Perdiste, piedra aplasta lagarto")
    elif eligePc == "tijera" and eligeUsuario == "papel":
        print("Perdiste, tijera corta papel")
    elif eligePc == "tijera" and eligeUsuario == "lagarto":
        print("Perdiste, tijera decapita lagarto")
    elif eligePc == "lagarto" and eligeUsuario == "papel":
        print("Perdiste, lagarto devora papel")
    elif eligePc == "lagarto" and eligeUsuario == "spok":
        print("Perdiste, lagarto envenena a Spok")
    elif eligePc == "spok" and eligeUsuario == "tijera":
        print("Perdiste, Spok rompe la tijera")
    elif eligePc == "spok" and eligeUsuario == "piedra":
        print("Perdiste, Spok vaporiza la piedra")

    if eligePc == eligeUsuario:
        print("Empate")

    again = input("Jugamos de nuevo? Si/No: ")
    if 'si' in again:
        continue
    elif 'no' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")
