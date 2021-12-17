file = open('5/input.txt')
lines = file.readlines()
directions = [i.split('->') for i in lines]
directions = [[[int(k) for k in i[0].strip().split(',')],[int(k) for k in i[1].strip().split(',')]] for i in directions]
appeared = set()
double = set()


		
for i in directions:
	x1,x2,y1,y2 = i[0][0], i[1][0], i[0][1], i[1][1]
	if x1 == x2:
		for j in range(min(y1,y2),max(y1,y2)+1):
			if (x1,j) in appeared:
				double.add((x1,j))
			appeared.add((x1,j))
	elif y1 == y2:
		for j in range(min(x1,x2),max(x1,x2)+1):
			if (j,y1) in appeared:
				double.add((j,y1))
			appeared.add((j,y1))
	elif x1 < x2:
		if y1 > y2:
			for j in range(x1,x2+1):
				if (j,y1 - (j-x1)) in appeared:
					double.add((j,y1 - (j-x1)))
				appeared.add((j,y1 - (j-x1)))
		else:
			for j in range(x1,x2+1):
				if (j,y1 + (j-x1)) in appeared:
					double.add((j,y1 + (j-x1)))
				appeared.add((j,y1 + (j-x1)))
	elif x2 < x1:
		if y1 > y2:
			for j in range(x2,x1+1):
				if (j,y2 + (j-x2)) in appeared:
					double.add((j,y2 + (j-x2)))
				appeared.add((j,y2 + (j-x2)))
		else:
			for j in range(x2,x1+1):
				if (j,y2 - (j-x2)) in appeared:
					double.add((j,y2 - (j-x2)))
				appeared.add((j,y2 - (j-x2)))


print((99,450) in appeared)
for i in range(93,582+1):
	if (i,450) not in appeared:
		print(i)
print(len(double))