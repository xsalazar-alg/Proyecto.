import os
import time

def borrarPantalla(): # La idea es ponerlo antes de cada cambio de menú.
    try:
        if os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")
        elif os.name == "posix":
            os.system ("clear")
        else:
            raise OSError
    except OSError:
        print('No s\'ha pogut reconèixer el teu sistema operatiu, no es netejarà la pantalla.')


def getOpt(textOpts="", inputOptText="", rangeList=[]):
    print(textOpts)
    inputOptText = input(" "*63 + "Opció:\n" + " "*63 + "> ")
    try:
        if inputOptText.isdigit():
            inputOptText = int(inputOptText)
        if inputOptText not in rangeList:
            raise IndexError
        if inputOptText in rangeList:
            return inputOptText
    except IndexError:
        input(" "*49 + 'Aquesta opció no és vàlida, ENTER per continuar...')
        borrarPantalla()


def ChooseYourDeck(spanish1, spanish2, spanish3, spanish4, spanish5, spanish6, poker1, poker2, poker3, poker4, poker5, poker6):
    opt_ok = False
    while not opt_ok:
        try:
            chooseSpanish = 'Type "Spanish" and you will pick the spanish deck'
            print('\n\n', chooseSpanish.center(150))
            print(spanish1.center(151), '\n', spanish2.center(150), '\n', spanish3.center(150), '\n', spanish4.center(150), '\n', spanish5.center(150), '\n', spanish6.center(150),'\n\n')
            # ------------------------------------
            choosePoker = 'Type "Poker" and you will pick the poker deck'
            print('\n', choosePoker.center(150))
            print(poker1.center(151), '\n', poker2.center(150), '\n', poker3.center(150), '\n', poker4.center(150), '\n', poker5.center(150), '\n', poker6.center(150),'\n\n')
            # ------------------------------------
            chooseBack = 'Type "Back" to return'
            print(chooseBack.center(150))


            option = input('\n                                                              > ')
            option = option.lower()
            if option == "spanish" or option == "poker" or option == "back":
                return option
            else:
                raise TypeError
            
        except TypeError:
            print("That's not an option. Press ENTER to continue...")

def maxRounds():
    rounds_ok = False
    while not rounds_ok:
        try:
            rounds = input('\n\n' + ' '*50 + 'Select the max of rounds for the next game (5-30):\n' + ' '*50 + '> ')
            if not rounds.isdigit():
                raise TypeError
            rounds = int(rounds)
            if rounds < 5 or rounds > 30:
                raise ValueError
            else:
                rounds_ok = True
                return rounds
        except ValueError:
            print('\n' + ' '*50 + 'That\'s not a valid number!')
            input(' '*50 + 'Press ENTER to continue...')
        except TypeError:
            print('\n' + ' '*50 + 'That\'s not a number!')
            input(' '*50 + 'Press ENTER to continue...')


# PRUEBAS
'''
t0 = time.time()

input('Holaaaaa dale a ENTER para continuar...')

t1 = time.time()

tiempo_jugado = t1-t0
tiempo_jugado = round(tiempo_jugado)

minutos_jugados = tiempo_jugado / 60

input(f'Has tardado {tiempo_jugado} segundos en darle al ENTER, y en minutos {minutos_jugados}.')'''