file = open('5/input.txt')
lines = file.readlines()
directions = [i.split('->') for i in lines]
directions = [[[int(k) for k in i[0].strip().split(',')],[int(k) for k in i[1].strip().split(',')]] for i in directions]
appeared = set()
double = set()

for i in directions:
	if i[0][0] == i[1][0]:
		for j in range(min(i[0][1],i[1][1]),max(i[0][1],i[1][1])+1):
			if (i[0][0],j) in appeared:
				double.add((i[0][0],j))
			appeared.add((i[0][0],j))
	elif i[0][1] == i[1][1]:
		for j in range(min(i[0][0],i[1][0]),max(i[0][0],i[1][0])+1):
			if (j,i[0][1]) in appeared:
				double.add((j,i[0][1]))
			appeared.add((j,i[0][1]))


print((99,450) in appeared)
for i in range(93,582+1):
	if (i,450) not in appeared:
		print(i)
print(len(double))