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
    

if __name__ == "__main__":
    practice_three_b()