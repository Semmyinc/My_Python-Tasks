# 2. generate multiplication table using an input method.
evenlist = []
oddlist = []
user = int(input('Enter figure:'))
for i in range(1,13):
        u = user * i
        print(f'{i} X {user} = {u}')
# result = user * i
# for x in result:
        if u%2 == 0:
            evenlist.append(u)
        else:
            oddlist.append(u)
print(evenlist)
print(oddlist)


even = []
odd = []
figure = int(input('Enter Value:'))
# NB: this means user should be prompted for input just once while the for loop make use of it 12 times counting from 1 to 12
for i in range(1,13):
        table = figure * i
        print (f'{figure} x {i} = {table}')
#   note 1      # for j in table: - NB this wont run because its already arranged vertically. for works on horizontal arrangement
        if table%2 == 0:
            even.append(table)
        else:
            odd.append(table)
print(even)
print(odd)
