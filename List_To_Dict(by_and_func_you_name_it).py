from collections import defaultdict
from itertools import groupby
lst=[(True, [64, 169]), (False, [73]), (True, [225]), (False, [117])]
def groupby_list_to_dict(lst,func):
    handle_by_groupby=[(k,list(v)) for k,v in groupby(lst,func)]
    dic={}
    [dic.setdefault(k,[]).extend(v) for k,v in handle_by_groupby]
    return dic



l1=[64, 169,73,225,117,345,779]
print(groupby_list_to_dict(l1,lambda x: x%5))
#{4: [64, 169, 779], 3: [73], 0: [225, 345], 2: [117]}

print(groupby_list_to_dict(l1,lambda x: x<=200))
#{True: [64, 169, 73, 117], False: [225, 345, 779]}

print(groupby_list_to_dict(l1,lambda x: (x**0.5)%1==0))
#{True: [64, 169, 225], False: [73, 117, 345, 779]}

print(groupby_list_to_dict(l1,lambda x: len(str(x))))

#{2: [64, 73], 3: [169, 225, 117, 345, 779]}

