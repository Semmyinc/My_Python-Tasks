# Even = []
# Odd = []
# Prime = []
# for m in range(100):
#     # if (n > 1):
#         if (m % 2 == 0):
#             Even.append(m)
#         elif (m % 2 == 1):
#             Odd.append(m)
#     # elif (m % 1 != 0) or (m % m ==0):not part
#     #       Prime.append(m) not part
# for x in range(100):
#     if (x > 1):
#         for n in range(2,x):
#             if x % n == 0:
#                 break 
#         else:
#             Prime.append(x)    
# print('Evenlist:', Even )
# print('Oddlist:', Odd)
# print('Primelist:', Prime)


# Number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# Even = []
# Odd = []
# Prime = []
# for m in Number:
#         if (m % 2 == 0):
#             Even.append(m)
#         elif (m % 2 == 1):
#             Odd.append(m)
# for x in Number:
#     if (x > 1):
#         for n in range(2,x):
#             if x % n == 0:
#                 break 
#         else:
#             Prime.append(x)    
# print('Evenlist:', Even )
# print('Oddlist:', Odd)
# print('Primelist:', Prime)

try:
    even = []
    odd = []
    prime = []
    number_min = int(input('Enter Starting Value:'))
    number_max = int(input('Enter Ending Value:'))
    for x in range (number_min,number_max):
            if x%2 == 0:
            # then perfom
                even.append(x)
            elif x%2 == 1:
                odd.append(x)
    for y in range (number_min,number_max):
        if y>1:
            for z in range (2, y):
                if y%z == 0:
                    break
            else:
                prime.append(y)
    print(f'Even List = {even}')
    print(f'Odd List = {odd}')
    print(f'Prime List = {prime}')
except(ValueError):
    print(f'Error! Value can only be integer.')