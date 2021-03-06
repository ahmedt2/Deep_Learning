import string
import time
import numpy as np
from itertools import chain, combinations
import random
import numpy as np
import itertools
# list(itertools.product(*arrays))
import sys
import string
import time
import numpy as np
from itertools import chain, combinations

def weight(item):
    return item[2]

def cost(item):
    return item[3]

def value(item):
    return item[4]

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
            t = [temp[0]]
            t.extend([float(x) for x in temp[1:]])
            items.append(t)

        elif ',' in x:
            temp = x.split(",")
            incomp_classes.append([int(u) for u in temp])
    return p, m, n, c, items, incomp_classes

def Master():
    problems = {}
    all_probs=["problem1.in", "problem2.in","problem3.in","problem4.in","problem5.in", "problem6.in","problem7.in", "problem8.in", "problem9.in", "problem10.in", "problem11.in", "problem12.in", "problem13.in", "problem14.in", "problem15.in", "problem16.in", "problem17.in", "problem18.in", "problem19.in", "problem20.in", "problem21.in"]
    all_probs_22=["problem3.in","problem4.in","problem8.in", "problem13.in", "problem14.in", "problem16.in", "problem17.in", "problem20.in", "problem21.in"]
    all_probs_17=["problem1.in","problem10.in", "problem11.in"]
    all_probs_12=["problem5.in", "problem6.in","problem12.in"]
    all_probs_8=["problem2.in","problem7.in", "problem9.in","problem15.in",  "problem18.in", "problem19.in"]
    all_probs_6 = ["problem2.in","problem7.in", "problem18.in", "problem19.in"]
    all_probs_3 = ["problem9.in","problem15.in"]
    for problem in all_probs:
        problems[problem] = []
    for i in range(100):
        for prob in all_probs_22:
            s, k = kp_R(_file="problem1.in", num=22)
            max_s=max(s)
            max_k=k[s.index(max(s))]
            if problems[prob][0] < max_s:
                problems[prob][0] = max_s
                problems[prob][1] = max_k
        for prob in all_probs_17:
            s, k = kp_R(_file="problem1.in", num=17)
            max_s=max(s)
            max_k=k[s.index(max(s))]
            if problems[prob][0] < max_s:
                problems[prob][0] = max_s
                problems[prob][1] = max_k
        for prob in all_probs_12:
            s, k = kp_R(_file="problem1.in", num=12)
            max_s=max(s)
            max_k=k[s.index(max(s))]
            if problems[prob][0] < max_s:
                problems[prob][0] = max_s
                problems[prob][1] = max_k
        for prob in all_probs_8:
            s, k = kp_R(_file="problem1.in", num=8)
            max_s=max(s)
            max_k=k[s.index(max(s))]
            if problems[prob][0] < max_s:
                problems[prob][0] = max_s
                problems[prob][1] = max_k
        for prob in all_probs_6:
            s, k = kp_R(_file="problem1.in", num=6)
            max_s=max(s)
            max_k=k[s.index(max(s))]
            if problems[prob][0] < max_s:
                problems[prob][0] = max_s
                problems[prob][1] = max_k
        for prob in all_probs_3:
            s, k = kp_R(_file="problem1.in", num=3)
            max_s=max(s)
            max_k=k[s.index(max(s))]
            if problems[prob][0] < max_s:
                problems[prob][0] = max_s
                problems[prob][1] = max_k
    return problems
def _powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    # s = list([i for i in range(len(iterable))])
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# A = np.array([[5,7,9],
#          [8,8,12],
#          [9,10,11],
#          [7,6,12],
#          [12,10,12]])

def make_dict(items, incomp_classes):
    set_of_inc_clss = set([x[1] for x in items])
    _dic = dict()
    j = 0
    for i in set_of_inc_clss:
        _dic[str(int(i))] = set()
    for i in incomp_classes:
        for classes in i:
            try:
                _dic[str(classes)].update(i)
            except KeyError:
                continue
    return _dic

def check_valid(items, incomp_classes, _dict):
    st = time.clock()
    classes = []
    for item in items:
        classes.append(item[1])
    for cls in classes:
        c = 0
        for _cls in classes:
            if _cls in _dict[str(int(cls))] and _cls != cls:
                c += 1
        if c >= 1:
            return False
    ed = time.clock()
    print("CHECK-VALIDATION TIME = ", ed-st)
    return True

def kp_R(p=0, m=0, n=0, items=[], c=0, incomp_classes=[], _file="problem1.in", num=10):
    if p == 0 and m==0 and n==0:
        params = get_params(_file)
        p, m, n, c, items, incomp_classes = params[0], params[1],  params[2],  params[3],\
        params[4],  params[5]
    scoress = []
    knapsackss = []
    _dict = make_dict(items, incomp_classes)

    for u in range(1000):
        knapsack = []
        best_weight = 0
        best_value = 0
        best_cost = 0
        st = time.clock()
        sample = random.sample(items, num)
        while not check_valid(sample, incomp_classes, _dict):
            sample = random.sample(items, 17)
        ed = time.clock()
        print("GETTING-VALID = ", ed-st)
        st = time.clock()
        ps = list(powerset(sample))
        ed = time.clock()
        print("POWER-SET = ", ed-st)
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
                best_weight, best_cost, best_value, knapsack = _weight, _cost, val, [item[0] for item in ps[i]]

        scoress.append(best_value)
        knapsackss.append(knapsack)

    return scoress, knapsackss

# A = [i for i in range(30)]
# st = time.clock()
# u = list(powerset(A))
# ed = time.clock()
# print("time = ", ed-st)

# st = time.clock()
# s, k = kp_R(_file="problem1.in")
# ed = time.clock()
# print("time = ", ed-st)
# max(s)
# k[s.index(max(s))]

# params = get_params("problem10.in")
# d = make_dict(params[4], params[5])
# for i in range(100000):
#     sample = random.sample(params[4], 22)
#     u = check_valid(sample,2,d)
#     check_valid(sample,2,d)
#     if u == True:
#         print("WINNEERRRR!!!")
#         print(i)
#         break
