input = open('3/input.txt')
input = [i.strip() for i in input.readlines()]
gamma = ''
epsilon = ''
for i in range(len(input[0])):
	numer_of_ones = sum([int(j[i]) for j in input])
	if numer_of_ones >= len(input)/2:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

print(gamma)
print(epsilon)
oxigen_rates = input
oxigen_rate = ''
co2_rates = input
co2_rate = ''
def most_common(list,position):
	ones = sum([int(i[position]) for i in list])
	if ones >= len(list)/2:
		return '1'
	else:
		return '0'

def leas_common(list,position):
	ones = sum([int(i[position]) for i in list])
	if ones >= len(list)/2:
		return '0'
	else:
		return '1'
for i in range(len(input[0])):


	if oxigen_rate == '':
		oxigen_rates = [j for j in oxigen_rates if j[i] == most_common(oxigen_rates,i)]


	if co2_rate == '':
		print(co2_rates)
		print(i)
		print(leas_common(co2_rates,i))
		co2_rates = [k for k in co2_rates if k[i] == leas_common(co2_rates,i) ]

	if len(oxigen_rates) == 1:
		oxigen_rate = oxigen_rates[0]
	
	if len(co2_rates) == 1:
		co2_rate = co2_rates[0]

print(oxigen_rate)
print(co2_rate)
print(int(oxigen_rate,2)*int(co2_rate,2))
