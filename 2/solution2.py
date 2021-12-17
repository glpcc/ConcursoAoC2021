
def load_file(route):
	file = open(route)
	return file.readlines()

lines = load_file('2/input.txt')
movement = [0,0,0]
directions = {
	'up':[0,0,-1],
	'down':[0,0,1],
}
for i in lines:
	direction = i.split(' ')
	direction[1] = int(direction[1].strip())
	if direction[0] in directions:
		movement[2] += directions[direction[0]][2] * direction[1]
	elif direction[0] == 'forward':
		movement[1] += direction[1]
		movement[0] += direction[1]*movement[2]

print(movement[0] * movement[1])