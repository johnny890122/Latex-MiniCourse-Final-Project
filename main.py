import pygame
import const
from renderer import Renderer
from node import Node
from edge import Edge
from sidebar import SideBar
from grid import Grid
from utility import *

class Canvas():
	def __init__(self):
		super(Canvas, self).__init__()
		# 初始化pygame 和顯示在畫布上的物件 
		pygame.init() 
		self.renderer = Renderer() 
		self.clock = pygame.time.Clock()
		self.sidebar = SideBar()
		self.renderer.set_option_pos(self.sidebar)

		self.grid = Grid(unit = const.grid_unit, 
						 width = const.grid_width, 
						 height = const.grid_height,
						 origin = const.grid_origin)
		self.obj_dct = {
						"node": list(),
						"edge": list(),
		}
		
		self.mode = "node" # 預設模式為 node 
		self.click = 0
		self.printer = self.renderer.draw_printer()
		self.display_canvas() # 進入主程式

	def event_listener(self):
		for event in pygame.event.get():
			# 追蹤滑鼠目前的座標
			if const.mouse["pos_moving"]:
				const.last_pos = const.mouse["x_pos"], const.mouse["y_pos"]
				const.position = const.mouse["x_pos"], const.mouse["y_pos"] = pygame.mouse.get_pos()

			if event.type == const.key["quit"]: # 退出程式
				sys.exit()
			
			elif event.type == const.mouse["down"]: # 按下滑鼠
				if event.button == const.click_type["left"]: # 按下滑鼠右鍵
					const.mouse["pos_moving"] = True

				elif event.button == const.click_type["right"]: # 按下滑鼠左鍵
					if self.sidebar.eraser.collidepoint(const.position):
						self.mode = "erase"
						for obj_type, obj_lst in self.obj_dct.items():
							self.obj_dct[obj_type] = list()
								

			elif event.type == const.mouse["up"]: # 放開滑鼠
				if event.button == const.click_type["left"]: # 放開滑鼠右鍵
					const.mouse["pos_moving"] = False

					''' 切換不同模式 '''
					if self.sidebar.node.collidepoint(const.position): # 切換至 node mode 
						self.mode = "node"
						self.click = 0
					elif self.sidebar.line.collidepoint(const.position): # 切換至 edge mode 
						self.mode = "edge"
						self.click = 0
					elif self.sidebar.eraser.collidepoint(const.position): # 切換至 erase mode 
						self.mode = "erase"
						self.click = 0
					elif self.printer.collidepoint(const.position): # 切換至 output mode 
						if self.obj_dct["node"] != list() or self.obj_dct["edge"] != list():
							to_tikz(self.obj_dct["node"], self.obj_dct["edge"])
					
					''' 不同模式相對應的行為 '''
					if self.mode == "edge": # Edge mode 
						if in_grid(self.grid) and not self.sidebar.show_style:
							self.click += 1
							if self.click == 2:
								self.click = 0
								self.obj_dct["edge"].append(Edge(const.last_pos[0], const.last_pos[1],
															 const.position[0], const.position[1]))
						elif self.sidebar.show_style:
							for key, obj in self.sidebar.color_option.items():
								if obj.collidepoint(const.position):
									const.node_code = key
									const.edge_outline = self.sidebar.color_option_rgb[key]
					
					elif self.mode == "node": # Node mode 
						if in_grid(self.grid) and not self.sidebar.show_style:
							self.obj_dct["node"].append(Node(const.node_outline, const.position))
						if self.sidebar.show_style:
							for key, obj in self.sidebar.color_option.items():
								if obj.collidepoint(const.position):
									const.node_code = key
									const.node_outline = self.sidebar.color_option_rgb[key]

					elif self.mode == "erase": # Erase mode 
						for obj_type, obj_lst in self.obj_dct.items():
							for index, obj in enumerate(obj_lst):
								if obj_type == "node" and obj.circle.collidepoint(const.position):
									del obj_lst[index]
								elif obj_type == "edge" and obj.line.collidepoint(const.position):
									del obj_lst[index]

				elif event.button == const.click_type["right"]: # 放開滑鼠左鍵
					if self.sidebar.node.collidepoint(const.position): # 展示 node style 選項
						self.mode = "node"
						if self.sidebar.show_style:
							self.sidebar.show_style = False
						else:
							self.sidebar.show_style = True
					elif self.sidebar.line.collidepoint(const.position): # 展示 edge style 選項
						self.mode = "edge"
						if self.sidebar.show_style:
							self.sidebar.show_style = False
						else:
							self.sidebar.show_style = True

	def display_canvas(self):
		while True: # 開始主程式的無窮迴圈
			self.renderer.screen.fill(const.color["white"])  # 背景底色為白色
			self.event_listener() # 開始讀取目前發生的事件
			self.renderer.draw_grid(self.grid)
			self.renderer.draw_obj(self.obj_dct) # 繪製物件
			self.renderer.draw_sidebar(self.sidebar, self.mode) # 繪製側邊欄
			self.renderer.draw_printer() # 繪製輸出按鈕
			pygame.display.flip() # 重新整理圖
			self.clock.tick(60)

if __name__ == '__main__':
	Canvas()
