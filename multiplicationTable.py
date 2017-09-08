w, h = 13, 13;
list1 = [[0 for x in range(w)] for y in range(h)]
list1[0] = ['x',1,2,3,4,5,6,7,8,9,10,11,12]
print ' '.join(str(e) for e in list1[0])
for i in range(1,13):
	list1[i][0] = i
	for j in range(1,13):

		list1[i][j] = i * j
	
	print ' '.join(str(e) for e in list1[i])
