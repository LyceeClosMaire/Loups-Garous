# Créé par martelet, le 13/03/2017 en Python 3.2
import random
Roles = [1,58,69,84]
def start_game ():
    r = random.choice(Roles)
    Roles.pop(r)
for i in Roles:
    start_game()
    print(i)