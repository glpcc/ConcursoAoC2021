file = open('6/input.txt')
fishes = [int(i) for i in file.readline().strip().split(',')]
print(fishes)
DAYS = 256

for i in range(DAYS):
	print(f'Day {i} ...')
	for j in range(len(fishes)):
		if fishes[j] == 0:
			fishes[j] = 6
			fishes.append(8)
		else:
			fishes[j] -= 1

print(len(fishes))