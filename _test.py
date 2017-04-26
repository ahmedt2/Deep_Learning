import numpy as np
import itertools
# list(itertools.product(*arrays))
import sys
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

def loadFromFile(_name):
    with open(_name) as f:
        content = f.readlines()
    content = [x.strip("\n") for x in content]
    return content

def get_params(_name):
    content = loadFromFile(_name)
    p = float(content[0])   # Pounds
    m = float(content[1])   # Dollars
    n = float(content[2])   # Num_Items
    c = float(content[3])   # Num_Constraints
    incomp_classes = []
    items = []
    for x in content[3:]:
        if ";" in x:
            temp = x.split(";")
            items.append([float(x) for x in temp[1:]])
        elif ',' in x:
            temp = x.split(",")
            incomp_classes.append([int(u) for u in temp])
    return p, m, n, c, items, incomp_classes

def run_all(_file):
    solutions = []
    for f in _file:
        p, m, n, c, items, incomp_classes = get_params(f)
        solutions.append(\
            solve(p, m, n, c, items, incomp_classes))
    return solutions
def kp_G_A(p=0, m=0, n=0, items=[], c=0, incomp_classes=[], _file="problem1.in"):
    if p == 0 and m==0 and n==0:
        params = get_params(_file)
        p, m, n, c, items, incomp_classes = params[0], params[1],  params[2],  params[3],\
         params[4],  params[5]
    tot = 1
    print(len(incomp_classes))
    s = [len(i) for i in incomp_classes]
    for i in s:
        tot*=i
    print(tot)
    # comb_inc = list(itertools.product(*incomp_classes))
    # return comb_inc