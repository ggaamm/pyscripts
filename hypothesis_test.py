# hypothesis testing

from math import sqrt

def mean(l):
    return float(sum(l))/len(l)

def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)

def factor(l):
    return 1.96 # this can be enhanced with t-table


def conf(l):
    return factor(l) * sqrt(var(l) / len(l))


def test(l, h):
    #Insert your code here
    m = mean(l)
    c = conf(l)
    return abs(h-m) <= c

l = [199, 200, 201, 202, 203, 204]
h = 201

print(mean(l))
print(conf(l))
print(test(l,h))

