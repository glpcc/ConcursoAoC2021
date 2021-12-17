file = open('7/input.txt')
crabs_pos = [int(i) for i in file.readline().strip().split(',')]


def calculate_fuel(crabs_pos,pos):
	return sum([abs(j-pos) for j in crabs_pos])

print(min([calculate_fuel(crabs_pos,i) for i in set(crabs_pos)]))