# Simple_Interest = PRT/100
p = float(input('Enter Principal Value: '))
r = float(input('Enter Rate Value: '))
t = float(input('Enter Time Value: '))
def interest(p, r, t=2):
    s_i = (p * r * t)/100
    print(f'Simple Interest is {s_i}')

interest(1000, 2.5, t)
# print(s_i)

    
