def practice_one():
    while True:
        number = int(input("Please input a number: "))

        if number == 0:
            print("Ditt tal var noll")
        elif number > 0:
            print("Ditt tal var positivt")
        else:
            print("Ditt tal var negativt") 

def practice_two():
    while True:
        first_number = int(input("Please input the first number for comparison: "))
        second_number = int(input("Please input the second number for comparison: "))

        if first_number < second_number:
            print(f"{first_number} was the smallest number")
        elif second_number < first_number:
            print(f"{second_number} was the smallest number")
        else:
             print(f"{first_number} and {second_number} is the same.")   

def get_valid_angle(prompt, min_val=None, max_val=None):
    while True:
        try:
            i = int(input(prompt.strip()))
            if min_val is not None and i < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and i > max_val:
                print(f"Value must be at most {max_val}.")
                continue
            return i
        except ValueError:
            print("Please enter a number.")

def validate_triangle(angle_one, angle_two, angle_three):
    if angle_one+angle_two+angle_three != 180:
        print(f"{angle_one} + {angle_two} + {angle_three} does not equal 180 and this is not a valid triangle.")
    else:
        print(f"{angle_one} + {angle_two} + {angle_three} Nice! This adds up to 180 degrees and we can create a triangle!")
        

def practice_three():
    while True:
        print("Please enter three angles to create a triangle, they must be positive and the total should add up to 180 degrees")
        angle_one = get_valid_angle(("Please enter the first angle: "),0,60)
        angle_two = get_valid_angle(("Please enter the second angle: "),0,60)
        angle_three = get_valid_angle(("Please enter the third angle: "),0,60)

        validate_triangle(angle_one, angle_two, angle_three)

def practice_four():
    while True:
        print("To know how many pills you can take, please enter age and weight.")
        
        age = int(input("Please enter your age: "))
        weight = int(input("Please enter your weight: "))

        if age > 12 or (age >= 7 and weight > 40):
            print("Please take 1-2 pills.")
        elif weight > 26:
            print("Please take 1/2 - 1 pill")
        else:
             print("Please take 1/2 pill")

def practice_five():
    while True:
        print("Time to check some odd numbers or even, whatever floats your boat")
        number = int(input("Please enter an integer: ")) 

        if number % 5 == 0:
            print(f"{number} is divisible by 5")    
        if number % 2 == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")

def practice_six():
    while True:
        print("Welcome to our luggage size controller, your luggage must at most be 8kg and dimensions 55x40x23cm (lenght x width x height)")
        weight = int(input("Please enter the weight of your luggage (kg): "))
        length = int(input("Please enter the lenght (cm): "))
        width = int(input("Please enter the width (cm): "))
        height = int(input("Please enter the height (cm): "))

        print(f"You've given us {weight}kg, {length}cm, {width}cm, {height}cm")

        if all([weight <= 8, length <= 55, width <= 40, height <= 23]):
            
            print("Perfect, your luggage is ready for travel.")
        else:
            print("Were sorry, but this luggage will not be traveling with us tonight. ")    


if __name__ == "__main__":
    practice_six()