file = open('1/input.txt')
depths = [int(i) for i in file.readlines()]
depths_bigger_than_before = 0
latest_depth = sum(depths[0:3])
for i in range(1,len(depths)-2):
	if sum(depths[i:i+3]) > latest_depth:
		depths_bigger_than_before += 1
	latest_depth = sum(depths[i:i+3])
print(depths_bigger_than_before)