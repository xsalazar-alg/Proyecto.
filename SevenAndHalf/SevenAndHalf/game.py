#####################################################
#                                                   #
#                       IMPORTS                     #
#                                                   #
#####################################################

import mysql.connector

mydb = mysql.connector.connect (
  host="proyecto-claudia-shayel-pol.mysql.database.azure.com",
  user="pol@proyecto-claudia-shayel-pol",
  password="P@ssw0rd"
)

import time
import random
import os
from functions import getOpt, borrarPantalla, ChooseYourDeck, maxRounds


#####################################################
#                                                   #
#                       TÍTOLS                      #
#                                                   #
#####################################################

lineas_titulo ="⊷"*150

# TÍTOL SEVEN AND HALF                                                      ---> https://www.askapache.com/online-tools/figlet-ascii/     FONT = basic
Seven1        =" .d8888. d88888b db    db d88888b d8b   db "
Seven2        =" 88'  YP 88'     88    88 88'     888o  88 "
Seven3        =" `8bo.   88ooooo Y8    8P 88ooooo 88V8o 88 "
Seven4        ="   `Y8b. 88      `8b  d8' 88      88 V8o88 "
Seven5        =" db   8D 88.      `8bd8'  88.     88  V888 "
Seven6        =" `8888Y' Y88888P    YP    Y88888P VP   V8P "

And1          ="  .d8b.  d8b   db d8888b. "
And2          =" d8' `8b 888o  88 88  `8D "
And3          =" 88ooo88 88V8o 88 88   88 "
And4          =" 88~~~88 88 V8o88 88   88 "
And5          =" 88   88 88  V888 88  .8D "
And6          =" YP   YP VP   V8P Y8888D' "

Half1         ="db   db  .d8b.  db      d88888b "
Half2         ="88   88 d8' `8b 88      88'     "     
Half3         ="88ooo88 88ooo88 88      88ooo   "
Half4         ="88   88 88   88 88      88      "
Half5         ="88   88 88   88 88booo. 88      "
Half6         ="YP   YP YP   YP Y88888P YP      "

settings1 = ".d8888. d88888b d888888b d888888b d888888b d8b   db  d888b  .d8888. "
settings2 = "88'  YP 88'        88       88      `88'   888o  88 88' Y8b 88'  YP "
settings3 = "`8bo.   88ooooo    88       88       88    88V8o 88 88      `8bo.   "
settings4 = "  `Y8b. 88         88       88       88    88 V8o88 88  roo   `Y8b. "
settings5 = "db   8D 88.        88       88      .88.   88  V888 88. 88  db   8D "
settings6 = "`8888Y' Y88888P    YP       YP    Y888888P VP   V8P  Y888P  `8888Y' "

pick1 = "d8888b. d888888b  .o88b. db   dD        .d8b.        d8888b. d88888b  .o88b. db   dD "
pick2 = "88  `8D   `88'   d8P  Y8 88 ,8P'       d8' `8b       88  `8D 88'     d8P  Y8 88 ,8P' "
pick3 = "88oodD'    88    8P      88,8P         88ooo88       88   88 88ooooo 8P      88,8P   "
pick4 = "88         88    8b      88`8b         88   88       88   88 88      8b      88`8b   "
pick5 = "88        .88.   Y8b  d8 88 `88.       88   88       88  .8D 88.     Y8b  d8 88 `88. "
pick6 = "88      Y888888P  `Y88P' YP   YD       YP   YP       Y8888D' Y88888P  `Y88P' YP   YD "

set1 = ".d8888. d88888b d888888b     .88b  d88.  .d8b.  db    db "
set2 = "88'  YP 88'        88        88'YbdP`88 d8' `8b `8b  d8' "
set3 = "`8bo.   88ooooo    88        88  88  88 88ooo88  `8bd8'  "
set4 = "  `Y8b. 88         88        88  88  88 88   88  .dPYb.  "
set5 = "db   8D 88.        88        88  88  88 88   88 .8P  Y8. "
set6 = "`8888Y' Y88888P    YP        YP  YP  YP YP   YP YP    YP "

