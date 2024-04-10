import random
import io
import sys

class var:
    def __init__(self, symbol, sign='+'):
        self.symbol=symbol
        self.sign=sign
    
#############    utilities for boolean algebra (conversions from one form to another and evaluations)

def get_starting_character(num_vars):
    rnd = random.randint(1,3)
    if rnd == 1:
        character = 'A'
    elif rnd == 2:
        character = chr(ord('Z') - num_vars)
    else:
        character = 'M'
    return character

def gen_random_exp(num_vars): #generating in postfix
    limit=random.randint(1,5) # lim on terms
    vars=[]
    character = get_starting_character(num_vars)
    for i in range (num_vars):
        vars.append(var(chr(ord(character)+i), "+"))
        vars.append(var(chr(ord(character)+i), "-"))
    stack=[]
    st_vars=0
    st_op=0
    probab=4 # probability of extending literals in the term
    while True:
        if limit>0 and random.randint(1,10)<probab:
            limit-=1
            random_index=random.randint(0, len(vars)-1)
            stack.append(vars[random_index])
            st_vars+=1
        elif st_op<st_vars-1:
            if random.randint(0,1)==0:
                stack.append(".")
            else:
                stack.append("+")
            st_op+=1
        elif limit==0:
            break
    return stack


def print_exp(exp):
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    stack=[]
    for i, val in enumerate(exp):
        if isinstance(val, str):
            var1=stack.pop()
            var2=stack.pop()
            res_var=f"({var1} {val} {var2})"
            stack.append(res_var)
        else:
            string=val.symbol
            if val.sign=="-":
                string=string+"'"
            stack.append(string)
            
    sys.stdout = sys.__stdout__
    captured_output = output_buffer.getvalue()
    return stack[0]


def gen_random_truth_table(num_vars):   #num_vars uptill 26 only for now.. practically 5-6 variable are required to generate question
    table=[]
    for i in range(2**num_vars):
        temp=format(i, f'0{num_vars}b')
        list=[int(bit) for bit in temp]
        list.append(random.randint(0,1))
        table.append(list)
    return table


def minterm_to_table(minterms, num_vars):
    table=[]
    for i in range(2**num_vars):
        temp=format(i, f'0{num_vars}b')
        list=[int(bit) for bit in temp]
        if i in minterms:
            list.append(1)
        else:
            list.append(0)
        table.append(list)
    return table


def gen_sop(table):
    num_vars=len(table[0])-1
    sop=[]
    character = get_starting_character(num_vars)
    for i in range (len(table)):
        if table[i][num_vars]==1:
            prod=[]
            for val in range(num_vars):
                if table[i][val]==1:
                    sym="+"
                else:
                    sym="-"
                prod.append(var(chr(ord(character)+val), sym))
            sop.append(prod)
    return sop


def gen_pos(table):
    num_vars=len(table[0])-1
    pos=[]
    character = get_starting_character(num_vars)
    for i in range (len(table)):
        if table[i][num_vars]==0:
            prod=[]
            for val in range(num_vars):
                if table[i][val]==1:
                    sym="+"
                else:
                    sym="-"
                prod.append(var(chr(ord(character)+val), sym))
            pos.append(prod)
    return pos


def print_sop(sop):
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    for i, prod in enumerate(sop):
        print("(", end="")
        for j, vars in enumerate(prod):
            print("{0}".format(vars.symbol), end="")
            if vars.sign=="-":
                print("'", end="")
            if j!=len(prod)-1:
                print(".", end="")
        print(")", end="")
        if i!= len(sop)-1:
            print("+", end="")

    sys.stdout = sys.__stdout__
    captured_output = output_buffer.getvalue()
    return captured_output

print(print_sop(gen_sop(gen_random_truth_table(4))))

def print_pos(pos):
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    for i, prod in enumerate(pos):
        print("(", end="")
        for j, vars in enumerate(prod):
            print("{0}".format(vars.symbol), end="")
            if vars.sign=="-":
                print("'", end="")
            if j!=len(prod)-1:
                print("+", end="")
        print(")", end="")
        if i!= len(pos)-1:
            print(".", end="")

    sys.stdout = sys.__stdout__
    captured_output = output_buffer.getvalue()
    return captured_output


