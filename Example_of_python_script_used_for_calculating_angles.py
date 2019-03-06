#!/usr/bin/python
import math
def angle(t,y,u,i,o,p,j,k,l):
	a=math.sqrt(((t-i)**2)+((y-o)**2)+((u-p)**2))
	b=math.sqrt((t-j)**2+(y-k)**2+(u-l)**2)
	c=math.sqrt((i-j)**2+(o-k)**2+(p-l)**2)
	ang=(a*a+b*b-c*c)/(2*a*b)
	return (180.0*math.acos(ang))/math.pi

out=open("output.log","w")

angles=[0]*180

for a in xrange(201):
	numbers=[]
	gro= open('%s%s%s' % ('traj',a,'.gro') ,"r")
	gro.readline()
	numbers=int(gro.readline())
	g=gro.readlines()
	for i in xrange(numbers):
		nx=0
		ny=0
		nz=0
		cz=0
		cy=0
		cx=0
		x=0
		y=0
		z=0
		if g[i][12:15]=='N35':
			nx+=float(g[i-3][21:28])
			nx+=float(g[i-2][21:28])
			nx+=float(g[i-1][21:28])
			nx+=float(g[i+1][21:28])
			nx+=float(g[i][21:28])
			nx=nx/5
			ny+=float(g[i-3][29:36])
			ny+=float(g[i-2][29:36])
			ny+=float(g[i-1][29:36])
			ny+=float(g[i+1][29:36])
			ny+=float(g[i][29:36])
			ny=ny/5
			nz+=float(g[i-3][37:44])
			nz+=float(g[i-2][37:44])
			nz+=float(g[i-1][37:44])
			nz+=float(g[i+1][37:44])
			nz+=float(g[i][37:44])
			nz=nz/5
			cx+=float(g[i-34][21:28])
			cx+=float(g[i-33][21:28])
			cx+=float(g[i-32][21:28])
			cx+=float(g[i-31][21:28])
			cx+=float(g[i-30][21:28])
			cx+=float(g[i-29][21:28])
			cx=cx/6
			cy+=float(g[i-34][29:36])
			cy+=float(g[i-33][29:36])
			cy+=float(g[i-32][29:36])
			cy+=float(g[i-31][29:36])
			cy+=float(g[i-30][29:36])
			cy+=float(g[i-29][29:36])
			cy=cy/6
			cz+=float(g[i-34][37:44])
			cz+=float(g[i-33][37:44])
			cz+=float(g[i-32][37:44])
			cz+=float(g[i-31][37:44])
			cz+=float(g[i-30][37:44])
			cz+=float(g[i-29][37:44])
			cz=cz/6
			x+=float(g[i+40][21:28])
			y+=float(g[i+40][29:36])
			z+=float(g[i+40][37:44])
			an=angle(nx,ny,nz,x,y,z,cx,cy,cz)
			angles[int(an)]+=1

counter=0
for i in angles:
print >>out, counter, i
counter+=1

out.close()