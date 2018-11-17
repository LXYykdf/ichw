'''planets.py:仿真太阳系水金地火木土6大行星围绕太阳的运行轨迹。

__author__='刘馨怡'
__pkuid__ ='1800011815'
__email__ ='1800011815@pku.edu.cn'
'''

import turtle
import math


def orbit(planet,a,turtlesize,color):
	'''orbit函数能赋予行星位置信息及轨道颜色:行星名称、
	初始位置、行星大小、行星及轨迹颜色。
	'''
	planet.speed(0)
	planet.penup()					
	planet.setx(a)
	planet.turtlesize(turtlesize)
	planet.shape('circle')
	planet.color(color)
	planet.pencolor(color)
	planet.pendown()		


def run(planet,a,i,speedk):
	'''使行星在轨道上按一定的轨迹做单次短距离运动：行星名称、
	行星轨道半长轴长、行星公转速度、参数方程中的角度变量、速度控制量。
	'''
	p=(i/180*math.pi)
	b=(a*a-1600)**0.5
	x=a*math.cos(p*speedk)
	y=b*math.sin(p*speedk)
	planet.goto(x,y)

def main():
	'''main module
	'''



wn=turtle.Screen()
wn.screensize(700,600)
wn.bgcolor('black')


Sun=turtle.Turtle()
Mercury=turtle.Turtle()
Venus=turtle.Turtle()
Earth=turtle.Turtle()
Mars=turtle.Turtle()
Jupiter=turtle.Turtle()
Saturn=turtle.Turtle()



s=20		#确定太阳的位置及行星运行轨道参数
m=48
v=60
e=120
ma=170
j=210
sa=300


orbit(Sun,s,1.5,'gold')

orbit(Mercury,m,0.3,'turquoise')

orbit(Venus,v,0.6,'darkorange')

orbit(Earth,e,0.5,'darkcyan')

orbit(Mars,ma,0.3,'lightcoral')

orbit(Jupiter,j,1.2,'khaki')
						
orbit(Saturn,sa,1,'brown')


k=1							#使行星们轮流间歇性运动起来
while k<=720 :
	run(Mercury,m,k,5)
	run(Venus,v,k,4)
	run(Earth,e,k,3)
	run(Mars,ma,k,2)
	run(Jupiter,j,k,1)
	run(Saturn,sa,k,0.5)
	k=k+1

wn.exitonclick()



if __name__=='__main__'	:
	mian()