def table_to_minterms(table):
    minterms = []
    res=len(table[0])-1
    for i in range (len(table)):
        if table[i][res]==1:
            minterms.append(i)
    return minterms, res


######################   utilities for qm method   #############################

def mul(x,y):
    res = []
    for i in x:
        if i+"'" in y or (len(i)==2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            res.append(i)
    return res

def multiply(x,y):
    res = []
    for i in x:
        for j in y:
            tmp = mul(i,j)
            res.append(tmp) if len(tmp) != 0 else None
    return res

def refine(my_list,dc_list):
    res = []
    for i in my_list:
        if int(i) not in dc_list:
            res.append(i)
    return res

def findEPI(x):
    res = []
    for i in x:
        if len(x[i]) == 1:
            res.append(x[i][0]) if x[i][0] not in res else None
    return res

def findVariables(x):
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append(chr(i+65)+"'")
        elif x[i] == '1':
            var_list.append(chr(i+65))
    return var_list

def flatten(x):
    flattened_items = []
    for i in x:
        flattened_items.extend(x[i])
    return flattened_items

def findminterms(a): 
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a,2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
    temp = []
    for i in range(pow(2,gaps)):
        temp2,ind = a[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

def compare(a,b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_index = i
            c += 1
            if c>1:
                return (False,None)
    return (True,mismatch_index)

def removeTerms(_chart,terms):
    for i in terms:
        for j in findminterms(i):
            try:
                del _chart[j]
            except KeyError:
                pass

def print_QM(mt, dc):
    mt.sort()
    minterms = mt+dc
    minterms.sort()
    size = len(bin(minterms[-1]))-2
    groups,all_pi = {},set()

    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]

    while True:
        tmp = groups.copy()
        groups,m,marked,should_stop = {},0,set(),True
        l = sorted(list(tmp.keys()))
        for i in range(len(l)-1):
            for j in tmp[l[i]]:
                for k in tmp[l[i+1]]:
                    res = compare(j,k)
                    if res[0]:
                        try:
                            groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None
                        except KeyError:
                            groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]]
                        should_stop = False
                        marked.add(j)
                        marked.add(k)
            m += 1
        local_unmarked = set(flatten(tmp)).difference(marked)
        all_pi = all_pi.union(local_unmarked)
        if should_stop:
            break

    sz = len(str(mt[-1]))
    chart = {}

    for i in all_pi:
        merged_minterms,y = findminterms(i),0

        for j in refine(merged_minterms,dc):
            x = mt.index(int(j))*(sz+1)
            y = x+sz
            try:
                chart[j].append(i) if i not in chart[j] else None
            except KeyError:
                chart[j] = [i]

    EPI = findEPI(chart)
    removeTerms(chart,EPI)

    if(len(chart) == 0):
        final_result = [findVariables(i) for i in EPI]
    else:
        P = [[findVariables(j) for j in chart[i]] for i in chart]
        while len(P)>1:
            P[1] = multiply(P[0],P[1])
            P.pop(0)
        final_result = [min(P[0],key=len)]
        final_result.extend(findVariables(i) for i in EPI)
    return "{0}".format('F = '+' + '.join(''.join(i) for i in final_result))


def bit_flip_var(x):
    var_list = []
    for i in range(len(x)):
        if(random.randint(0,1)==0):
            if x[i] == '0':
                var_list.append(chr(i+65))
            elif x[i] == '1':
                var_list.append(chr(i+65)+"'")
        else:
            if x[i] == '0':
                var_list.append(chr(i+65)+"'")
            elif x[i] == '1':
                var_list.append(chr(i+65))
    return var_list


