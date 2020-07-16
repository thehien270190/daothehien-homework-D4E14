from turtle import *
n = int(input('Enter the number of circle? '))
speed(-2)
pencolor('green')
for  i in range(n):
    circle(100)
    left(360/n)
mainloop()