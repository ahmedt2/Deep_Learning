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
    comb_inc = list(itertools.product(*incomp_classes))
    set_of_inc_clss = set([x[0] for x in items])
    _dic = dict()
    for i in set_inc_clss:
        _dic[str(i)] = []
    for i in set_inc_clss:
        for x in items:
            if x[0] == i:
                _dic[str(i)].append(x[1:])

    best = []  # LIST: [ COMB, MAX_VALUE ] 
    for comb in comb_inc:
        curr_items = []
        for _class in comb:
            curr_items.extend(_dic[str(_class)])            

        lst1, lst2, lst3, lst4, lst5, lst6, sorted_lsts = [], [], [], [], [], [], []
        for it in items:
            try:
                lst1.append((it, it[1]/it[0]))
            except Exception:
                lst1.append((it, 10000000000))
            try:
                lst2.append((it, it[2]/it[0]))
            except Exception:
                lst2.append((it, 10000000000))
            try:
                lst3.append((it, (it[2]-it[1])/it[0]))
            except Exception:
                lst3.append((it, 10000000000))
            try:
                lst4.append((it, (it[2]/it[1])/it[0]))
            except Exception:
                lst4.append((it, 10000000000))
            try:
                lst5.append((it, it[2]/it[1]))
            except Exception:
                lst5.append((it, 10000000000))
            try:
                lst6.append((it, it[2]/(it[1]+it[0])))
            except Exception:
                lst6.append((it, 10000000000))
        for lst in [lst1, lst2, lst3, lst4, lst5, lst6]:
            sorted_lsts.append(sorted(lst, key = lambda x: x[1]))
        sols = []
        u, leave = 1, []
        for lst in sorted_lsts:
            knapsack, tot_weight,tot_value,tot_cost = [],0,0,0
            while len(lst) > 0:
                item = lst.pop()[0]
                if (weight(item) + tot_weight) <= p and (cost(item) + tot_cost) <= m:
                    knapsack.append(item)
                    tot_weight += weight(item)
                    tot_value += value(item)
                    tot_cost += cost(item)
                    leave.append([knapsack, tot_value+(m-tot_cost)])
                else:
                    leave.append([knapsack, tot_value+(m-tot_cost)])
                    break
            sols.append([u, tot_value + (m-tot_cost)])
            u+=1
        leave.extend(sols)
        sor = sorted(leave, key=lambda x: x[1])
        max_val = sor[-1]
        best.append([comb, max_val, sols])
    return sorted(best, key = lambda x: x[1])