def print_QM_distract(mt, dc):
    mt.sort()
    minterms = mt+dc
    minterms.sort()
    size = len(bin(minterms[-1]))-2
    groups,all_pi = {},set()

    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]

    while True:
        tmp = groups.copy()
        groups,m,marked,should_stop = {},0,set(),True
        l = sorted(list(tmp.keys()))
        for i in range(len(l)-1):
            for j in tmp[l[i]]:
                for k in tmp[l[i+1]]:
                    res = compare(j,k)
                    if res[0]:
                        try:
                            groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None
                        except KeyError:
                            groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]]
                        should_stop = False
                        marked.add(j)
                        marked.add(k)
            m += 1
        local_unmarked = set(flatten(tmp)).difference(marked)
        all_pi = all_pi.union(local_unmarked)
        if should_stop:
            break

    sz = len(str(mt[-1]))
    chart = {}

    for i in all_pi:
        merged_minterms,y = findminterms(i),0

        for j in refine(merged_minterms,dc):
            x = mt.index(int(j))*(sz+1)
            y = x+sz
            try:
                chart[j].append(i) if i not in chart[j] else None
            except KeyError:
                chart[j] = [i]

    EPI = findEPI(chart)
    removeTerms(chart,EPI)

    if(len(chart) == 0):
        final_result = [bit_flip_var(i) for i in EPI]
    else:
        P = [[bit_flip_var(j) for j in chart[i]] for i in chart]
        while len(P)>1:
            P[1] = multiply(P[0],P[1])
            P.pop(0)
        final_result = [min(P[0],key=len)]
        final_result.extend(bit_flip_var(i) for i in EPI)
    return "{0}".format('F = '+' + '.join(''.join(i) for i in final_result))


def manipulate_minterms(table):
    mt, num_vars = table_to_minterms(table)
    for i in range (len(table)):
        if i not in mt and random.randint(0,6)<=1:
            mt.append(i)
        if i in mt and random.randint(0,6)<=1:
            mt.remove(i)
    return mt


def manipulate_dc(table):
    dc=[]
    mt, num_vars = table_to_minterms(table)
    for i in range (len(table)):
        if i not in mt and random.randint(0,6)<=1:
            dc.append(i)
    return dc


####   question templates  ############################

def sop_to_minterm():
    table = gen_random_truth_table(3)
    sop = gen_sop(table)
    minterms = table_to_minterms(table)
    question = "What are the minterms for the given sop expression: {0}".format(print_sop(sop))
    answer = minterms[0]
    options=[]
    while len(options)<3:
        m=manipulate_dc(table)
        if m:
            options.append(m)
    options.append(minterms[0])
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer

def pos_to_minterm():
    table = gen_random_truth_table(3)
    pos = gen_pos(table)
    minterms = table_to_minterms(table)
    question = "What are the minterms for the given pos expression: {0}".format(print_pos(pos))
    answer = minterms[0]
    options=[]
    while len(options)<3:
        m=manipulate_dc(table)
        if m:
            options.append(m)
    options.append(minterms[0])
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer

def sop_to_pos():
    table = gen_random_truth_table(3)
    sop = gen_sop(table)
    minterms, num = table_to_minterms(table)
    pos = gen_pos(table)
    question = "Convert the expression {0} to POS form".format(print_sop(sop))
    answer = print_pos(pos)
    options=[]
    options.append(answer)
    for i in range(3):
        options.append(print_pos(gen_pos(minterm_to_table(manipulate_minterms(table), num))))
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer

def pos_to_sop():
    table = gen_random_truth_table(3)
    sop = gen_sop(table)
    minterms, num = table_to_minterms(table)
    pos = gen_pos(table)
    question = "Convert the expression {0} to SOP form".format(print_pos(pos))
    answer = print_sop(sop)
    options=[]
    options.append(answer)
    for i in range(3):
        options.append(print_sop(gen_sop(minterm_to_table(manipulate_minterms(table), num))))
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer

def minterm_to_sop():
    table = gen_random_truth_table(3)
    sop = gen_sop(table)
    minterms, num = table_to_minterms(table)
    question = "The SOP for the given minterms - {0} is?".format(minterms)
    answer = print_sop(sop)
    options=[]
    options.append(answer)
    for i in range(3):
        options.append(print_sop(gen_sop(minterm_to_table(manipulate_minterms(table), num))))
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer

def minterm_to_pos():
    table = gen_random_truth_table(3)
    pos = gen_pos(table)
    minterms, num = table_to_minterms(table)
    question = "The POS for the given minterms - {0} is?".format(minterms)
    answer = print_pos(pos)
    options=[]
    options.append(answer)
    for i in range(3):
        options.append(print_pos(gen_pos(minterm_to_table(manipulate_minterms(table), num))))
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer


