import turtle
import random


screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')


t = turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("backround color",font=('arial',30,'normal'), align="center")


# num1= int(input('enter a number:'))
# num2= int(input('enter a another number:'))

#
# num1 = random.randint(-100,100)
# num2 = random.randint(-100,100)

# sum = num1+num2
t.penup()
t.goto(-75, 100)
t.pendown()
t.pencolor('tan')
t.write("1. tan", font=('arial', 20, 'normal'), align="left")
t.penup()
t.goto(-75, 50)
t.pendown()
t.pencolor('azure')
t.write("2. Azure", font=('arial', 20, 'normal'), align="left")
t.penup()
t.goto(-75, 0)
t.pendown()
t.pencolor('aquamarine')
t.write("3. aquamarine", font=('arial', 20, 'normal'), align="left")
t.penup()
t.goto(-75, -50)
t.pendown()
t.pencolor('darkkhaki')
t.write("4. darkkhaki", font=('arial', 20, 'normal'), align="left")

t.penup()
t.goto(0, -150)
t.pendown()
t.pencolor('white')
t.write("choose a color ", font=('arial', 30, 'normal'), align="center")


choose=int(input('choose a color:'))

if choose ==1:
   screen.bgcolor("tan")
elif choose==2:
   screen.bgcolor('azure')
elif choose ==3:
   screen.bgcolor('aquamarine')
else:
   screen.bgcolor('darkkhaki')
t.clear()

t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor('black')
t.write("enter your name:", font=('arial', 30, 'normal'),align= "center")

name= input('enter your name:')
t.clear()
operation= random.randint(1,4)
if operation ==1:
   symbol = "+"
   #add
   num1 = random.randint(-100, 100)
   num2 = random.randint(-100, 100)
   solution = num1 + num2
elif operation ==2:
   symbol="-"
   #add
   num1 = random.randint(-100, 100)
   num2 = random.randint(-100, 100)
   solution = num1 - num2

elif operation ==3:
   symbol="x"
   #multiply
   num1 = random.randint(-10, 10)
   num2 = random.randint(-10, 10)

   solution= num1 * num2

elif operation ==4:
   symbol="/"
   #divide
   num1 = random.randint(-10, 10)
   num2 = random.randint(1, 10)
   sign = random.randint(1,2)
   if sign==2:
       num2= -1+num2


   solution= num1 / num2
t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('blue')
t.write(name,font=('arial',30,'normal'), align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('blue')
t.write(num1,font=('arial',30,'normal'), align="center")


t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('red')
t.write(symbol,font=('arial',30,'normal'), align="center")


t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('blue')
t.write(num2,font=('arial',30,'normal'), align="center")


t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('green')
t.write("=",font=('arial',30,'normal'), align="center")


ans= float(input('Please enter the answer: '))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('red')
t.write(solution,font=('arial',30,'normal'), align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('red')
t.write('your answer is:'+str(ans),font=("arial",30,"normal"), align="center")

if ans==solution:
   screen.bgcolor('dodgerblue')
   t.penup()
   t.goto(0,50)
   t.pendown()
   t.pencolor('black')
   t.write('correct'+str(ans),font=("arial",30,"normal"), align="center")


else:
   screen.bgcolor('dark orange')
   t.penup()
   t.goto(0,50)
   t.pendown()
   t.pencolor('black')
   t.write('incorrect'+str(ans),font=("arial",30,"normal"), align="center")

turtle.done()