# import math

# print(dir(math))
# print(help(math))
# import os

# print(dir(os))
# print(help(os))

# name = 'paul'
# method 1
# - To call the class Myball in second.py to make use of any of its functions;
# - Dont make an object on it here. just leave it the way it is.
# - In second .py, make an object of it, say x = Myball().
# then, do the object.the function to be called like x.ball().
# finally, print(x.ball()).

# method2
# 1. make an object of it here first. say q = Myball()
try:
 class Myball:
        def __init__(self):
            self.name = 'paul'
        
        # def ball(self):
        #     # '''return add of x and y'''
        #     return 7

    # q = Myball()
        def add(self, x, y):
            '''return add of x and y'''
            return x + y

        def sub(self, x, y):
            '''return sub of x and y'''
            return x - y

        def div(self, x, y):
            '''return div of x and y'''
            return x / y

        def mul(self, x, y):
            '''return mul of x and y'''
            return x * y

        def flr(self, x, y):
            '''return flr of x and y'''
            return x // y

        def mod(self, x, y):
            '''return mod of x and y'''
            return x % y

        def exp(self, x, y):
            '''return exp of x and y'''
            return x ** y

        def fac(self, x):
            '''return fac of x'''
            if x < 0:
                return f'Operation not valid for negative integers'
            elif x == 0:
                return 1
            else: 
                fac = 1
                for number in range (1, x+1):
                    fac *= number
            return fac

        def per(self, x, y):
            '''return per of x and y'''
            if x < y:
                return f'{x} must be greater than {y} '
            elif x < 0 and y < 0:
                return f'Operation not valid for negative integers'
            elif x == 0:
                return 1
            else: 
                fac = 1
                for number in range (1, x+1):
                    fac *= number
                    fac1 = 1
                    for other_number in range(1, (x-y)+1):
                        fac1 *= other_number
                per = fac / fac1
            return per
      
        def com(self, x, y):
            '''return com of x and y'''
            if x < y:
                return f'{x} must be greater than {y}'
            elif x < 0 and y < 0:
                return f'Operation not valid for negative integers'
            elif x == 0:
                return 1
            else: 
                fac = 1
                for number in range (1, x+1):
                    fac *= number
                    fac1 = 1
                    for other_number in range(1, (x-y)+1):
                        fac1 *= other_number
                        fac2 = 1
                        for another_number in range(1, y+1):
                            fac2 *= another_number
                com = fac / (fac1 * fac2)     
            return com       
except(ValueError):
    print(f'Takes only integer values')
            
                   
   

    

