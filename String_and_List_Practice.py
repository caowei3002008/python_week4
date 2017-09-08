
# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
words =  words.replace('day','month')
print words
#Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
y = []
y.append(x[0])
y.append(x[len(x)-1])
print y
#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
z = []
a = []
for i in range(0,(len(x)/2)): 
	z.append(x[i])
a.append(z)
for i in range(len(x)/2, len(x)):
	a.append(x[i])
print a
