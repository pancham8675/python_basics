
import random

def game_win(comp, you):
    if comp==you:
        return None

    elif comp=="rock":
        if you=="paper":
            return True
        elif you=="scissors":
            return False
    
    elif comp=="paper":
        if you=="scissors":
            return True
        elif you=="rock":
            return False
    
    elif comp=="scissors":
        if you=="rock":
            return True
        elif you=="paper":
            return False


print("Computer's turn:\n 1. Rock\n 2. Paper\n 3. Scissors\nComputer has chosen.\n")
rand_num = random.randint(1, 3)

if rand_num==1:
    comp="rock"
elif rand_num==2:
    comp="paper"
elif rand_num==3:
    comp="scissors"

you=input("Your turn:\n 1. Rock\n 2. Paper\n 3. Scissors\nEnter your choice(rock,paper or scissors): ")

# if y==1:
#     you="rock"
# elif y==2:
#     you="paper"
# elif y==3:
#     you="scissors"
# else:

result= game_win(comp, you)

print(f"\nComputer chose {comp}")
print(f"You chose {you}")

if result==False:
    print("You lose")
elif result==True:
    print("You win!")
elif result==None:
    print("It's a tie!")
