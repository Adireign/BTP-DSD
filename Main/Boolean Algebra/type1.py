from boolean_algebra import *
from QM_method import *
from distractors import *

print("Minimize the given expression")
table = gen_random_truth_table(3)
print_sop(gen_sop(table))
print("\n")
minterms, num_vars = table_to_minterms(table)

print("a> {0}".format(print_QM_distract(minterms, [])))
print("b> {0}".format(print_QM(manipulate_minterms(table), [])))
print("c> {0}".format(print_QM(manipulate_minterms(table), manipulate_dc(table)))) 
print("d> {0}".format(print_QM_distract(manipulate_minterms(table), manipulate_dc(table)))) 
print("e> {0}".format(print_QM(minterms, []))) 


Ans = print_QM(minterms, [])


# laws and identities
# find more distractors