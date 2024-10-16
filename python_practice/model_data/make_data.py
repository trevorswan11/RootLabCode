from math import sin, e

data = []

def make_data(func):    
    # create some model data 
    for i in range(0, 1000):
        data.append([ i, func(i) ])
    
    # make a csv file with the data
    with open(f"{func.__name__}_data.csv", 'w') as f:
        for row, col in data:
            f.write(f"{row if row > 0 else 'NaN'},{col if (row % 300 != 0) else 'NaN'}\n")

def keplers_equation(val):
    return val - e * sin(val)
    
make_data(keplers_equation)
    