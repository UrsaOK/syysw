#import sfml
import sphere
import numpy

WIDTH = 16
HEIGHT = 16

SIZE = 4.7

#screen = sfml.VertexArray(sfml.PrimitiveType.POINTS, WIDTH*HEIGHT)

screen = [[0 for x in range(HEIGHT)] for y in range(WIDTH)]


TRIANGLE = ((10,11,120),(11,10,120),(11,11,120))


for i in range(WIDTH*HEIGHT):
	color = 0
	scrx = i%WIDTH
	scry = int((i-scrx)/WIDTH)
	
	
	point = (-(scrx-(WIDTH>>1)),-(scry-(HEIGHT>>1)),-120)
	
	#print(point)
	
	if sphere.ray_hits_triangle(point,TRIANGLE):
		color = 1

	
	#screen.__setitem__(i, sfml.Vertex(sfml.Vector2(scrx,scry), color))
	screen[int(scrx)][int(scry)] = color

for i in range(WIDTH):
	print(screen[i])
	print()

"""
for i in range(WIDTH*HEIGHT):
	color = sfml.Color.RED
	scrx = i%WIDTH
	scry = (i-scrx)/WIDTH
	
	
	point = (scrx-(WIDTH>>1),scry-(HEIGHT>>1),0.001)
	
	print(point)
	
	if plane.ray_hits_triangle(point,TRIANGLE):
		color = sfml.Color.BLUE
	
	screen.__setitem__(i, sfml.Vertex(sfml.Vector2(scrx,scry), color))

"""
	
"""
for i in range(WIDTH*HEIGHT):
	color = sfml.Color.RED
	scrx = i%WIDTH
	scry = (i-scrx)/WIDTH
	
	print(scrx)
	print(scry)
	
	screen.__setitem__(i, sfml.Vertex(sfml.Vector2(scrx,scry), sfml.Color.RED, sfml.Vector2(scrx,scry)))
"""
"""
window = sfml.RenderWindow(sfml.VideoMode(WIDTH, HEIGHT), "pySFML Window")

while window.is_open:

	for event in window.events:
 
		if type(event) is sfml.CloseEvent:
			window.close()

	window.clear() # clear screen
	window.draw(screen)
	window.display() # update the window
"""