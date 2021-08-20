import random
def game(comp,you):
    if comp==you:
        return "Tie"
    elif comp=='s':
        if you=='w':
            return "you lost"
        elif you =='g':
            return "you win"
    elif comp=='g':
        if you=='w':
            return "you win"
        elif you =='s':
            return "you lost"
    elif comp=='w':
        if you=='s':
            return "you win"
        elif you =='g':
            return "you lost"
    

randNo= random.randint(1,3)
print("comp turn : snake(s) water(w) or gun(g?" )
if randNo==1:
    comp= 's'
elif randNo==2:
    comp= 'w'
elif randNo==3:
    comp= 'g'
you=input("your turn : snake(s) water(w) or gun(g?" )

a=game(comp,you)
print(f'Computer choose  {comp}')
print(f'you choose   {you}')

if a== "Tie":
    print("The game is a tie")
elif a=="you win":
    print("you are winner")
elif a=="you lost":
    print("computer is winner")