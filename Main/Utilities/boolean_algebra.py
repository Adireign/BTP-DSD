import random

class var:
    def __init__(self, symbol, sign='+'):
        self.symbol=symbol
        self.sign=sign
    
def gen_random_exp(num_vars): #generating in postfix
    limit=random.randint(1,5) # lim on terms
    vars=[]
    for i in range (num_vars):
        vars.append(var(chr(ord('A')+i), "+"))
        vars.append(var(chr(ord('A')+i), "-"))
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
                string="~"+string
            stack.append(string)
            
    print(stack[0])

def gen_random_truth_table(num_vars):   #num_vars uptill 26 only for now.. practically 5-6 variable are required to generate question
    table=[]
    for i in range(2**num_vars):
        temp=format(i, f'0{num_vars}b')
        list=[int(bit) for bit in temp]
        list.append(random.randint(0,1))
        table.append(list)
    return table

def gen_sop(table):
    num_vars=len(table[0])-1
    sop=[]
    for i in range (len(table)):
        if table[i][num_vars]==1:
            prod=[]
            for val in range(num_vars):
                if table[i][val]==1:
                    sym="+"
                else:
                    sym="-"
                prod.append(var(chr(ord('A')+val), sym))
            sop.append(prod)
    return sop

def print_sop(sop):
    for i, prod in enumerate(sop):
        print("(", end="")
        for j, vars in enumerate(prod):
            if vars.sign=="-":
                print("~", end="")
            print("{0}".format(vars.symbol), end="")
            if j!=len(prod)-1:
                print(".", end="")
        print(")", end="")
        if i!= len(sop)-1:
            print("+", end="")


        