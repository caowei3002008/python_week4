#Multiple part 1
def printOddNumber():
	for i in range(1,1000,2):
		print i
	return
# printOddNumber()
#multiple part 2
def printAllTheMultiple():
	for i in range(5,1000001):
		if(i%5 == 0):
			print i 
	return
# printAllTheMultiple()

#Sum List and average
a = [1, 2, 5, 10, 255, 3]
sum = 0;
for i in a:
	sum +=i
print sum

print 'The list average is',sum/len(a)