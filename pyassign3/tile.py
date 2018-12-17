'''
tile.py:placing bricks.

__author__ = 'Liuxinyi'
__pkuid__  = '1800011815'
__email__  = '1800011815@pku.edu.cn'
'''


m=int(input('the width of your wall is:'))
n=int(input('the length of your wall is:'))
a=int(input('the width of your brick is:'))
b=int(input('the length of your brick is:'))



wall=[[0 for w in range(m) ] for e in range(n)]	#creat the wall you want to pave!

def find_start(wall):
	'''find a blank space to begin!'''
	for i in range(n):
		for j in range(m):
			if wall[i][j]==0:
				return [i,j] 		
	return [n,m]


def placing(wall,ans,final):
	'''place 
	'''
	i=find_start(wall)[0]
	j=find_start(wall)[1]

	if i==n and j==m :
		final.append(ans.copy())
		return final	#wall is full!

	else:
		if i+b<=n and j+a<=m and (wall[i+k][j+g]==0 for g in range(a) for k in range(b)): 			#heng
			for k in range(b):
				for g in range(a):
					wall[i+k][j+g]=1

			out=tuple([(i+s)*m+j+d for d in range(a) for s in range(b)])
			ans.append(out)
			placing(wall,ans,final)

			for k in range(b):
				for g in range(a):
					wall[i+k][j+g]=0
			ans.remove(out)
			

		if i+a<=n and j+b<=m and (wall[i+k][j+g]==0 for g in range(b) for k in range(a)):		#shu
			for k in range(a):
				for g in range(b):
					wall[i+k][j+g]=1

			out=tuple([(i+s)*m+j+d for d in range(b) for s in range(a)])
			ans.append(out)
			placing(wall,ans,final)

			for k in range(a):
				for g in range(b):
					wall[i+k][j+g]=0
			ans.remove(out)

		else:
			final=[[]]
		return final

def print_final(final_answer):
	if final_answer==[[]]:
		print([[]])
	else:
		out={}
		v=0
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

print_final(placing(wall,[],[]))
