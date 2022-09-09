# import first
# from first import ball

# # print(first.name)

# print(ball())
# method 1
# from first import Myball

# x = Myball()
# x.ball()
# print(x.ball())

# # method 2
# from first import q

# # v = q()
# q.ball()
# print(q.ball())
from cmath import log
from first import Myball    
print(f'Welcome to Semmyinc Basic Maths Operations\nSelect from the range of options in the menu below by typing the figure\nagainst your preffered operation in the input box and press the Enter key.')
def oper_list():
    print('''
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication
    5. Floor Division
    6. Modulus
    7. Exponential
    8. Factorial
    9. Permutation
    10.Combination
    ''')
def if_list():

    option = input('Operation: ')

    if option == '1':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.add(number1, number2))

    elif option == '2':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.sub(number1, number2))

    elif option == '3':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.div(number1, number2))

    elif option == '4':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.mul(number1, number2))

    elif option == '5':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.flr(number1, number2))

    elif option == '6':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.mod(number1, number2))

    elif option == '7':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.exp(number1, number2))

    elif option == '8':
        number = int(input('Number: '))
        print(n.fac(number))

    elif option == '9':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.per(number1, number2))

    elif option == '10':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
        print(n.com(number1, number2))

    else:
        trial = 1
        while trial <=3:
            print(f'Invalid Selection\nChoice must be between 1 and 10 as seen in the list below.')
            oper_list()
            print(f'Do you wish to continue? Y/N')
            answer = input('Response: ')
            if answer.upper() == 'Y':
                oper_list()
                if_list()
                break
            elif answer.upper() == 'N':
                pass
                break
            else:
                trial+=1
                print('Invalid Selection')

            
n = Myball()
oper_list()
if_list()





    