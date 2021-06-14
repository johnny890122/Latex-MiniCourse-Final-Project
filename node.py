import const
from utility import *

class Node():
	def __init__(self, color, position):
		super(Node, self).__init__()
		self.position = closest_point(position[0], position[1])
		self.color = color
		self.radii = 25
		self.fill = const.color["white"]
		self.width = 3
		self.circle = None