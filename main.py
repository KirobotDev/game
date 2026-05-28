import random
import os 
import time

print("1. Pierre")
print("2. Fueille")
print("3. Ciseau")

try:
    choix = int(input("Choisis ce que tu va jouer : "))
except ValueError:
    print("Erreur : tu dois taper un nombre (1, 2, 3)")
    exit()
c = choix

def choix_joueur():
    if c < 1 or c > 3:
        print("Choisis un chiffre valide... (1, 2, 3)")

    elif c == 1:
        print("""
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
        """)
    elif c == 2:
        print("""
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """)
    elif c == 3:
        print("""
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
        """)

def choix_desktop():
    random_choices = random.randint(1, 3)
    r = random_choices

    if r == 1:
            print("""
                    _______
                ---'   ____)
                    (_____)
                    (_____)
                    (____)
                ---.__(___)
            """)

    elif r == 2:
            print("""
                _______
            ---'    ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            """)
    elif r == 3:
        print("""
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
        """)
def resultas(joueur, pc): # result function help ai :)
    if joueur == pc:
        return "égalité "
    if (joueur == 1 and pc == 3) or \
       (joueur == 2 and pc == 1) or \
       (joueur == 3 and pc == 2):
          return "Tu a gagnez"
    return "Le pc a gagner !"

r = choix_desktop()
os.system("cls")

print("Tu a fais")
print("")
choix_joueur()
print("")

print("Le pc a fais")
print("")
choix_desktop()

print("")
print(resultas(c, r))
