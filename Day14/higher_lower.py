from game_data import data
import art
import random

# Initialize variables
a = random.choice(data)
correct_counter = 0


def comparision(a):
    b = random.choice(data)
    while a == b:
        b = random.choice(data)

    print('\n' * 5)
    print(art.logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    return b  # return the new b for comparison


while True:
    b = comparision(a)  # get the new b from the function
    user = input("Enter A or B:\t").lower()

    if user == 'a':
        if a['follower_count'] > b['follower_count']:
            correct_counter += 1
            a = b  # update 'a' to the correct choice b
            print(f"Correct! Current score: {correct_counter}")
        else:
            print(f"Wrong! Your final score is: {correct_counter}")
            break
    elif user == 'b':
        if b['follower_count'] > a['follower_count']:
            correct_counter += 1
            a = b  # update a to the correct choice b
            print(f"Correct! Current score: {correct_counter}")
        else:
            print(f"Wrong! Your final score is: {correct_counter}")
            break
    else:
        print("Invalid input. Please enter 'A' or 'B'.")
