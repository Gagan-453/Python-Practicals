Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import *
>>> pos()
(0.00,0.00)
>>> setx(100)
>>> sety(10)
>>> penup()
>>> setx(200)
>>> sety(0)
>>> pendown()
>>> sety(0)
>>> setheading(100)
>>> a = Screen()
>>> a.bg('green')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.bg('green')
AttributeError: '_Screen' object has no attribute 'bg'
>>> a.background('green')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.background('green')
AttributeError: '_Screen' object has no attribute 'background'
>>> clear()
>>> pos()
(200.00,0.00)
>>> penup()
>>> setpos(0, 0)
>>> setheading(0)
>>> heading()
0.0
>>> setheading(10)
>>> heading()
10.0
>>> seth(100)
>>> seth(0)
>>> seth(0)
>>> seth(180)
>>> setpos(100, 100)
>>> pendown()
>>> home()
>>> clear()
>>> circle(120, 180)
>>> circle(120, 180)
>>> clear()
>>> circle(120, 360)
>>> clear()
>>> circle(200, 360)
>>> clear()
>>> circle(10, 360)
>>> clear()
>>> circle(120, 360, 10)
>>> clear()
>>> circle(120, 360, 1)
>>> clear()
>>> circle(120, 360, 2)
>>> clear()
>>> circle(120, 360, 4)
>>> dot(100, "blue")
>>> clear()
>>> dot(10, "blue")
>>> fd(100)
>>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
NameError: name 'turtle' is not defined
>>> 
>>> clear()
>>> fd(50); dot(20, "blue"); fd(50)
>>> clear()
>>> color("green")
>>> stamp()
24
>>> fd(50)
>>> setpos(0, 100)
>>> clear()
>>> fd(50)
>>> stamp()
26
>>> fd(50)
>>> clearstamp(0)
>>> clear()
>>> a = stamp()
>>> fd(50)
>>> clearstamp(a)
>>> clear()
>>> setpos(-20, 0)
>>> setpos(-50, 0)
>>> setpos(-200, 0)
>>> clear()
>>> for i in range(5):
	stamp()
	fd(10)

	
31
32
33
34
35
>>> clearstamps()
>>> clearstamp()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    clearstamp()
TypeError: clearstamp() missing 1 required positional argument: 'stampid'
>>> clearstamps()
>>> for i in range(5):
	stamp()
	fd(10)

	
36
37
38
39
40
>>> clearstamps(2)
>>> clearstamps(-2)
>>> clearstamps()
>>> speed()
3
>>> speed('normal')
>>> speed()
6
>>> speed('high')
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    speed('high')
  File "<string>", line 8, in speed
  File "C:\Users\ADINARAYANAREDDY\AppData\Local\Programs\Python\Python38-32\lib\turtle.py", line 2170, in speed
    elif 0.5 < speed < 10.5:
TypeError: '<' not supported between instances of 'float' and 'str'
>>> clear()
>>> pos()
(-100.00,-0.00)
>>> position()
(-100.00,-0.00)

>>> goto(0, 0)
>>> pos
<function pos at 0x03222388>
>>> pos()
(0.00,0.00)
>>> clear()
>>> towards(10, 0)
0.0
>>> goto(10, 10)
>>> towards(10, 10)
0.0
>>> towards(100, 100)
45.0
>>> goto(100, 100)
>>> undo()
>>> redo()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    redo()
NameError: name 'redo' is not defined
>>> undo()
>>> goto(10, 10)
>>> goto(100, 100)
>>> xcor()
100
>>> ycor()
100
>>> clear()
>>> xcor()
100
>>> ycor()
100
>>> setpos(0, 0)
>>> clear()
>>> xcor()
0
>>> ycor()
0
>>> sety(40)
>>> ycor()'
SyntaxError: EOL while scanning string literal
>>> ycor()
40
>>> xcor(0)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    xcor(0)
TypeError: xcor() takes 0 positional arguments but 1 was given
>>> xcor()
0
>>> 