from turtle import *
color('red')
for i in range(4):
    if i == 0:
        left(150)
        forward(100)
    else:
        left(30)
        forward(100)
    for j in range(3):
        if j == 1:
            left(120)
            forward(100)
        else:
            left(60)
            forward(100)
mainloop()