rounds1 = "d8888b.  .d88b.  db    db d8b   db d8888b. .d8888."
rounds2 = "88  `8D .8P  Y8. 88    88 888o  88 88  `8D 88'  YP "
rounds3 = "88oobY' 88    88 88    88 88V8o 88 88   88 `8bo.   "
rounds4 = "88`8b   88    88 88    88 88 V8o88 88   88   `Y8b. "
rounds5 = "88 `88. `8b  d8' 88b  d88 88  V888 88  .8D db   8D "
rounds6 = "88   YD  `Y88P'  ~Y8888P' VP   V8P Y8888D' `8888Y' "

nrounds1 = ",d88888        d8888b.  .d88b.  "
nrounds2 = "88             VP  `8D .8P  88. "
nrounds3 = "dP88b.           oooY' 88  d'88 "
nrounds4 = "    b88 C8888D   ~~~b. 88 d' 88 "
nrounds5 = "    `8D        db   8D `88  d8' "
nrounds6 = "88oobY'        Y8888P'  `Y88P'  "

spanish1 = ".------..------..------..------..------..------..------."
spanish2 = "|S.--. ||P.--. ||A.--. ||N.--. ||I.--. ||S.--. ||H.--. |"
spanish3 = "| :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :/\: |"
spanish4 = "| :\/: || (__) || :\/: || ()() || :\/: || :\/: || (__) |"
spanish5 = "| '--'S|| '--'P|| '--'A|| '--'N|| '--'I|| '--'S|| '--'H|"
spanish6 = "`------'`------'`------'`------'`------'`------'`------'"

poker1 = ".------..------..------..------..------."
poker2 = "|P.--. ||O.--. ||K.--. ||E.--. ||R.--. |"
poker3 = "| :/\: || :/\: || :/\: || (\/) || :(): |"
poker4 = "| (__) || :\/: || :\/: || :\/: || ()() |"
poker5 = "| '--'P|| '--'O|| '--'K|| '--'E|| '--'R|"
poker6 = "`------'`------'`------'`------'`------'"


#####################################################
#                                                   #
#                        MENÚS                      #
#                                                   #
#####################################################

menu00 = "\n" + " "*63 + "1) Add/Remove/Show Players".ljust(60)+"\n" + " "*63 + "2) Settings".ljust(60)+"\n"  + " "*63 + "3) Play Game".ljust(60)+"\n"  + " "*63 + "4) Ranking".ljust(60)+"\n" + " "*63 + "5) Reports".ljust(60)+"\n"  + " "*63 + "6) Exit".ljust(60)
menu01 = "\n" + " "*63 + "1) New Human Player".ljust(60)+"\n" + " "*63 + "2) New Boot".ljust(60)+"\n"  + " "*63 + "3) Show/Remove Players".ljust(60)+"\n"  + " "*63 + "4) Go Back".ljust(60)
menu02 = "\n" + " "*63 + "1) Set Game Players".ljust(60)+"\n" + " "*63 + "2) Set Card's Deck (Default Spanish Deck)".ljust(60)+"\n"  + " "*63 + "3) Set Max Rounds (Default 5 Rounds)".ljust(60)+"\n"  + " "*63 + "4) Go Back".ljust(60)
menu04 = "\n" + " "*63 + "1) Players With More Earnings".ljust(60)+"\n" + " "*63 + "2) Players With More Games Played".ljust(60)+"\n"  + " "*63 + "3) Players With More Minutes Played".ljust(60)
menu05 = "\n" + " "*63 + "1) Initial card more repeated by each user,\nonly users who have played a minimum of 3 games.".ljust(60)+"\n" + " "*63 + "2) Player who makes the highest bet per game,\nfind the round with the highest bet.".ljust(60)+"\n" + " "*63 + "3) Player who makes the lowest bet per game.".ljust(60)+"\n" + " "*63 + "4) Percentage of rounds won per player in each game\n(%), as well as their average bet for the game.".ljust(60)+"\n" + " "*63 + "5) List of games won by Bots.".ljust(60)+"\n" + " "*63 + "6) Rounds won by the bank in each game.".ljust(60)+"\n" + " "*63 + "7) Number of users have been the bank in each game.".ljust(60)+"\n" + " "*63 + "8) Average bet per game.".ljust(60)+"\n" + " "*63 + "9) Average bet of the first round of each game.".ljust(60)+"\n" + " "*63 + "10) Average bet of the last round of each game.".ljust(60)+"\n" + " "*63 + "11) Go Back."


