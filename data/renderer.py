import pygame
from pygame import gfxdraw
import data.const as const
from data.utility import *

class Renderer():
	def __init__(self):
		super(Renderer, self).__init__()
		pygame.init()
		self.screen = pygame.display.set_mode((1330, 855))
		const.screen_width = self.screen.get_width()
		const.screen_height = self.screen.get_height()
		# print(const.screen_width, const.screen_height)
		self.img_dct = {
						 "printer": pygame.image.load("data/img/printer.png").convert_alpha(),
						 "eraser_no": pygame.image.load("data/img/eraser_no.png").convert_alpha(),
						 "eraser_yes": pygame.image.load("data/img/eraser_yes.png").convert_alpha(),
						 "bar": pygame.image.load("data/img/bar.png").convert_alpha(),
						 "node_style": pygame.image.load("data/img/node_style.png").convert_alpha(),
						 "edge_style": pygame.image.load("data/img/edge_style.png").convert_alpha(),
		}
		self.resize_img()

	# 改變圖片的長寬至適合大小
	def resize_img(self):
		self.img_dct["eraser_yes"] = pygame.transform.scale(self.img_dct["eraser_yes"], (const.option_width, const.option_width))
		self.img_dct["eraser_no"] = pygame.transform.scale(self.img_dct["eraser_no"], (const.option_width, const.option_width))

	# 繪製「圓」的函數
	def draw_circle(self, node):
		node.circle = self.aaring(node.position, node.radii, node.width, node.color, const.color["white"])

	# 繪製「線」的函數
	def draw_edge(self, edge):
		edge.line = pygame.draw.aaline(self.screen, edge.color, edge.start_pos, edge.end_pos, 1)

	# 繪製「環」的函數
	def aaring(self, position, radius, width, color, filled_color):
		node = pygame.draw.circle(self.screen, (0,0,0,0), position, radius*0.95)
		pygame.gfxdraw.filled_circle(self.screen, position[0], position[1], radius, color)
		pygame.gfxdraw.aacircle(self.screen, position[0], position[1], radius, color)
		pygame.gfxdraw.filled_circle(self.screen, position[0], position[1], radius - width, filled_color)
		pygame.gfxdraw.aacircle(self.screen, position[0], position[1], radius - width, filled_color)
		return node

	# 繪製「網格」的函數
	def draw_grid(self, grid):
		for x in range(grid.origin[0], grid.width, grid.unit):
			for y in range(grid.origin[1], grid.height, grid.unit):
				rect = pygame.Rect(x, y, grid.unit, grid.unit)
				pygame.draw.rect(self.screen, grid.color, rect, 1)
		grid.rect = pygame.Rect(grid.origin[0], grid.origin[1], grid.width, grid.height)

	def draw_sidebar(self, sidebar, mode):
		'''橡皮擦的方塊'''
		rect = pygame.Rect(sidebar.eraser_origin[0], sidebar.eraser_origin[1], 
						   sidebar.option_width, sidebar.option_width)
		sidebar.eraser = pygame.draw.rect(self.screen, const.color["white"], rect)

		sidebar.node = pygame.draw.circle(self.screen, const.node_outline, sidebar.node_position, 30)
		if sidebar.show_style and mode == "node":
			self.screen.blit(self.img_dct["node_style"], (sidebar.option_origin[0], sidebar.option_origin[1]))

		elif sidebar.show_style and mode == "edge":
			self.screen.blit(self.img_dct["edge_style"], (sidebar.option_origin[0], sidebar.option_origin[1]))
		else:
			self.screen.blit(self.img_dct["bar"], (sidebar.option_origin[0], sidebar.option_origin[1]))

		'''選項被選中/沒選中'''
		if mode == "node":
			# Node 顯示為目前樣式
			pygame.gfxdraw.aacircle(self.screen, sidebar.node_position[0], sidebar.node_position[1], sidebar.node_radius + 6, const.color["white"])
			# 其餘顯示為 default 
			self.screen.blit(self.img_dct["eraser_no"], (sidebar.eraser_origin[0], sidebar.eraser_origin[1]))
			sidebar.line = pygame.draw.line(self.screen, const.edge_outline, sidebar.line_start, sidebar.line_end, 2)
		elif mode == "edge":
			# Edge 顯示為目前樣式
			sidebar.line = pygame.draw.line(self.screen, const.edge_outline, sidebar.line_start, sidebar.line_end, 5)
			pygame.gfxdraw.aacircle(self.screen, 83, 457, 28, const.color["white"])

			# 其餘顯示為 default 
			self.screen.blit(self.img_dct["eraser_no"], (sidebar.eraser_origin[0], sidebar.eraser_origin[1]))
		elif mode == "erase":
			# Eraser 顯示為目前樣式
			self.screen.blit(self.img_dct["eraser_yes"], (sidebar.eraser_origin[0], sidebar.eraser_origin[1]))
			# 其餘顯示為 default 
			sidebar.line = pygame.draw.line(self.screen, const.edge_outline, sidebar.line_start, sidebar.line_end, 2)

	def draw_printer(self):
		rect = pygame.Rect(45, const.screen_height//2 + const.option_height//3 + 170, 75, 75)
		pygame.draw.rect(self.screen, const.color["white"], rect)
		return self.screen.blit(self.img_dct["printer"], (45, const.screen_height//2 + const.option_height//3 + 170))
		

	# 繪製 node edge 物件
	def draw_obj(self, object_dct):
		for obj in object_dct["edge"]:
			self.draw_edge(obj)
		for obj in object_dct["node"]:
			self.draw_circle(obj)

	# 設定 sidebar 顏色選項的位置和圓
	def set_option_pos(self, sidebar):
		for key, value in const.color_pos.items():
			sidebar.color_option[key] = pygame.draw.circle(self.screen, const.color["white"], value, 20)

