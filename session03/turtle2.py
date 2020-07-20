from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    fillcolor(colors[i])
    begin_fill()
    for j in range(4):
        if j%2 == 0:
            forward(50)
        else:
            forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()
