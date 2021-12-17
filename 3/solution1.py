input = open('3/input.txt')
input = [i.strip() for i in input.readlines()]
gamma = ''
epsilon = ''
for i in range(len(input[0])):
	numer_of_ones = sum([int(j[i]) for j in input])
	if numer_of_ones > len(input)/2:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

print(int(gamma,2)*int(epsilon,2))
print(int(epsilon,2))
print