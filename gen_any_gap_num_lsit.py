import itertools as it
def gen_any_gap_num_list(times,step=1,start=0,):
    """generate  any  times and steps seq you decide
          times -> how many num you actually want!
          step  -> gaps,default by 1
          start -> start number,default by 0
    """
    gap_num = it.count(step=step,start=start)
    return list(next(gap_num) for _ in range(times))
 print(gen_any_gap_num(20,3,200))   
# start by 200  step =3 and 20 items list you generator
"""
[200,
 203,
 206,
 209,
 212,
 215,
 218,
 221,
 224,
 227,
 230,
 233,
 236,
 239,
 242,
 245,
 248,
 251,
 254,
 257]
"""
