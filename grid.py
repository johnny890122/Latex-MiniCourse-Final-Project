import const

class Grid():
	def __init__(self, unit, width, height, origin):
		super(Grid, self).__init__()
		self.unit = unit
		self.width = width
		self.height = height
		self.origin = origin
		self.color = const.color["gray"]
		self.rect = None


		