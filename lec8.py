"""
functions
"""

def my_function(a,b=0):
    
    result=a+b
    print('a is', a)
    print('b is', b)
    #return result
    
#print(my_function(1))

def calculate_abs(a):
    if type(a) is str:
        return ('wrong data type')
    elif a>0:
        return a
    else:
        return -a 
        
#print(calculate_abs('b'))
        
def calculate_sigma(m,n):
    
    result= 0
    
    for i in range(n,m+1):
        result=result+i
    return result
    
#print(calculate_sigma(5,3))

def calculate_pi(m,n):
    
    result= 1
    
    for i in range(n,m+1):
        result=result*i
    return result
    
#print(calculate_pi(5,3))

def calculate_f(m):
    
    if m==0:
        return 1
    else:
        return m*calculate_f(m-1)
        
print(calculate_f(5))

def calculate_p(m,n):
    return calculate_f(m)/calculate_f(m-n)
    
print(calculate_p(6,4))