#####################################################
#                                                   #
#                       BARAJAS                     #
#                                                   #
#####################################################

baraja_española = {
                # ---------------------------- OROS / COINS
                "G01": {"literal": "Ace of Coins", "value": 1, "priority": 4, "realValue": 1},
                "G02": {"literal": "Two of Coins", "value": 2, "priority": 4, "realValue": 2},
                "G03": {"literal": "Three of Coins", "value": 3, "priority": 4, "realValue": 3},
                "G04": {"literal": "Four of Coins", "value": 4, "priority": 4, "realValue": 4},
                "G05": {"literal": "Five of Coins", "value": 5, "priority": 4, "realValue": 5},
                "G06": {"literal": "Six of Coins", "value": 6, "priority": 4, "realValue": 6},
                "G07": {"literal": "Seven of Coins", "value": 7, "priority": 4, "realValue": 7},
                "G08": {"literal": "Eight of Coins", "value": 8, "priority": 4, "realValue": 0.5},
                "G09": {"literal": "Nine of Coins", "value": 9, "priority": 4, "realValue": 0.5},
                "G10": {"literal": "Jack of Coins", "value": 10, "priority": 4, "realValue": 0.5},
                "G11": {"literal": "Horse of Coins", "value": 11, "priority": 4, "realValue": 0.5},
                "G12": {"literal": "King of Coins", "value": 12, "priority": 4, "realValue": 0.5},
                # ---------------------------- COPAS / CUPS
                "C01": {"literal": "Ace of Cups", "value": 1, "priority": 3, "realValue": 1},
                "C02": {"literal": "Two of Cups", "value": 2, "priority": 3, "realValue": 2},
                "C03": {"literal": "Three of Cups", "value": 3, "priority": 3, "realValue": 3},
                "C04": {"literal": "Four of Cups", "value": 4, "priority": 3, "realValue": 4},
                "C05": {"literal": "Five of Cups", "value": 5, "priority": 3, "realValue": 5},
                "C06": {"literal": "Six of Cups", "value": 6, "priority": 3, "realValue": 6},
                "C07": {"literal": "Seven of Cups", "value": 7, "priority": 3, "realValue": 7},
                "C08": {"literal": "Eight of Cups", "value": 8, "priority": 3, "realValue": 0.5},
                "C09": {"literal": "Nine of Cups", "value": 9, "priority": 3, "realValue": 0.5},
                "C10": {"literal": "Jack of Cups", "value": 10, "priority": 3, "realValue": 0.5},
                "C11": {"literal": "Horse of Cups", "value": 11, "priority": 3, "realValue": 0.5},
                "C12": {"literal": "King of Cups", "value": 12, "priority": 3, "realValue": 0.5},
                # ---------------------------- SWORDS / ESPADAS
                "S01": {"literal": "Ace of Swords", "value": 1, "priority": 2, "realValue": 1},
                "S02": {"literal": "Two of Swords", "value": 2, "priority": 2, "realValue": 2},
                "S03": {"literal": "Three of Swords", "value": 3, "priority": 2, "realValue": 3},
                "S04": {"literal": "Four of Swords", "value": 4, "priority": 2, "realValue": 4},
                "S05": {"literal": "Five of Swords", "value": 5, "priority": 2, "realValue": 5},
                "S06": {"literal": "Six of Swords", "value": 6, "priority": 2, "realValue": 6},
                "S07": {"literal": "Seven of Swords", "value": 7, "priority": 2, "realValue": 7},
                "S08": {"literal": "Eight of Swords", "value": 8, "priority": 2, "realValue": 0.5},
                "S09": {"literal": "Nine of Swords", "value": 9, "priority": 2, "realValue": 0.5},
                "S10": {"literal": "Jack of Swords", "value": 10, "priority": 2, "realValue": 0.5},
                "S11": {"literal": "Horse of Swords", "value": 11, "priority": 2, "realValue": 0.5},
                "S12": {"literal": "King of Swords", "value": 12, "priority": 2, "realValue": 0.5},
                # ---------------------------- CLUBS / BASTOS
                "B01": {"literal": "Ace of Clubs", "value": 1, "priority": 1, "realValue": 1},
                "B02": {"literal": "Two of Clubs", "value": 2, "priority": 1, "realValue": 2},
                "B03": {"literal": "Three of Clubs", "value": 3, "priority": 1, "realValue": 3},
                "B04": {"literal": "Four of Clubs", "value": 4, "priority": 1, "realValue": 4},
                "B05": {"literal": "Five of Clubs", "value": 5, "priority": 1, "realValue": 5},
                "B06": {"literal": "Six of Clubs", "value": 6, "priority": 1, "realValue": 6},
                "B07": {"literal": "Seven of Clubs", "value": 7, "priority": 1, "realValue": 7},
                "B08": {"literal": "Eight of Clubs", "value": 8, "priority": 1, "realValue": 0.5},
                "B09": {"literal": "Nine of Clubs", "value": 9, "priority": 1, "realValue": 0.5},
                "B10": {"literal": "Jack of Clubs", "value": 10, "priority": 1, "realValue": 0.5},
                "B11": {"literal": "Horse of Clubs", "value": 11, "priority": 1, "realValue": 0.5},
                "B12": {"literal": "King of Clubs", "value": 12, "priority": 1, "realValue": 0.5}
}


