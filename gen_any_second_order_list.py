import itertools as it
	
def s(p,q,r,ini,times):
    """Use second order formula
      S= S[n-1]*P+S[n-2]*Q+R to generate any second order
     sequences 
     for instance:P=1,Q=1,R=0 is Fib seqencces
                  S = S[n-1]+S[n-2]
      p for how many S[n-1]
      s for how many  S[n-2]
      r for how many to add on
      ini for first 2 values
     times for how many value you would like to obtain 
     """
    imt = it.accumulate(it.repeat(ini),lambda x , _ : (x[1] , x[1] * q + x[0] * p + r))
     #imt for imidated tuple
    lst= map(lambda x: x[0],imt)
    return [next(lst) for _ in range(times)]
print(s(1,1,0,(0,1),25))

