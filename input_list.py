
# Generate list with inputs where last item multiplies the others.m
productlist1 = []
productlist2 = []
for x in range(10):
    number = int(input('Enter Value:')) 
    productlist1.append(number)
# print(productlist1)
for y in productlist1:
    z = productlist1[-1] * y
    productlist2.append(z)
print(productlist1)
print(productlist2)

sola = []
femi = []
for i in range (10):
   tola = int(input('Enter Value:')) 
   sola.append(tola)
print(sola)
for j in sola:
    leah = sola[5] * j
    femi.append(leah)
print(femi)


sola = []
femi = []
for i in range (10):
   tola = int(input('Enter Value:')) 
    # NB: this means the user should be prompted 10 times for input
   sola.append(tola)
print(sola)
for j in sola:
    leah = 2 * j
    femi.append(leah)
print(femi)
# note 2: there seems to be diff between when input and for comes before and after each other in command sequencing as noticedin the examples above.