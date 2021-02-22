#importing the pen 
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors=["red","orange","yellow","light green","green","light blue","blue","indigo","purple","pink"]

classmates=[]
#turtle asking what to write
name = turtle.textinput("Classmates",
                        "Enter a name or hit ENTER to end")
while name !="":
    classmates.append(name)
    name = turtle.textinput("Classmates",
                        "Enter a name or hit ENTER to end")

#Drawing spiral based on name
for x in range (100):
    t.pencolor(colors[x%len(classmates)]) #Rotate through colors
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(classmates[x%len(classmates)],font=("Arial",int((x+4)/4),"bold"))
    t.left(360/len(classmates)+2)
    
            

