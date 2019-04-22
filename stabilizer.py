import math

def stress(x):
    return 60*math.sin(x/10) + 100

def maxima(x):
    if(6*math.cos(x/10) == 0):
        if(-(3/5) *math.sin(x/10) > 0):
            return -1
        else:
            return 1
    else:
        return 0



def stressArea(x1, x2):
    return 100*x1 - 600*math.cos(x1/10) - (100*x2 - 600*math.cos(x2/10))

def lineArea(x1, x2):
    m = (stress(x2)-stress(x1))/(x2-x1)
    b = stress(x1)-m*x1

    return (m*x1^2)/2 + b*x1 - ((m*x2^2)/2 + b*x2)


def highest_dif(x0, x1, x2):
    m = (stress(x2) - stress(x1)) / (x2 - x1)
    b = stress(x1) - m * x1

    return m*x0+b


def stabilizer(storage_cap, input_cap, output_cap):
    charge_intervals = []
    dispense_intervals = []
    for i in range(120):
        if maxima(i) == 1:
            x1 = i
            x2 = i
            flip = True
            while highest_dif(i, x1, x2) < output_cap and stressArea(x1,x2)-lineArea(x1,x2) < storage_cap:
                if flip:
                    x1 -= 1
                else:
                    x2 += 1
                flip = not flip
            dispense_intervals.append([x1,x2])
        elif maxima(i) == -1:
            x1 = i
            x2 = i
            flip = True
            while highest_dif(i, x1, x2) < output_cap and lineArea(x1, x2) - stressArea(x1, x2) < storage_cap:
                if flip:
                    x1 -= 1
                else:
                    x2 += 1
                flip = not flip
            charge_intervals.append([x1, x2])
