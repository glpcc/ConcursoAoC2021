file = open('6/input.txt')
fishes = [int(i) for i in file.readline().strip().split(',')]
print(fishes)
DAYS = 256
fishes_ages = {
	0:0,
	1:0,
	2:0,
	3:0,
	4:0,
	5:0,
	6:0,
	7:0,
	8:0
}
for i in fishes:
	fishes_ages[i] += 1

for i in range(DAYS):
	new_fishes = fishes_ages[0]
	for i in range(1,9):
		fishes_ages[i-1] = fishes_ages[i]

	fishes_ages[8] = new_fishes
	fishes_ages[6] += new_fishes



print(sum([fishes_ages[i] for i in range(9)]))