import sfml
import sphere

WIDTH = 240
HEIGHT = 120

SIZE = 4.7

screen = sfml.VertexArray(sfml.PrimitiveType.POINTS, WIDTH*HEIGHT)

TRIANGLE = ((0,1,120),(1,1,120),(1,1,120))


for i in range(WIDTH*HEIGHT):
	color = sfml.Color.RED
	scrx = i%WIDTH
	scry = (i-scrx)/WIDTH
	
	
	point = (-(scrx-(WIDTH>>1)),-(scry-(HEIGHT>>1)),120)
	
	print(point)
	
	if sphere.ray_hits_triangle(point,TRIANGLE):
		color = sfml.Color.BLUE
	
	screen.__setitem__(i, sfml.Vertex(sfml.Vector2(scrx,scry), color))




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

window = sfml.RenderWindow(sfml.VideoMode(WIDTH, HEIGHT), "pySFML Window")

while window.is_open:

	for event in window.events:
 
		if type(event) is sfml.CloseEvent:
			window.close()

	window.clear() # clear screen
	window.draw(screen)
	window.display() # update the window