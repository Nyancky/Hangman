import random


def load_words(gamemode):
    capital = []
    country = []
    easy = []
    medium = []
    hard = []
    with open("C:\Users\sinka\Documents\GitHub\proba\.vscode\01\countries-and-capitals.txt", "r") as f:
        for line in f:
            splitline = line.split(" | ")
            country.append(splitline[0])
            capital.append(splitline[1])
        if gamemode == 1:
            for k in range(len(country)):
                if len(country[k]) < 7:
                    easy.append(country[k])
            return random.choice(easy)
        elif gamemode == 2:
            for k in range(len(country)):
                if len(country[k]) < 11 and len(country[k]) > 6:
                    medium.append(country[k])
            return random.choice(medium)
        elif gamemode == 3:
            for k in range(len(country)):
                if len(country[k]) > 10:
                    hard.append(country[k])
            return random.choice(hard)
        elif gamemode == 4:
            return secret()


exceptions = [" ", "'", "!", ",", "/", "-", "-"]


hm = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def difficulty():
    gamemode = input('[1:easy], [2:medium], [3:hard] ')
    if gamemode == "1":
        game = 3
    elif gamemode == "2":
        game = 2
    elif gamemode == "3":
        game = 1
    elif gamemode == "4":
        game = 4
    else:
        return difficulty()
    return game


def health(x):
    if x == 3:
        hp = 9
        return hp
    if x == 2:
        hp = 6
        return hp
    if x == 1 or 4:
        hp = 3
        return hp


def pics(mode, hp):
    if hp > 5:
        return hm[0]
    elif hp > 4:
        return hm[1]
    elif hp > 3:
        return hm[2]
    elif hp > 2:
        return hm[3]
    elif hp > 1:
        return hm[4]
    elif hp > 0:
        return hm[5]
    elif hp > -1:
        return hm[6]


def puzzle(szo, rejtett_karakter="_ "):
    karakter = ""
    for x in szo:
        karakter = karakter + rejtett_karakter
    return karakter


def output_tl(tipp_list, upper_list):
    upper_list = []
    upper_list.append(tipp_list[0::2])
    print(upper_list)


def secret():
    return 'ALMA-FA'


def kitoltes(szo_lista, feladvany_lista, feladvany2):
    for y in range(len(exceptions)):
        for x in range(len(szo_lista)):
            if szo_lista[x] == exceptions[y]:
                feladvany_lista[x*2] = exceptions[y]
                feladvany_lista[x*2+1] = ''
        feladvany2 = "".join(feladvany_lista)
    return feladvany2


def play():
    gamediff = difficulty()
    szo = load_words(gamediff)
    feladvany2 = puzzle(szo)
    szo_lista = list(szo)
    feladvany_lista = list(feladvany2)
    tipp_list = []
    upper_list = []
    elet = health(gamediff)
    elet_szam = int(elet)
    elet = str(elet)
    feladvany2 = kitoltes(szo_lista, feladvany_lista, feladvany2)

    while elet_szam > 0:
        if feladvany2 != szo:
            output_tl(tipp_list, upper_list)
            if int(elet) < 10:
                print(pics(gamediff, int(elet)))
            print(feladvany2 + '  -  ' + elet + "HP")
            tipp = input("\nGuess a Letter: ")
            if tipp == szo:
                print("\nJackpot!")
                break
            elif tipp == 'quit':
                break
            elif len(tipp) == 1 and tipp.isalpha():

                if tipp in tipp_list or tipp in exceptions:
                    print(tipp)
                    if tipp in tipp_list:
                        print("\nInput was already used")
                    if tipp in exceptions:
                        print("\nInvalid input.")
                else:

                    if tipp.lower() in szo_lista or tipp.upper() in szo_lista:
                        for x in range(len(szo_lista)):
                            if szo_lista[x] == tipp.lower():
                                feladvany_lista[x*2] = tipp.lower()
                                feladvany_lista[x*2+1] = ''
                            if szo_lista[x] == tipp.upper():
                                feladvany_lista[x*2] = tipp.upper()
                                feladvany_lista[x*2+1] = ''
                        feladvany2 = "".join(feladvany_lista)
                        tipp_list.append(tipp.upper())
                        tipp_list.append(tipp.lower())
                        print("")
                    else:
                        elet = str(elet_szam - 1)
                        elet_szam = elet_szam - 1
                        tipp_list.append(tipp.upper())
                        tipp_list.append(tipp.lower())
                        print("\n-1HP")
            else:
                print("\nInvalid input.")
        else:
            print("\nYou win!")
            break
    else:
        print(pics(gamediff, int(elet)))
        print("\nYou loose! :'( \n------------------")
    retry = input("\nPlay again? [y], [n]: ")
    if retry == "y":
        return play()


play()

for x in range(len(szo_lista)):
                    if szo_lista[x] == tipp:
                        feladvany_lista[x2] = tipp
                        feladvany_lista[x2+1] = ''
            feladvany2 = "".join(feladvany_lista)