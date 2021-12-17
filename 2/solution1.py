
def load_file(route):
	file = open(route)
	return file.readlines()

lines = load_file('2/input.txt')
movement = [0,0]
directions = {
	'up':[-1,0],
	'down':[1,0],
	'forward':[0,1],
}
for i in lines:
	direction = i.split(' ')
	direction[1] = int(direction[1].strip())
	movement[0] += directions[direction[0]][0] * direction[1]
	movement[1] += directions[direction[0]][1] * direction[1]

print(movement[0] * movement[1])