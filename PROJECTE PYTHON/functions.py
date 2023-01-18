import os
import time

letraNIF = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

Players1 = "d8888b. d8888b. d8888b. d8888b.    d8888b. db       .d8b.  db    db d88888b d8888b. .d8888. "
Players2 = "88  `8D 88  `8D 88  `8D 88  `8D    88  `8D 88      d8' `8b `8b  d8' 88'     88  `8D 88'  YP "
Players3 = "88oooY' 88oooY' 88   88 88   88    88oodD' 88      88ooo88  `8bd8'  88ooooo 88oobY' `8bo.   "
Players4 = "88~~~b. 88~~~b. 88   88 88   88    88~~~   88      88~~~88    88    88~~~~~ 88`8b     `Y8b. "
Players5 = "88   8D 88   8D 88  .8D 88  .8D    88      88booo. 88   88    88    88.     88 `88. db   8D "
Players6 = "Y8888P' Y8888P' Y8888D' Y8888D'    88      Y88888P YP   YP    YP    Y88888P 88   YD `8888Y' "

lineas_titulo = "⊷" * 150

# ————————————————————————————————————————————————————————————————————— La idea es ponerlo antes de cada cambio de menú.
def borrarPantalla():
    try:
        if os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            raise OSError
    except OSError:
        print("Your operating system couldn't be recognized, screen will not be cleaned.")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def getOpt(textOpts="", inputOptText="", rangeList=[]):
    print(textOpts)
    inputOptText = input(" " * 63 + "Opció:\n" + " " * 63 + "> ")
    try:
        if inputOptText.isdigit():
            inputOptText = int(inputOptText)
        if inputOptText not in rangeList:
            raise IndexError
        if inputOptText in rangeList:
            return inputOptText
    except IndexError:
        input(" " * 49 + "This option is not valid. Press enter to continue...")
        borrarPantalla()


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def ChooseYourDeck(spanish1, spanish2, spanish3, spanish4, spanish5, spanish6, poker1, poker2, poker3, poker4, poker5,
                   poker6):
    opt_ok = False
    while not opt_ok:
        try:
            chooseSpanish = "Type \"Spanish\" and you will pick the spanish deck"
            print("\n\n", chooseSpanish.center(150))
            print(spanish1.center(151), '\n', spanish2.center(150), '\n', spanish3.center(150), "\n",
                  spanish4.center(150), '\n', spanish5.center(150), '\n', spanish6.center(150), "\n\n")
            # ------------------------------------
            choosePoker = "Type \"Poker\" and you will pick the poker deck"
            print("\n", choosePoker.center(150))
            print(poker1.center(151), "\n", poker2.center(150), "\n", poker3.center(150), "\n", poker4.center(150),
                  "\n", poker5.center(150), "\n", poker6.center(150), "\n\n")
            # ------------------------------------
            chooseBack = "Type \"Back\" to return"
            print(chooseBack.center(150))

            option = input("\n                                                              > ")
            option = option.lower()
            if option == "spanish" or option == "poker" or option == "back":
                return option
            else:
                raise TypeError

        except TypeError:
            print("That's not an option. Press ENTER to continue...")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def maxRounds():
    rounds_ok = False
    while not rounds_ok:
        try:
            rounds = input("\n\n" + " " * 50 + "Select the max of rounds for the next game (5-30):\n" + " " * 50 + "> ")
            if not rounds.isdigit():
                raise TypeError
            rounds = int(rounds)
            if rounds < 5 or rounds > 30:
                raise ValueError
            else:
                rounds_ok = True
                return rounds
        except ValueError:
            print("\n" + " " * 50 + "That's not a valid number!")
            input(" " * 50 + "Press ENTER to continue...")
        except TypeError:
            print('\n' + " " * 50 + "That's not a number!")
            input(" " * 50 + "Press ENTER to continue...")


# —————————————————————————————————————————————————————————————————————————————————————— PRUEBAS.

def crear_nombre():
    borrarPantalla()
    print("\n", Players1.center(150), "\n", Players2.center(150), "\n", Players3.center(150), "\n", Players4.center(150),
          "\n", Players5.center(150), "\n", Players6.center(150), "\n")
    print(lineas_titulo.center(150))
    nombre_ok = False
    while not nombre_ok:
        try:
            nombre = input("Insert Name: ")
            if nombre.isspace() or nombre == "":
                raise TypeError("Incorrect typing")
            else:
                return nombre

        except TypeError:
            print("Space-only or empty names are not allowed. Type Name Again.")

def crear_dni():
    borrarPantalla()
    print("\n", Players1.center(150), "\n", Players2.center(150), "\n", Players3.center(150), "\n", Players4.center(150),
          "\n", Players5.center(150), "\n", Players6.center(150), "\n")
    print(lineas_titulo.center(150))
    dni_ok = False
    while not dni_ok:
        try:
            DNI = input("Insert NIF: ").upper()
            NIF = DNI[0:len(DNI)-1]
            if 9 > len(NIF) > 6:
                letraDNI = letraNIF[int(NIF) % 23]
                NIFadd = NIF + letraDNI
                if NIFadd == DNI:
                    return DNI
                else:
                    raise ValueError # Incorrect letter.
                
            else:
                raise IndexError # Incorrect length.
        
        except ValueError:
            print("The letter doesn't match with the NIF. Type NIF again.")

        except IndexError:
            print("NIF's length isn't correct. Type NIF again.")
                
def establecer_tipo():
    borrarPantalla()
    print("\n", Players1.center(150), "\n", Players2.center(150), "\n", Players3.center(150), "\n", Players4.center(150),
          "\n", Players5.center(150), "\n", Players6.center(150), "\n")
    print(lineas_titulo.center(150))
    opc = getOpt(textOpts="Select your profile:\n1) Cautious\n2) Moderated\n3) Bold", inputOptText="", rangeList=[1, 2, 3])
    if opc == 1:
        #son 30 puntos
        type = 30
        return type
    elif opc == 2:
        #son 40p
        type = 40
        return type
    elif opc == 3:
        #son 50p
        type = 50
        return type

def crear_jugador():
    nombre = crear_nombre()
    dni = crear_dni()
    type = establecer_tipo()
    return nombre, dni, type

"""
t0 = time.time()
input("Holaaaaa dale a ENTER para continuar...")
t1 = time.time()
tiempo_jugado = t1-t0
tiempo_jugado = round(tiempo_jugado)
minutos_jugados = tiempo_jugado / 60
input(f"Has tardado {tiempo_jugado} segundos en darle al ENTER, y en minutos {minutos_jugados}.")
"""
