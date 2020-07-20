my_sheep_sizes = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Hien and these are my ship sizes:')
print(my_sheep_sizes)
the_biggest_sheep = my_sheep_sizes[0]
for i in range(1, len(my_sheep_sizes)):
    if the_biggest_sheep < my_sheep_sizes[i]:
        the_biggest_sheep = my_sheep_sizes[i]
print(f"Now, my biggest sheep has size {the_biggest_sheep} let's shear it")
for i in range(len(my_sheep_sizes)):
    if my_sheep_sizes[i] == the_biggest_sheep:
        my_sheep_sizes[i] = 8
print('After shearing, here is my flock: ', end='\n')
print(my_sheep_sizes)
for i in range(len(my_sheep_sizes)):
    my_sheep_sizes[i] = my_sheep_sizes[i] + 50
print('One month has passed, now here is my flock: ', end='\n')
print(my_sheep_sizes)