baraja_poker = {# ----------------------- Tréboles / Clubs
                "C01":{"literal":"One of Clubs", "value": 1, "priority": 4, "realValue": 1},
                "C02":{"literal":"Two of Clubs", "value":2, "priority":4, "realValue":2},
                "C03":{"literal":"Three of Clubs", "value":3, "priority":4, "realValue":3},
                "C04":{"literal":"Four of Clubs", "value":4, "priority":4, "realValue":4},
                "C05":{"literal":"Five of Clubs", "value":5, "priority":4, "realValue":5},
                "C06":{"literal":"Six of Clubs", "value":6, "priority":4, "realValue":6},
                "C07":{"literal":"Seven of Clubs", "value":7, "priority":4, "realValue":7},
                "C08":{"literal":"Eight of Clubs", "value":8, "priority":4, "realValue":0.5},
                "C09":{"literal":"Nine of Clubs", "value":9, "priority":4, "realValue":0.5},
                "C10":{"literal":"Ten of Clubs", "value":10, "priority":4, "realValue":0.5},
                "C11":{"literal":"Jack of Clubs", "value":11, "priority":4, "realValue":0.5},
                "C12":{"literal":"Queen of Clubs", "value":12, "priority":4, "realValue":0.5},
                "C13":{"literal":"King of Clubs", "value":13, "priority":4, "realValue":0.5},
                "C14":{"literal":"Ace of Clubs", "value":14, "priority":4, "realValue":0.5},
                # ----------------------- Picas / Spades
                "S01":{"literal":"One of Spades", "value": 1, "priority": 3, "realValue": 1},
                "S02":{"literal":"Two of Spades", "value":2, "priority":3, "realValue":2},
                "S03":{"literal":"Three of Spades", "value":3, "priority":3, "realValue":3},
                "S04":{"literal":"Four of Spades", "value":4, "priority":3, "realValue":4},
                "S05":{"literal":"Five of Spades", "value":5, "priority":3, "realValue":5},
                "S06":{"literal":"Six of Spades", "value":6, "priority":3, "realValue":6},
                "S07":{"literal":"Seven of Spades", "value":7, "priority":3, "realValue":7},
                "S08":{"literal":"Eight of Spades", "value":8, "priority":3, "realValue":0.5},
                "S09":{"literal":"Nine of Spades", "value":9, "priority":3, "realValue":0.5},
                "S10":{"literal":"Ten of Spades", "value":10, "priority":3, "realValue":0.5},
                "S11":{"literal":"Jack of Spades", "value":11, "priority":3, "realValue":0.5},
                "S12":{"literal":"Queen of Spades", "value":12, "priority":3, "realValue":0.5},
                "S13":{"literal":"King of Spades", "value":13, "priority":3, "realValue":0.5},
                "S14":{"literal":"Ace of Spades", "value":14, "priority":3, "realValue":0.5},
                # ----------------------- Corazones / Hearts
                "H01":{"literal":"One of Hearts", "value": 1, "priority": 2, "realValue": 1},
                "H02":{"literal":"Two of Hearts", "value":2, "priority":2, "realValue":2},
                "H03":{"literal":"Three of Hearts", "value":3, "priority":2, "realValue":3},
                "H04":{"literal":"Four of Hearts", "value":4, "priority":2, "realValue":4},
                "H05":{"literal":"Five of Hearts", "value":5, "priority":2, "realValue":5},
                "H06":{"literal":"Six of Hearts", "value":6, "priority":2, "realValue":6},
                "H07":{"literal":"Seven of Hearts", "value":7, "priority":2, "realValue":7},
                "H08":{"literal":"Eight of Hearts", "value":8, "priority":2, "realValue":0.5},
                "H09":{"literal":"Nine of Hearts", "value":9, "priority":2, "realValue":0.5},
                "H10":{"literal":"Ten of Hearts", "value":10, "priority":2, "realValue":0.5},
                "H11":{"literal":"Jack of Hearts", "value":11, "priority":2, "realValue":0.5},
                "H12":{"literal":"Queen of Hearts", "value":12, "priority":2, "realValue":0.5},
                "H13":{"literal":"King of Hearts", "value":13, "priority":2, "realValue":0.5},
                "H14":{"literal":"Ace of Hearts", "value":14, "priority":2, "realValue":0.5},
                # ----------------------- Diamantes / Diamonds
                "D01":{"literal":"One of Diamonds", "value": 1, "priority": 1, "realValue": 1},
                "D02":{"literal":"Two of Diamonds", "value":2, "priority":1, "realValue":2},
                "D03":{"literal":"Three of Diamonds", "value":3, "priority":1, "realValue":3},
                "D04":{"literal":"Four of Diamonds", "value":4, "priority":1, "realValue":4},
                "D05":{"literal":"Five of Diamonds", "value":5, "priority":1, "realValue":5},
                "D06":{"literal":"Six of Diamonds", "value":6, "priority":1, "realValue":6},
                "D07":{"literal":"Seven of Diamonds", "value":7, "priority":1, "realValue":7},
                "D08":{"literal":"Eight of Diamonds", "value":8, "priority":1, "realValue":0.5},
                "D09":{"literal":"Nine of Diamonds", "value":9, "priority":1, "realValue":0.5},
                "D10":{"literal":"Ten of Diamonds", "value":10, "priority":1, "realValue":0.5},
                "D11":{"literal":"Jack of Diamonds", "value":11, "priority":1, "realValue":0.5},
                "D12":{"literal":"Queen of Diamonds", "value":12, "priority":1, "realValue":0.5},
                "D13":{"literal":"King of Diamonds", "value":13, "priority":1, "realValue":0.5},
                "D14":{"literal":"Ace of Diamonds", "value":14, "priority":1, "realValue":0.5}}


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
baraja = baraja_española
opc = None

