file = open('7/input.txt')
crabs_pos = [int(i) for i in file.readline().strip().split(',')]
print(crabs_pos)

def fuel_consumption(pos_i,pos_f):
	diference = abs(pos_f-pos_i)
	return (diference*(diference+1))//2


def calculate_fuel(crabs_pos,pos):
	
	return sum([fuel_consumption(j,pos) for j in crabs_pos])


print(min([calculate_fuel(crabs_pos,i) for i in range(max(crabs_pos)+1)]))

