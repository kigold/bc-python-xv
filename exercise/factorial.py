def factorial_reduce(n):
    if n == 0:
        return 1
    return reduce(lambda x,y: x*y, range(1,n+1))
def factorial_recur(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return n * factorial_recur(n-1)
        
    
        
    
