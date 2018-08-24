from turtle import*
shape("square")
hideturtle()
colors = ['red','blue','brown','yellow','grey','white']
colors_size = len(colors)
for i in range(len(colors)):
    color(colors[i])
    begin_fill()
    for j in range(2):
        right(90)
        forward(100)
        right(90)
        forward(50)
    
    end_fill()
    forward(50)
mainloop()
