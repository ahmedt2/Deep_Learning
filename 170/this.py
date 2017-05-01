
def write(prob,probs,_f="here.txt"):
    _max = probs[0]
    ks = probs[1]
    f = open(_f.strip(".in")+".out", 'w')
    f.write("FILE: " + prob + '\n')
    f.write("Max Score: \n")
    f.write(str(_max) +'\n')
    f.write("KnapSack: \n")
    for i in ks:
        f.write(str(i) + '\n')

def help(_name):
    print_me = []
    all_probs=["problem1.in", "problem2.in","problem3.in","problem4.in","problem5.in", "problem6.in","problem7.in", "problem8.in", "problem9.in", "problem10.in", "problem11.in", "problem12.in", "problem13.in", "problem14.in", "problem15.in", "problem16.in", "problem17.in", "problem18.in", "problem19.in", "problem20.in", "problem21.in"]
    for prob in  all_probs:
        file_R = prob.strip(".in") + ".out"
        file_G = prob.strip(".in") + "_greedy.out"
        content_R = loadFromFile(file_R)
        content_G = loadFromFile(file_G)
        score_R = float(content_R[2])   # Pounds
        score_G = float(content_G[2])   # Dollars
        if score_G >= score_R:
            print_me.append[content_G[0],content_G[2]]
        else:
            print_me.append[content_R[0],content_R[2]]

    f = open("best_scores.txt", 'w')
    for p in print_me:
        f.write(p[0], ": ", p[1], " \n")