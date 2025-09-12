import random

def practice_one_a():
    for i in range(-10, 11, 1):
        print(i, iend=" ")

def practice_one_b():
    for i in range(-10, 11, 2):
        print(i, end=" ")       

def practice_two_a():
    total = 0
    for i in range(1, 101):  
        total += i  
        print(total, end=" ")

def practice_two_b():
    total = 0
    for i in range(1, 101, 2):
        total += i
        print(total, end=" ")

def practice_three_a():
    number = 6
    for i in range(1,11):
        print(number * i, end=" ")

def practice_three_b():
    table = int(input("Which table are you interested in?: "))
    start = int(input("Please specify start of table: "))
    end = int(input("Plase specify end of table: "))

    for i in range(start, end + 1):
        print(table * i, end=" ")

def practice_three_c():
    for i in range(0, 11):
        for x in range (0, 11):
            print(f" {i*x:<2} ", end=" ")
        print(f" ", end="\n")

def practice_four():
     
    faculty = int(input("Which number should we evaluate faculty on today?: "))
    fact = 1
    for i in range(1, faculty+1):
        fact = fact * i

    print(f"The factorial of {faculty} is: {fact}", end=" ")

def practice_five():
    target = random.randint(1, 10000)

    for attempt in range(100):
        guess = int(input("What's your guess?: "))

        if guess < target:
            print("Please guess higher ")
        elif guess > target:
            print("Please guess lower ")
        else:
            print(f"Correct! {target} was the correct number")
            break


def practice_six():
    grain = 1
    total_grain = 0
    for i in range(64):
        total_grain += grain
        grain *= 2
    print(total_grain)    

if __name__ == "__main__":
    practice_five()