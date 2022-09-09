

try:
    # num1 = float(input('Enter First Value: '))
    oper = input('Operation: ')
    # num2 = float(input('Enter Second Value: '))

    def operation():
        
        
        if oper  == '+':
            num1 = float(input('Enter First Value: '))
            num2 = float(input('Enter Second Value: '))
            result = (num1 + num2)
            print(result)
        elif oper == '-':
            num1 = float(input('Enter First Value: '))
            num2 = float(input('Enter Second Value: '))
            print(num1 - num2)
        elif oper == '*':
            num1 = float(input('Enter First Value: '))
            num2 = float(input('Enter Second Value: '))
            print(num1 * num2)
        elif oper == '/':
            num1 = float(input('Enter First Value: '))
            num2 = float(input('Enter Second Value: '))
            print(num1 / num2)
        elif oper == '//':
            num1 = float(input('Enter First Value: '))
            num2 = float(input('Enter Second Value: '))
            print(num1 // num2)
        elif oper == '**':
            num1 = float(input('Enter First Value: '))
            num2 = float(input('Enter Second Value: '))
            print(num1 ** num2)
        elif oper == '%':
            num1 = float(input('Enter First Value: '))
            num2 = float(input('Enter Second Value: '))
            print(num1 % num2)
        elif oper == '!':
            n = int(input('Enter Value: '))
            if n < 0:
                print('Operation not allowed for negative integers')
            elif n == 0:
                print('Factorial of 0 is 1')
            else:
                f = 1
                for x in range(1, n+1):
                    f *= x 
                print(f)
        elif oper == 'p':
            n = int(input('Enter Value of n: '))
            r = int(input('Enter Value of r: '))
            if n < r:
                print('n must be greater than r')
            elif n < 0:
                print('Operation not allowed for negative integers')
            elif n == 0:
                print('Factorial of 0 is 1')
            else:
                f = 1
                for numm in range(1, n+1):
                    f *= numm
                    k = 1
                    for nummm in range(1, n-r+1):
                        k *= nummm
                p = f / k
                print(p)
        elif oper == 'c':
            n = int(input('Enter Value of n: '))
            r = int(input('Enter Value of r: '))
            if n < r:
                print('n must be greater than r')
            elif n < 0:
                print('Operation not allowed for negative integers')
            elif n == 0:
                print('Factorial of 0 is 1')
            else:
                f = 1
                for numm in range(1, n+1):
                    f *= numm
                    k = 1
                    for nummm in range(1, n-r+1):
                        k *= nummm
                        d = 1
                        for nummmm in range(1, r+1):
                            d *= nummmm
                c = f /(k * d)
                print(c)
        else:
            print('Invalid Operation')
    operation()        
except ValueError:
    print('Value can only be float')
except ZeroDivisionError:
    print('num2 can not be zero')

     


