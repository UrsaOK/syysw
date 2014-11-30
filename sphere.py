
#TOIMII

def isInTriangle(x,y,x1,y1,x2,y2,x3,y3):
	
	
	sqx1 = x1*x1
	sqx2 = x2*x2
	sqx3 = x3*x3
	
	sqy1 = y1*y1
	sqy2 = y2*y2
	sqy3 = y3*y3
	
	return sqx1+sqy1 > x*x+y*y





#TOIMII
def d3determinant(a,b,c,d,e,f,g,h,i):
	"""
	[[a,b,c]
	 [d,e,f]
	 [g,h,i]]
	"""
	
	return a*d2determinant(e,f,h,i) - b*d2determinant(d,f,g,i) + c*d2determinant(d,e,g,h)


#TOIMII
def d2determinant(a,b,c,d):
	"""
	[[a,b]
	 [c,d]]
	
	"""
	
	return (a*d)-(b*c)

#TOIMII
def solve2x2(x0,y0,x1,y1,x2,y2):
	
	"""
	[[x1,x2]     [a,   [x0,
	 [y1,y2]] *   b] =  y0]
	"""

	det = d2determinant(x1,x2,y1,y2)
	
	try:
		a = d2determinant(x0,x2,y0,y2)/det
	except ZeroDivisionError:
		a = None
	try:
		b = d2determinant(x1,x0,y1,y0)/det
	except ZeroDivisionError:
		b = None
		
	return (a,b)


#TOIMII
def solve3x3(x0,y0,z0,x1,y1,z1,x2,y2,z2,x3,y3,z3):
	
	"""
	[[x1,x2,x3]     [a,    [x0
	 [y1,y2,y3]  *   b,  =  y0
	 [z1,z2,z3]]     c]     z0]	Solve by Cramer's rule.
	
	"""
	
	
	det = d3determinant(x1,x2,x3,y1,y2,y3,z1,z2,z3)
	
	try:
		a = d3determinant(x0,x2,x3,y0,y2,y3,z0,z2,z3)/det
	except ZeroDivisionError:
		a = None
	try:
		b = d3determinant(x1,x0,x3,y1,y0,y3,z1,z0,z3)/det
	except ZeroDivisionError:
		b = None
	try:
		c = d3determinant(x1,x2,x0,y1,y2,y0,z1,z2,z0)/det
	except ZeroDivisionError:
		c = None
	
	return (a,b,c)





#TESTAA
def ray_hits_triangle(screenpoint,triangle):
	
	"""
	screenpoint = (x,y,z)
	
	triangle = ((x,y,z),(x,y,z),(x,y,z))
	
	"""
	
	#vector defining line:
	t = screenpoint

	#vectors defining plane: 
	u = (triangle[1][0]-triangle[0][0],triangle[1][1]-triangle[0][1],triangle[1][2]-triangle[0][2])
	v = (triangle[2][0]-triangle[0][0],triangle[2][1]-triangle[0][1],triangle[2][2]-triangle[0][2])

	
	#plane's origo:
	o = (triangle[0][0],triangle[0][1],triangle[0][2])

	"""
	solve plane = line
	
	at = o + bu + cv

	<=> -at + bu + cv = -o

	        [[-xt,xu,xv]	  [a,     [-xo,
	<=>      [-yt,yu,yv]	*  b,   =  -yo,
	         [-zt,zu,zv]]      c]      -zo,]
	"""

	#intersection point vector
	p = solve3x3(-o[0],-o[1],-o[2],-t[0],-t[1],-t[2],u[0],u[1],u[2],v[0],v[1],v[2])
	
	"""
	solve intersection point vector = nu + mv

	<=> p = nu + mv
	<=> [[ux,vx], * [n,  =  [px,
	     [uy,vy]]    m]      py]
	"""
	
	planecoords = solve2x2(p[0],p[1],u[0],u[1],v[0],v[1])


	return isInTriangle(planecoords[0],planecoords[1],0,0,1,0,0,1)


