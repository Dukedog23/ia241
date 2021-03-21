"""
lec9 class
"""

class car:
    
    maker= 'toyota' #shared by all instances
    
    def __init__(self, input_model):
        self.model=input_model  #unique to each instance
        
    def report(self):
        return self.model, self.maker
        
my_corolla=car('corolla')

#my_highlander=car('highlander')

#print(my_corolla.model)

my_corolla.maker='ford'
#print(my_corolla.maker)

#print(my_corolla.maker)
#print(my_highlander.maker)

#print(my_corolla.model)
#print(my_highlander.model)

#import lec8

#print(lec8.calculate_f(5))