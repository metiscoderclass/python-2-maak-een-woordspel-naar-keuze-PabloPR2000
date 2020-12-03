import codecs
import random
import pickle
gelezen = False
d = set()
klinkers = ["a", "e", "u", "i", "o"]
medeklinkers = ["b", "c", "d", "f", "g",
                "h", "j", "k", "l", "m", "n",
                "p", "q", "r", "s", "t", "v",
                "w", "x", "y", "z"]
naam = input("Hoe heet jij?")
Score = int(0)
High_score = int(0)

def lees_bestand():
    fobj = codecs.open("nl.txt", "r", "utf-8")
    for line in fobj:
        d.add(line.rstrip())
    fobj.close()
    gelezen = True
    
def bestaat_woord (woord):
    if not gelezen:
        lees_bestand()

    if woord in d:
        return True
    else:
        return False

def Welkom():
    global naam, klinkers, medeklinkers
    print("Welkom " + naam + "! Maak vijf woorden van de volgened letters:")
    q = random.choices(klinkers, k=3)
    w = random.choices(medeklinkers, k=4)
    print(q, w)

def Woord1Raden():
    global Score
    Woord1 = input("Woord 1:")
    if (bestaat_woord(Woord1) == True):
        Punten = int(len(Woord1))
        Score = Score + Punten
        print("Goed! Je hebt nu " + str(Score) + " punten")
    elif (gelezen == False):
        Punten = int(len(Woord1))
        Score = Score - Punten
        print("Dit woord bestaat niet! Je hebt nu " + str(Score) + " punten")

def Woord2Raden():
    global Score
    Woord2 = input("Woord 2:")
    if (bestaat_woord(Woord2) == True):
        Punten = int(len(Woord2))
        Score = Score + Punten
        print("Goed! Je hebt nu " + str(Score) + " punten")
    elif (gelezen == False):
        Punten = int(len(Woord2))
        Score = Score - Punten
        print("Dit woord bestaat niet! Je hebt nu " + str(Score) + " punten")

def Woord3Raden():
    global Score
    Woord3 = input("Woord 3:")
    if (bestaat_woord(Woord3) == True):
        Punten = int(len(Woord3))
        Score = Score + Punten
        print("Goed! Je hebt nu " + str(Score) + " punten")
    elif (gelezen == False):
        Punten = int(len(Woord3))
        Score = Score - Punten
        print("Dit woord bestaat niet! Je hebt nu " + str(Score) + " punten")


def Woord4Raden():
    global Score
    Woord4 = input("Woord 4:")
    if (bestaat_woord(Woord4) == True):
        Punten = int(len(Woord4))
        Score = Score + Punten
        print("Goed! Je hebt nu " + str(Score) + " punten")
    elif (gelezen == False):
        Punten = int(len(Woord4))
        Score = Score - Punten
        print("Dit woord bestaat niet! Je hebt nu " + str(Score) + " punten")


def Woord5Raden():
    global Score
    Woord5 = input("Woord 5:")
    if (bestaat_woord(Woord5) == True):
        Punten = int(len(Woord5))
        Score = Score + Punten
        print("Goed! Je hebt nu " + str(Score) + " punten")
    elif (gelezen == False):
        Punten = int(len(Woord5))
        Score = Score - Punten
        print("Dit woord bestaat niet! Je hebt nu " + str(Score) + " punten")

def SeeYa():
    global Score, naam, High_score
    if (High_score < Score):
        High_score = Score      
    print("Het spel is afgelopen. De hoogste score tot nu toe is " + str(High_score))
    WelNiet = input("Wil je het spel opnieuw spelen " + naam + " (kies j of n) ")
    if (WelNiet ==  "j"):
        Score = 0
        HetSpel()
    else:
        print(" Fijne dag "+ naam +"!")

def HetSpel():
    Welkom()
    Woord1Raden()
    Woord2Raden()
    Woord3Raden()
    Woord4Raden()
    Woord5Raden()
    SeeYa()

HetSpel()
