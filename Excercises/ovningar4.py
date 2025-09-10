import random

def practice_one():
    ten_dice = [random.randint(1,20) for x in range(1,10)]
    ten_dice.sort()
    print(f"{ten_dice} i ordning")
    ten_dice.sort(reverse=True)
    print(f"{ten_dice} i omvänd ordning")
    print(f"{max(ten_dice)} är det största värdet och  {min(ten_dice)} det minsta")

def practice_five_a():
    hundred_dice = [random.randint(1, 6) for x in range(1, 101)]
    print(f"{hundred_dice.count(6)} var antalet 6or och {hundred_dice} är den fulla listan, antal entries var {len(hundred_dice)}")

def practice_five_b():

    iterations = 10
    number_of_sixes = []

    while iterations <= 1000000:    
        dice_rolls = [random.randint(1, 6) for x in range(1, iterations+1)]
        number_of_sixes.append(dice_rolls.count(6))
        print(f"{dice_rolls.count(6)} var antalet 6or, antal entries var {len(dice_rolls)}")
        
        iterations = iterations * 10

    print(f"{number_of_sixes}")    

if __name__ == "__main__":
    practice_five_b()