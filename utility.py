import const

# 將滑鼠選取位置校正至網格上
def closest_point(x,y):
	if (x - const.grid_origin[0]) % const.grid_unit < const.grid_unit//2:
		x = const.grid_origin[0] + ((x- const.grid_origin[0]) // const.grid_unit) * (const.grid_unit)
	else:
		x = const.grid_origin[0] + ((x- const.grid_origin[0]) // const.grid_unit + 1) * (const.grid_unit)

	if (y - const.grid_origin[0]) % const.grid_unit < const.grid_unit//2:
		y = const.grid_origin[0] + ((y- const.grid_origin[0]) // const.grid_unit) * (const.grid_unit)
	else:
		y = const.grid_origin[0] + ((y- const.grid_origin[0]) // const.grid_unit + 1) * (const.grid_unit)
	return (x, y)

# 判斷是否繪製在網格中的函數
def in_grid(grid):
	if grid.origin[0] - grid.unit//3 < const.position[0] and const.position[0] < grid.origin[0] + grid.width - 270:
		if grid.origin[1] - grid.unit//3 < const.position[1] and const.position[1] < grid.origin[1] + grid.height - 30:
			return True
	return False

# 取絕對值的函數
def abs(a):
	if a < 0:
		return -a
	return a

# 判斷兩個 node 的相對位置，並輸出相對應的 Tikz code
def relative_pos(parent, child, parent_id, child_id):
	w, h = abs((child.position[0] - parent.position[0])//50), (child.position[1] - parent.position[1])//50

	pos = str()
	if child.position[0] < parent.position[0]:
		pos = "left"
	else:
		pos = "right"

	state = "state"
	if child.color != const.color["black"]:
		state += ", " + f"draw = {const.inverse_color[child.color]}"

	out = "\t" + f"\\node[{state}] (x{child_id}) [below {pos} = {h}.0cm and {w}.0cm of x{parent_id}] {{$x_{child_id}$}};" + "\n"
	return out


# 將 node 和 edge 的相對位置以 tree 的方式儲存起來
def build_tree(node_lst, edge_lst):
	lst = [-1 for _ in range(len(node_lst))]

	parent, child = int(), int()
	parent_pos, child_pos = tuple(), tuple()
	for edge in edge_lst:
		if edge.start_pos[1] > edge.end_pos[1]:
			parent_pos = edge.end_pos
			child_pos = edge.start_pos
		else:
			parent_pos = edge.start_pos
			child_pos = edge.end_pos

		for index, node in enumerate(node_lst):
			if parent_pos == node.position:
				parent = index
			elif child_pos == node.position:
				child = index
		if lst[child] == -1:
			lst[child] = parent


	levels = [-1 for _ in range(len(node_lst))]
	for index, root in enumerate(lst):
		cnt = 0
		while root != -1:
			root = lst[root]
			cnt += 1
		levels[index] = cnt
	return lst, levels

# 輸出 latex code 的主函數
def to_tikz(node_lst, edge_lst):
	root, levels = build_tree(node_lst, edge_lst)
	cnt = max(levels)
	out_lst = list()
	while cnt != 0:
		for index, level in enumerate(levels):
			if level == cnt:
				out = relative_pos(node_lst[root[index]], node_lst[index], root[index], index)
				out_lst.append(out)
		cnt -= 1

	state = "state"
	
	for index, level in enumerate(levels):
		if level == 0:
			if node_lst[index].color != const.color["black"]:
				state += ", " + f"draw = {const.inverse_color[node_lst[index].color]}"
			out_lst.append("\t" +f"\\node[{state}] (x{index}) at (0,0) {{$x_{index}$}};" + "\n")

	with open('output/test.tex', 'w') as f:
		f.write("\\documentclass{standalone}\n")
		f.write("\\usepackage{tikz, xcolor}\n")
		f.write("\\usetikzlibrary{positioning}\n")
		f.write("\\tikzset{state/.style={draw, circle, inner sep=0pt, minimum size=7mm, fill=white, line width=1pt}}\n")
		f.write("\\begin{document}\n")
		f.write("\t\\begin{tikzpicture}\n")

		# for node position
		for i in range(len(out_lst)):
			f.write(out_lst[len(out_lst) - i -1])

		# for edge position
		for index in range(len(root)):
			if root[index] != -1:
				f.write("\t" + f"\\draw (x{root[index]}) -- (x{index});" + "\n")

		f.write("\t\\end{tikzpicture}\n")
		f.write("\\end{document}\n")
	f.close()
