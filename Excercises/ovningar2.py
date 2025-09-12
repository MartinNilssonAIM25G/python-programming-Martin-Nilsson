import random

def practice_one():
    i = -10

    while i <= 10:
        
        i += 1

def practice_two_a():
    i = 0
    x = 0

    while i <= 100:
        print(x, end=" ")
        i += 1
        x += i

def practice_two_b():
    i = 1
    x = 0

    while i <= 99:
        x += i
        i += 2 
        print(x, end=" ")
                

def practice_three_a():
    target = random.randint(1,100)
    guess = 0
    attempts = 0
    print(target)
    

    while True:
        guess = int(input("Welcome to guess the numbers game, guess on a number between 1 - 100 and we'll see how close you get and in how many guesses "))
        attempts += 1
        if guess < target:
            print("Please guess higher ")
        elif guess > target:
            print("Please guess lower ")
        else:
            print(f"Correct! {target} was the correct number and you did it in {attempts} attempts")
            break

def practice_three_b():
    target = random.randint(1,100)
    min = 1
    max = 100
    guess = 0
    attempts = 0
    print(target) 

    while True:
        guess = (min+max) // 2
        attempts += 1
        if guess < target:
            print(f"Please guess higher than {guess}  ")
            min = guess + 1
        elif guess > target:
            print(f"Please guess lower than {guess}  ")
            max = guess - 1
        else:
            print(f"Correct! {target} was the correct number and you did it in {attempts} attempts")
            break
    
def practice_four():
    score = 0

    while True:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        

        while True:
             
            target = x * y
            answer = int(input(f"What is {x} times {y}: "))
            
            if answer == target:
                print(f"Correct! {x} * {y} = {answer}")
                score += 1              
                break
            else:
                print(f"Sorry, {x} * {y} is not equal to {answer}")    
                break
                
        play_again = input(f"Would you like to play again? (y, n)").lower()
        if play_again == "y":
            continue
        else:
            print(f"Thanks for playing!, you got {score} correct guesses")
            break

def practice_five_a():
    sum = 1
    term = 1/2
    n = 20
    i = 0

    while i < n:
        sum = sum + term
        term = term/2
        print(sum)
        i += 1

def practice_five_b():
    sum = 1
    denom = 3
    sign = -1
    term = 1 / denom

    while term > 1e-6:
        sum += sign * term
        denom += 2
        sign = -sign
        term = 1 / denom
        print(sum)
      


if __name__ == "__main__":
    practice_five_b()