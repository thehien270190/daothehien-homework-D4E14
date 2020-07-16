#2.a.i
for i in range(20):
    if i%2 == 0:
        print('1', end=' ')
    else:
        print('0', end=' ')

#2.a.ii
print('\n')
n = int(input("Enter the total number of 1's and 0's: "))
for i in range(n):
    if i%2 == 0:
        print('1', end='  ')
    else:
        print('0', end='  ')

#2.b.i
print(end='\n')
for i in range(9):
    print(end='\n')
    for j in range(9):
        a = (i+1)*(j+1)
        if a < 10:
            print(a, end='  ')
        else:
            print(a, end=' ')

#2.b.ii
print('\n')
n = int(input('Enter a number: ',))
for i in range(n):
    if i > 0:
        print(end='\n')
    for j in range(n):
        a = (i+1)*(j+1)
        if a < 10:
            print(a, end='  ')
        else:
            print(a, end=' ')

#2.c.i
print(end='\n')
for i in range(9):
    print(end='\n')
    if i%2 == 0:
        for j in range(9):
            if j%2 == 0:
                print('1', end='  ')
            else:
                print('0', end='  ')
    else:
        for j in range(9):
            if j%2 == 0:
                print('0', end='  ')
            else:
                print('1', end='  ')

# 2.c.ii
print('\n')
n = int(input('Enter a number: '))
for i in range(n):
    if i > 0:
        print(end='\n')
    if i%2 == 0:
        for j in range(n):
            if j%2 == 0:
                print('1', end='  ')
            else:
                print('0', end='  ')
    else:
        for j in range(n):
            if j%2 == 0:
                print('0', end='  ')
            else:
                print('1', end='  ')