import math
def mean(x):
    return sum(x)/len(x)


def sd(x):
    m = mean(x)
    ss = sum((i-m)**2 for i in x)
    return math.sqrt(ss/len(x))

def corr(x,y):
    x_m = mean(x)
    y_m = mean(y)
    xy_d = []
    for i in range(len(x)):
        x_d = x[i]-x_m
        y_d = y[i]-y_m
        xy_d.append(x_d*y_d)
    return mean(xy_d)/(sd(x)*sd(y))

