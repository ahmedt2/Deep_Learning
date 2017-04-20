import string
import time
import numpy as np
from itertools import chain, combinations

def weight(item):
    return item[0]

def cost(item):
    return item[1]

def value(item):
    return item[2]
def _powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    # s = list([i for i in range(len(iterable))])
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

A = np.array([[5,7,9],
         [8,8,12],
         [9,10,11],
         [7,6,12],
         [12,10,12]])

def kp_R(p, m, n, items, c=0, incomp_classes=[]):
    knapsack = []
    best_weight = 0
    best_value = 0
    best_cost = 0
    ps = list(powerset(items))
    for i in range(len(ps)):
        if ps[i] == () or ps[i] == []:
            if m > best_value:
                best_weight, best_cost, best_value  = 0, 0, m
        _weight = sum(map(weight, ps[i]))
        _cost = sum(map(cost, ps[i]))
        if _weight > p or _cost > m:
            continue
        val = sum(map(value, ps[i])) + (m - _cost)
        if val > best_value:
            best_weight = _weight
            best_cost = _cost
            best_value = val
            knapsack = ps[i]

    return best_weight, best_cost, best_value
