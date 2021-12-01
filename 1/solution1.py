file = open('1/input.txt')
depths = [int(i) for i in file.readlines()]
depths_bigger_than_before = 0
latest_depth = depths[0]
for i in depths[1:]:
	if i > latest_depth:
		depths_bigger_than_before += 1
	latest_depth = i
print(depths_bigger_than_before)