
#TOIMII

def isInTriangle(x,y,x1,y1,x2,y2,x3,y3):
	
	
	det = (y2-y3)*(x1-x3)+(x3-x2)*(y1-y3)
	detPositive = det > 0
	
	l1nodet = (y2-y3)*(x-x3)+(x3-x2)*(y-y3)
	l2nodet = (y3-y1)*(x-x3)+(x1-x3)*(y-y3)
	l3nodet = det - l1nodet - l2nodet
	
	
	l1Pos = l1nodet >= 0
	l2Pos = l2nodet >= 0
	l3Pos = l3nodet >= 0
	
	
	return (l1Pos == l2Pos == l3Pos == detPositive)


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
	
	a = d2determinant(x0,x2,y0,y2)/det
	b = d2determinant(x1,x0,y1,y0)/det
		
	return (a,b)


#TOIMII
def solve3x3(x0,y0,z0,x1,y1,z1,x2,y2,z2,x3,y3,z3):
	
	"""
	[[x1,x2,x3]     [a,    [x0
	 [y1,y2,y3]  *   b,  =  y0
	 [z1,z2,z3]]     c]     z0]	Solve by Cramer's rule.
	
	"""
	
	
	det = d3determinant(x1,x2,x3,y1,y2,y3,z1,z2,z3)
	
	a = d3determinant(x0,x2,x3,y0,y2,y3,z0,z2,z3)/det
	b = d3determinant(x1,x0,x3,y1,y0,y3,z1,z0,z3)/det
	c = d3determinant(x1,x2,x0,y1,y2,y0,z1,z2,z0)/det
	
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
	input(-o,au,bv,-ct)
	
	solve plane = line
	
	ct = o + au + bv

	<=> au + bv + -ct = -o

	        [[-xu,xv,xt]	  [a,     [-xo,
	<=>      [-yu,yv,yt]	*  b,   =  -yo,
	         [-zu,zv,zt]]      c]      -zo,]
			
	return (a,b,c)
	"""
	
	#intersection point vector
	p = solve3x3(-o[0],-o[1],-o[2],u[0],u[1],u[2],v[0],v[1],v[2],-t[0],-t[1],-t[2])
	
	"""
	solve intersection point vector = nu + mv

	<=> p = nu + mv
	<=> [[ux,vx], * [n,  =  [px,
	     [uy,vy]]    m]      py]
	"""
	
	planecoords = solve2x2(p[0],p[1],u[0],u[1],v[0],v[1])
	

	return isInTriangle(planecoords[0],planecoords[1],0,0,1,0,0,1)


