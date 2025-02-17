import art
import random
print(art.logo)
a=list(range(1,101))
number = random.choice(a)


choice = input("Enter Hard or Easy").lower()
if choice=='hard':
    life=5
    print(f"You've {life} attempts to guess the number")
elif choice == 'easy':
    life =10
    print(f"You've {life} attempts to guess the number")
else:
    life = 5
    print(f"You entered invalid input so by default you have {life} attemps to guess the number")
def guess(user):
    if user==number:
        print("You got the Correct Number You Won")
        return True
    elif user < number:
        print("Too Low")
    else:
        print("Too High")
    return False

while life>0:
    try:
        user = int(input("make a guess"))
        if guess(user):
            break
        life-=1
        print(f"You have {life} attempts remaining")
    except ValueError:
        print("you enter invalid input")

if life == 0:
    print(f"You ran out attempts You lose the correct number was {number}")
