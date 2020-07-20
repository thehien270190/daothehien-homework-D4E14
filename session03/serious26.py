my_sheep_sizes = [5, 7, 300, 90, 24, 50, 75]
for i in range(4):
    if i == 0:
        print('Hello, my name is Hien and these are my ship sizes:')
        print(my_sheep_sizes)
    else:
        print(f'MONTH {i} :')
        for j in range(len(my_sheep_sizes)):
            my_sheep_sizes[j] = my_sheep_sizes[j] + 50
        print('One month has passed, now here is my flock: ', end='\n')
        print(my_sheep_sizes)
    if i == 3:
        total_of_sizes = 0
        for j in my_sheep_sizes:
            total_of_sizes = total_of_sizes + j
        print('My flock has size in total: ', total_of_sizes)
        print(f'I would get {total_of_sizes} * 2$ = {total_of_sizes*2}$')
    else:
        the_biggest_sheep = my_sheep_sizes[0]
        for j in range(1, len(my_sheep_sizes)):
            if the_biggest_sheep < my_sheep_sizes[j]:
                the_biggest_sheep = my_sheep_sizes[j]
        print(f"Now, my biggest sheep has size {the_biggest_sheep} let's shear it")
        for j in range(len(my_sheep_sizes)):
            if my_sheep_sizes[j] == the_biggest_sheep:
                my_sheep_sizes[j] = 8
        print('After shearing, here is my flock: ', end='\n')
        print(my_sheep_sizes)
        print('\n')