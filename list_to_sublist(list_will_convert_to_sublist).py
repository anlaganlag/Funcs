from itertools import zip_longest
def list_range(lst,gap):
    """
     Efficent way handle list to sublist(gap you decide it)

     Space unefficent way:[lst[i:i+gap] for i in lst[statr:end:gap]]
    
     zip() will abandon the last one if less than gap
     
     with zip_longest() the last one will plus Nones
     """
    tmp=[iter(lst)]*gap # create mutiple iterors
    return list(zip_longest(*tmp))
    

print(list_range(range(2,11),4))
[(2, 3, 4, 5), (6, 7, 8, 9), (10, None, None, None)]
git 
