import random
import matplotlib.pyplot as plt
import math

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

    for sixes in list:
        result = round(sixes / iterations, 4)

    return result
#Mitt första försök till att lösa uppgift 5b
#def plot_list(sixes, rolls):
    plt.plot(sixes, '-*')
    plt.title("Probability of six for different number of rolls")
    plt.xticks([0,1,2,3,4,5], rolls)
    plt.xlabel("Number of dice rolls")
    plt.ylabel("Probability")
    plt.show()
#def calculate_procentage(list, iterations):    
#def practice_five_b():
    iterations = 10
    number_of_sixes = []
    sixes_in_procentage = []
    num_rolls = [10, 100, 1000, 10000, 100000, 1000000]

    while iterations <= 1000000:    
        dice_rolls = [random.randint(1, 6) for x in range(1, iterations+1)]
        number_of_sixes.append(dice_rolls.count(6))
        #print(f"{dice_rolls.count(6)} var antalet 6or, antal entries var {len(dice_rolls)}")
        sixes_in_procentage.append(calculate_procentage(number_of_sixes, iterations))
        iterations = iterations * 10
        
    print(f"{sixes_in_procentage}") 
    print(f"{number_of_sixes}")
    plot_list(sixes_in_procentage, num_rolls)

def practice_five_bb():
    number_of_rolls = [10,100,1000,10000,100000,1000000]
    number_of_sixes = [sum(1 for _ in range(iterations) if random.randint(1,6)==6) for iterations in number_of_rolls]    
    probability_six = [sum(1 for _ in range(N) if random.randint(1,6)==6)/N for N in number_of_rolls]
    
    print(f"{number_of_sixes} var antalet 6or, procentuppdelningen är som följer {probability_six}")
    plt.plot(probability_six, '-*')
    plt.title("Probability of six for different number of rolls")
    plt.xticks([0,1,2,3,4,5], number_of_rolls)
    plt.xlabel("Number of dice rolls")
    plt.ylabel("Probability")
    plt.show()

def practice_six():
    iterations = 5000
    x_points = [random.uniform(-1,1) for _ in range(iterations)]
    y_points = [random.uniform(-1,1) for _ in range(iterations)]
    distance = [math.sqrt(x_points[i]**2 + y_points[i]**2) for i in range(iterations)]
    colors = ['green' if distance[i] <= 1 else 'purple' for i in range(iterations)]
    inside_circle = 0

    plt.scatter(x_points, y_points, c=colors)
    plt.show()

    for v in distance:
        if v <= 1:
            inside_circle += 1
    print(inside_circle)

    print(f"Is it pi? {4*(inside_circle/iterations)}")

def practice_seven():
    # A: My choice would be door B, a snake is shown in door C, then i would change to door A.
    # When you first choose your door you have 1/3 chances to be correct, if one gets removed it's now 2/3 chances to be correct as you know one of the doors which are a snake
    
    number_of_iterations = [10,100,1000,10000,100000,1000000]
    stay_probability = []
    switch_probability = []

    for N in number_of_iterations:
        stay_wins = sum(1 for _ in range(N) if random.randint(0,2) == random.randint(0,2))
        stay_probability.append(stay_wins / N)

        switch_wins = sum(1 for _ in range(N) if random.randint(0,2) != random.randint(0,2))
        switch_probability.append(switch_wins / N)
        
    plt.figure(figsize=(10, 6))
    plt.plot(number_of_iterations, stay_probability, linestyle='--', marker='o', label="Stay")
    plt.plot(number_of_iterations, switch_probability, linestyle='--', marker='o', label="Switch")
    plt.xscale('log')
    plt.xticks(
    [10, 100, 1000, 10000, 100000, 1000000],  # tick positions
    ['10', '100', '1000', '10000', '100000', '1000000']  # labels som strängar
    )
    plt.xlabel("Number of simulations")
    plt.ylabel("Proportion Wins")
    plt.title("Proportion of wins are 2/3 compared to 1/3 when switching")
    plt.legend()
    plt.grid(True)   
    plt.show()


if __name__ == "__main__":
    practice_seven()

