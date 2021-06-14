import const
from utility import *

class Edge(object):
	def __init__(self, start_x, start_y, end_x, end_y):
		super(Edge, self).__init__()
		self.color = const.edge_outline
		self.start_pos = closest_point(start_x, start_y)
		self.end_pos = closest_point(end_x, end_y)
		self.width = int()
		self.line = None
