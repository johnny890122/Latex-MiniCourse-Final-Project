import pygame

######################### 螢幕顯示的參數 #########################

# the width and height of screen 
screen_width, screen_height = int(), int()
screen_size = screen_width, screen_height

# Some RBG code
color = {
			"black": (0, 0, 0),
			"white": (255, 255, 255),
			"red": (255, 38, 1),
			"blue": (2, 77, 153),
			"green": (4, 100, 3),
			"brown": (48, 45, 36),
			"gray": (192,192,192),
			"pink": (230, 37, 91),
			"orange": (254, 116, 0),
			"mud": (78, 57, 1),
}

inverse_color = {
					(0, 0, 0): "black",
					(255, 255, 255): "white",
					(255, 38, 1): "red",
					(2, 77, 153): "blue",
					(4, 100, 3): "green",
					(48, 45, 36): "brown",
					(192,192,192): "gray",
					(230, 37, 91): "pink",
					(254, 116, 0): "orange",
					(78, 57, 1): "mud",
}

########################## Event Type #################################
'''
Keyboard Event 
'''
key = {
		"left": pygame.K_LEFT,
		"right": pygame.K_RIGHT,
		"up": pygame.K_UP,
		"down": pygame.K_DOWN,
		"esc": pygame.K_ESCAPE,
		"quit": pygame.QUIT,
		"space": pygame.K_SPACE,
}


'''
Mouse event 
'''
position = int(), int()
last_pos = int(), int()
mouse = {
		"down": pygame.MOUSEBUTTONDOWN,
		"up": pygame.MOUSEBUTTONUP,
		"pos_moving": False,
		"x_pos": position[0],
		"y_pos": position[1],
}

click_type = {
				"left": 1,
				"middle": 2,
				"right": 3,
				"scroll_up": 4,
				"scroll_down": 5,		
}

######################### Object configuration ##################################

'''
Grid information
'''
grid_origin = (300, 50)
grid_unit = 50

grid_width = 1400
grid_height = 850

'''
Side bar information
'''
option_width = 80
option_height = 400

style_width = 300
style_height = 500


'''
Node information
'''
node_code, node_outline = "c1", color["black"]
edge_code, edge_outline = "c1", color["black"]


'''
Style information
'''
color_pos = {
				"c1": (159, 285), "c2": (208, 285), "c3": (255, 285), "c4": (304, 285), 
				"c5": (159, 343), "c6": (208, 343), "c7": (255, 343), "c8": (304, 343),
				
}
