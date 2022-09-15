from colorama import Fore, Style, Back
player1 = "X"
player2 = "0"
board = {
    "7": " ", "8": " ", "9": " ",
    "4": " ", "5": " ", "6": " ",
    "1": " ", "2": " ", "3": " "
}
def setup():
    print(" " + '7' + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + '8' + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + '9')
    print(Back.RED + Fore.BLUE + "---+---+---" + Style.RESET_ALL)
    print(" " + '4' + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + '5' + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + '6')
    print(Back.RED + Fore.BLUE + "---+---+---" + Style.RESET_ALL)
    print(" " + '1' + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + '2' + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + '3'+"\n")
def game():
    print(" " + board['7'] + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + board['8'] + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + board['9'])
    print(Back.RED + Fore.BLUE + "---+---+---" + Style.RESET_ALL)
    print(" " + board['4'] + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + board['5'] + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + board['6'])
    print(Back.RED + Fore.BLUE + "---+---+---" + Style.RESET_ALL)
    print(" " + board['1'] + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + board['2'] + " " + Back.RED + Fore.BLUE + "|" + Style.RESET_ALL + " " + board['3']+"\n")
def inputt():
    alternator = 0
    variable = " "
    no_repeat = []
    command = ["1", "2" , "3", "4", "5", "6", "7", "8", "9"]
    print(Back.LIGHTGREEN_EX + Style.BRIGHT + " Have a look on controls!!!       " + Style.RESET_ALL+"\n")
    print(Fore.RED + "LET'S BEGIN THE GAME..." + Style.RESET_ALL)
    while ((board['1'] != board['2'] or board['1'] != board['3'] or board['1'] == " " or board['2'] ==" " or board['3'] == " ") and
           (board['4'] != board['5'] or board['4'] != board['6'] or board['3'] == " " or board['4'] == " " or board['6'] == " ") and
           (board['7'] != board['8'] or board['7'] != board['9'] or board['7'] == " " or board['8'] == " " or board['9'] == " ") and
           (board['1'] != board['4'] or board['1'] != board['7'] or board['1'] == " " or board['4'] == " " or board['7'] == " ") and
           (board['2'] != board['5'] or board['2'] != board['8'] or board['2'] == " " or board['5'] == " " or board['8'] == " ") and
           (board['3'] != board['6'] or board['3'] != board['9'] or board['3'] == " " or board['6'] == " " or board['9'] == " ") and
           (board['1'] != board['5'] or board['1'] != board['9'] or board['1'] == " " or board['5'] == " " or board['9'] == " ") and
           (board['3'] != board['5'] or board['3'] != board['7'] or board['3'] == " " or board['5'] == " " or board['7'] == " ")):
        if alternator % 2 == 0:
            variable = player1
        else:
            variable = player2
        print(Back.BLUE + f"CHANCE OF PLAYER: {variable}               " + Style.RESET_ALL)
        if len(no_repeat)==9:
            print(Back.LIGHTYELLOW_EX + " ITS A TIE :-)... " + Style.RESET_ALL)
            checker=True
            exit()
        elif len(no_repeat)<9:
            location = input()
            if location not in no_repeat:
                if location in command:
                    board.update({location: variable})
                    no_repeat.append(location)
                else:
                    print("ERROR! Invalid Move")
            else:
                print("ERROR! : Repeated Move")
                alternator = alternator - 1
            alternator = alternator + 1
        game()
    print(Back.LIGHTYELLOW_EX + f"winner is {variable}"+Style.RESET_ALL+"\n")
setup()
inputt()