while opc != -1:
    while opc == None:  # MENU 00
        print('\n', Seven1.center(150), '\n', Seven2.center(150), '\n', Seven3.center(150), '\n', Seven4.center(150), '\n', Seven5.center(150), '\n', Seven6.center(150))
        print('\n', And1.center(150), '\n', And2.center(150), '\n', And3.center(150), '\n', And4.center(150), '\n', And5.center(150), '\n', And6.center(150))
        print('\n', Half1.center(150), '\n', Half2.center(150), '\n', Half3.center(150), '\n', Half4.center(150), '\n', Half5.center(150), '\n', Half6.center(150), '\n')
        print(lineas_titulo.center(150))
        opc = getOpt(textOpts=menu00, inputOptText="", rangeList=[1, 2, 3, 4, 5, 6])

    if opc == 1:        # MENU 01
        print('Opción 1.')
        input('ENTER to continue...')
        opc = None

    while opc == 2:     # MENU 02
        borrarPantalla()
        print("\n", settings1.center(150), '\n', settings2.center(150), '\n', settings3.center(150), '\n', settings4.center(150), '\n', settings5.center(150), '\n', settings6.center(150))
        print("\n", lineas_titulo.center(150), "\n")
        opc2 = getOpt(textOpts=menu02, inputOptText="", rangeList=[1, 2, 3, 4])
        borrarPantalla()

        if opc2 == 1:   # MENU 21
            print('Opción 1.')
            input('ENTER to continue...')
            borrarPantalla()
            opc2 = None

        elif opc2 == 2: # Pick a deck
            borrarPantalla()
            print("\n", pick1.center(150), '\n', pick2.center(150), '\n', pick3.center(150), '\n', pick4.center(150), '\n', pick5.center(150), '\n', pick6.center(150))
            print("\n", lineas_titulo.center(150))
            opc_baraja = ChooseYourDeck(spanish1, spanish2, spanish3, spanish4, spanish5, spanish6, poker1, poker2, poker3, poker4, poker5, poker6)
            if opc_baraja == "spanish":
                baraja = baraja_española
                print("\n" + " "*55 + "Your deck have been changed successfully")
                input(" "*65 + 'ENTER to continue...')
            elif opc_baraja == "poker":
                baraja = baraja_poker
                print("\n" + " "*55 + "Your deck have been changed successfully")
                input(" "*65 + 'ENTER to continue...')
            borrarPantalla()

        elif opc2 == 3: # Set max rounds
            print('\n', set1.center(150), '\n', set2.center(150), '\n', set3.center(150), '\n', set4.center(150), '\n', set5.center(150), '\n', set6.center(150))
            print('\n', rounds1.center(148), '\n', rounds2.center(150), '\n', rounds3.center(150), '\n', rounds4.center(150), '\n', rounds5.center(150), '\n', rounds6.center(150))
            print("\n", lineas_titulo.center(150))
            print('\n', nrounds1.center(150), '\n', nrounds2.center(150), '\n', nrounds3.center(150), '\n', nrounds4.center(150), '\n', nrounds5.center(150), '\n', nrounds6.center(150))
            rounds = maxRounds()
            print(" "*50 + "Max of rounds setted succesfully!")
            input(' '*50 + 'ENTER to continue...')
            borrarPantalla()
            
        elif opc2 == 4: # MENU 24
            borrarPantalla()
            opc2 = None
            opc = None
    
    if opc == 3:    # Play Game
        print('play')
        input('ENTER to continue...')

    if opc == 4:    # Ranking
        print('Este es el Ranking')
        input('ENTER to continue...')

    if opc == 5:    # Reports
        print('Reports (queremos hacer al menos: 2, 3, 6, 7, 8, 9, 10)')
        input('ENTER to continue...')

    if opc == 6:
        opc = -1
