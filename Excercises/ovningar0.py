import math

def pythagoeran_theorem():
    a = 3
    b = 4

    print(f"The hypothenuse is {round(math.sqrt(a**2 + b**2))} length units")

    a = 5
    c = 7

    print(f"The other cathetus is {round(math.sqrt(c**2 - a**2), 2)} length units")

def classification_accuracy_a():
    a = 365
    b = 300

    print(f"Accuracy is {round((b/a)*100, 2)}%")    

def classification_accuracy_b():
    tp = 2
    fp = 2
    fn = 11
    tn = 985

    print(f"The accuracy of this model is {round((tp+tn)/(tp+tn+fp+fn), 4)}")

def line():
    x1, y1 = 4, 4
    x2, y2 = 0, 1

    k = ((y2 - y1) / (x2 - x1))
    m = 1 -(k*0)

    print(f"k = {k}, m = {m}, so the equation for the slope is y = {k}x + {round(m)}")

def euclidean_distance():
    p1x, p1y = 3, 5
    p2x, p2y = -2, 4

    print(f"The distance is around {round(math.sqrt((p2x-p1x)**2 + (p2y - p1y)**2), 2)}")

def euclidean_distance_3D():
    p1x, p1y, p1z = 2,1,4
    p2x, p2y, p2z = 3,1,0

    print(f"The distance is around {round(math.sqrt((p2x-p1x)**2 + (p2y - p1y)**2 + (p2z - p1z)**2), 2)}")

if __name__ == "__main__":
    euclidean_distance_3D()