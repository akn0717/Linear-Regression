import pygame
from Line import *
w = 512
h = 512

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill((255,255,255))
clock = pygame.time.Clock()
clock.tick(60)

dataset = []
L = Line()
num = 0
while (True):
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			pygame.quit()
			break
		elif (event.type == pygame.MOUSEBUTTONUP):
			p = event.pos
			print(p)
			dataset.append(Point(p[0]/512,(512-p[1])/512))
			num+=1
	#L.plot(screen)
	if (pygame.time.get_ticks()%30==0):
		screen.fill((255,255,255))
		L.plot(screen)
		for p in dataset:
			p.plot(screen)
	if (pygame.time.get_ticks()%30==0 and len(dataset)>=1):
		#print(L.a," ",L.b)
		L.fit(dataset)
		print(L.a," ",L.b)
	pygame.display.update()