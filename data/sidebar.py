import data.const as const

class SideBar():
	def __init__(self):
		super(SideBar, self).__init__()
		self.color = const.color["brown"]
		self.show_style = False
		self.node = None
		self.line = None
		self.eraser = None
		self.color_option = {
								"c1": None, "c2": None, "c3": None,
								"c4": None, "c5": None, "c6": None,
		}
		self.color_option_rgb = {
								"c1": const.color["white"], "c2": const.color["black"], "c3": const.color["blue"], 
								"c4": const.color["red"], "c5": const.color["mud"], "c6": const.color["green"], 
								"c7": const.color["orange"], "c8": const.color["pink"]
		}

		self.thick_option = {
								"t1": None, "t2": None, "t3": None,
		}

		self.edge_option = {
								"e1": None, "e2": None,
		}

		'''
		清單：
		1. 背景的正方形
		2. Node 選項
		3. Edge 選項 
		'''

		# 背景的正方形
		self.option_origin = (50, const.screen_height//2 - 452//2)
		self.option_width = const.option_width
		self.option_height = const.option_height

		self.eraser_origin = (45, const.screen_height//2 + const.option_height//3)

		# Node Option
		self.node_color = const.color["black"]
		self.node_position = 50 + 123 //4+1, const.screen_height//2 - 450//4 +1
		self.node_radius = 22

		# Edge Option
		self.line_color = const.color["white"]
		self.line_start = (50 + 123 //4 + 3, const.screen_height//2 + 120//4 - 22)
		self.line_end = (50 + 123 //4 + 3, const.screen_height//2 + 120//4 + 22)

		'''
		樣式：
		1. 背景的長方形
		2. color option
		3. width option
		'''

		self.style_origin = (120,  const.screen_height//2 - const.style_height//2)
		self.style_width = const.style_width
		self.style_height = const.style_height
