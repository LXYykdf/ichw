'''
tile.py:placing bricks.

__author__ = 'Liuxinyi'
__pkuid__  = '1800011815'
__email__  = '1800011815@pku.edu.cn'
'''
import turtle
def main():
	'''main function'''
	m=int(input('the width of your wall is:'))
	n=int(input('the length of your wall is:'))
	a=int(input('the width of your brick is:'))
	b=int(input('the length of your brick is:'))


	wall=[[0 for w in range(m) ] for e in range(n)]	#creat the wall you want to pave!
	print_final(placing(wall,[],[],m,n,a,b))
	if placing(wall,[],[],m,n,a,b)==[[]]:
		pass
	else:
		draw_placing(placing(wall,[],[],m,n,a,b),m,n,a,b)


def find_start(wall,m,n,a,b):
	'''find a blank space to begin!'''
	for i in range(n):
		for j in range(m):
			if wall[i][j]==0:
				return [i,j] 		
	return [n,m]


def placing(wall,ans,final,m,n,a,b):
	'''find solutions '''
	i=find_start(wall,m,n,a,b)[0]
	j=find_start(wall,m,n,a,b)[1]

	if i==n and j==m :
		anscopy=ans.copy()
		if len(anscopy)==(m*n)/(a*b):
			final.append(anscopy)

		return final	#wall is full!

	else:
		if i+b<=n and j+a<=m and (wall[i+k][j+g]==0 for g in range(a) for k in range(b)): 	
			for k in range(b):
				for g in range(a):
					wall[i+k][j+g]=1

			out=tuple([(i+s)*m+j+d for d in range(a) for s in range(b)])
			ans.append(out)
			placing(wall,ans,final,m,n,a,b)

			for k in range(b):
				for g in range(a):
					wall[i+k][j+g]=0
			ans.remove(out)
			

		if i+a<=n and j+b<=m and (wall[i+k][j+g]==0 for g in range(b) for k in range(a)):
			for k in range(a):
				for g in range(b):
					wall[i+k][j+g]=1

			out=tuple([(i+s)*m+j+d for d in range(b) for s in range(a)])
			ans.append(out)
			placing(wall,ans,final,m,n,a,b)

			for k in range(a):
				for g in range(b):
					wall[i+k][j+g]=0
			ans.remove(out)

		else:
			final=[[]]
		return final


def count(final_answer):
	'''coun the amount of solutions'''
	v=0
	if final_answer==[[]]:
		pass
	else:
		out={}
		while v <len(final_answer):
			if str(final_answer) in out:
				pass
			else:
				out[v]=str(final_answer[v])
				v+=1
	return v


def print_final(final_answer):
	'''print all the solutions'''
	v=0
	if final_answer==[[]]:
		print([[]])
	else:
		out={}
		while v <len(final_answer):
			if str(final_answer) in out:
				pass
			else:
				out[v]=str(final_answer[v])
				v+=1
		if v==1:
			print('We found one solution.')
		else:
			print('We found '+str(v)+' solutions.')
		for o in range(v):
			print(out[o])
	




def draw_placing(final_answer,m,n,a,b):
	'''draw the choosen solution'''

	wn=turtle.Screen()
	wn.screensize(500,500)
	t=turtle.Turtle()


	t.pencolor('blue')
	for h in range(n+1):
		t.penup()
		t.goto((-m/2)*30,(-n/2+h)*30)
		t.setheading(0)
		t.pendown()
		t.fd(m*30)

	for f in range(m+1):
		t.penup()
		t.goto((-m/2+f)*30,(-n/2)*30)
		t.setheading(90)
		t.pendown()
		t.fd(n*30)


	for w in range(n):
		for q in range(m):
			t.penup()
			t.goto(15*(1+2*q-m)-3,15*(1+2*w-n)-3)
			t.write(str(w*m+q), font=('Arial', 10, 'normal'))
		
	
	t.pencolor('black')
	x=int(turtle.numinput('Draw','choose a solution to draw between 1 and '\
		+str(count(final_answer)),1,minval=1,maxval=count(final_answer)))
	t.speed(0)
	t.pensize(3)
	choice=final_answer[x-1]

	
	for brick in choice:
		poss=[]
		count_x=0
		for pos in brick:
			x=pos%m
			y=pos//m
			poss.append((x,y))

		for poses in poss:
			if poss[0][1]==poses[1]:
				count_x+=1

		count_y=int(a*b/count_x)
		

		pos_start=brick[0]
		x_start=pos_start%m-m/2
		y_start=pos_start//m-n/2
		t.penup()
		t.goto(x_start*30,y_start*30)
		t.setheading(0)
		t.pendown()
		t.fd(count_x*30)
		t.left(90)
		t.fd(count_y*30)
		t.left(90)
		t.fd(count_x*30)
		t.left(90)
		t.fd(count_y*30)
	
	wn.exitonclick()


if __name__=='__main__':
	main()



