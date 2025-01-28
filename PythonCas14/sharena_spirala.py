from turtle import *
speed(0)
colors = ['red','green','yellow','blue','purple','skyblue']
for x in range(0,1000):
    pencolor(colors[x % len(colors)])
    x=x+10
    forward(x)
    left(100)
done()

# 0 % 4 = 0
# 1 % 4 = 1
# 2 % 4 = 2
# 3 % 4 = 3
# 4 % 4 = 0
# 5 % 4 = 1
# 6 % 4 = 2
# ...itn

