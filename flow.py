
x = int(input("enter an integer:  "))
if x < 0:
    x = 0
    print('Negative number changed to zero.')
elif x == 0:
    print('zero')
elif x == 1:
    print('one')
else:
    print('Some other number')


# the 3rd number here is the one by which we increment
# (so the outcome would be 0 2 4)
for i in range(0, 5, 2):
    print(i)
