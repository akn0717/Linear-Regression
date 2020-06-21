import pygame
import math
import numpy as np
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def get_point(self):
		return [self.x*512,512-self.y*512]
	def plot(self,screen):
		screen.fill(pygame.Color(255,0,0),(self.get_point(),(4,4)))

class Line:
	def __init__(self):
		self.a = np.random.rand()*2-1
		self.b = np.random.rand()*2-1
		self.lr = 0.7

	def get_x(self,y):
		return (y-self.b)/self.a

	def get_y(self,x):
		return self.a*x+self.b

	def plot(self,screen):
		p1 = Point(0,0)
		p2 = Point(0,0)
		if (abs(self.a)>abs(self.b)):
			p1.x = 0
			p1.y = self.get_y(p1.x)
			p2.x = 1
			p2.y = self.get_y(p2.x)
		else:
			p1.y = 0
			p1.x = self.get_x(p1.y)
			p2.y = 1
			p2.x = self.get_x(p2.y)
		pygame.draw.aaline(screen,pygame.Color(0,0,255),p1.get_point(),p2.get_point(),8)

	def fit(self,dataset):
		delta_a = 0
		delta_b = 0

		for p in dataset:
			delta_a += 2*(self.get_y(p.x)-p.y)*p.x
			delta_b += 2*(self.get_y(p.x)-p.y)

		self.a-=self.lr*(delta_a/len(dataset))
		self.b-=self.lr*(delta_b/len(dataset))