#evaluate the given expression 
def evaluate():
    num_vars=random.randint(3,4)
    exp=gen_random_exp(num_vars)
    final_exp=print_exp(exp)
    mapy={}
    mapy['A']=random.randint(0,1)
    mapy['B']=random.randint(0,1)
    mapy['C']=random.randint(0,1)
    mapy['D']=random.randint(0,1)
    question="What does the expression {0} evaluate to, When ".format(final_exp)
    for i in range(num_vars):
        if(i==0):
            question+="A={0} ".format(mapy['A'])
        elif(i==1):
            question+="B={0} ".format(mapy['B'])
        elif(i==2):
            question+="C={0} ".format(mapy['C'])
        elif(i==3):
            question+="D={0} ".format(mapy['D'])
    # question+="\n"

    new_stack=[]
    for i, val in enumerate(exp):
        if isinstance(val, str):
            new_stack.append(val)
        else:
            x=mapy[val.symbol]
            if val.sign=="-":
                x^=1
            new_stack.append(x)

    res=[]
    for val in new_stack:
        if val=="+" or val==".":
            v1=res.pop()
            v2=res.pop()
            if(val=="+"):
                res_var=v1|v2
            else:
                res_var=v1&v2
            res.append(res_var)
        else:
            res.append(val)

    answer=res[0]
    options=['0', '1']
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer


def simplify_exp_sop():
    table = gen_random_truth_table(3)
    question = "Minimize the given expression - {0}".format(print_sop(gen_sop(table)))
    minterms, num_vars = table_to_minterms(table)
    options=[]
    options.append(print_QM(manipulate_minterms(table), []))
    options.append(print_QM(manipulate_minterms(table), manipulate_dc(table)))
    options.append(print_QM(minterms, []))
    options.append(print_QM_distract(minterms, []))
    options.append(print_QM_distract(manipulate_minterms(table), manipulate_dc(table)))
    answer=print_QM(minterms, [])
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer


def simplify_exp_pos():
    table = gen_random_truth_table(3)
    question = "Minimize the given expression - {0}".format(print_pos(gen_pos(table)))
    minterms, num_vars = table_to_minterms(table)
    options=[]
    options.append(print_QM(manipulate_minterms(table), []))
    options.append(print_QM(manipulate_minterms(table), manipulate_dc(table)))
    options.append(print_QM(minterms, []))
    options.append(print_QM_distract(minterms, []))
    options.append(print_QM_distract(manipulate_minterms(table), manipulate_dc(table)))
    answer=print_QM(minterms, [])
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer


def simplify_exp_minterms():
    table = gen_random_truth_table(3)
    minterms, num_vars = table_to_minterms(table)
    question = "Minimize the given expression - Minterms: {0}".format(minterms)
    options=[]
    options.append(print_QM(manipulate_minterms(table), []))
    options.append(print_QM(manipulate_minterms(table), manipulate_dc(table)))
    options.append(print_QM(minterms, []))
    options.append(print_QM_distract(minterms, []))
    options.append(print_QM_distract(manipulate_minterms(table), manipulate_dc(table)))
    answer=print_QM(minterms, [])
    random.shuffle(options)
    idx = 'A'
    new_options = []
    for option in options:
        new_option = idx+". "+str(option)
        new_options.append(new_option)
        idx = chr(ord(idx) + 1)
    return question, new_options, answer


question_list={
    1: sop_to_minterm,
    2: pos_to_minterm,
    3: sop_to_pos,
    4: pos_to_sop,
    5: minterm_to_sop,
    6: minterm_to_pos,
    7: evaluate,
    8: simplify_exp_sop,
    9: simplify_exp_pos,
    10: simplify_exp_minterms,
}


def test():
    for i in range(1,11):
        q,o,a=question_list[i]()
        print(q)
        print(o)
        print(a)
# test()  
# Uncomment the test to check every question templates output

#final function needs to be combined with generator.py
def generate_question_boolean_algebra(level):
    q,o,a = question_list[random.randint(1,10)]()
    return q,o,a

if __name__ == "__main__":
    ans = generate_question_boolean_algebra(1)
    print(ans)