"""
lab 9 class lab
"""

#3.1

class my_stat():
    
    def calculate_sigma(self,m,n):
    
        result= 0
    
        for i in range(n,m+1):
            result=result+i
        return result
    def calculate_pi(self,m,n):
    
        result= 1
    
        for i in range(n,m+1):
            result=result*i
        return result
    def calculate_f(self,m):
    
        if m==0:
            return 1
        else:
            return m*self.calculate_f(m-1)
            
    def calculate_p(self,m,n):
        
        return self.calculate_f(m)/self.calculate_f(m-n)
        
#3.2
my_cal=my_stat()

print(my_cal.calculate_sigma(5,3))

print(my_cal.calculate_p(5,3))

print(my_cal.calculate_f(5))

print(my_cal.calculate_p(5,2))