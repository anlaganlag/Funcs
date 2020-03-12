import functools 
@functools.lru_cache(maxsize=128)
def fib(n):
	if n <2:
		return 1
	return fib(n-1) + fib(n-2)

#加上lru真的快幾萬倍
