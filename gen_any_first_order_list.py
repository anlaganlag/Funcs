import itertools as it

def foo(ini,p,q,times):
    """ini is the start value
       p is the multy number
       q is the add number
       times is the how many ele you want
    """
    g=it.accumulate(it.repeat(ini),lambda x,_:x*p + q)
    return list(next(g) for _ in range (times))
