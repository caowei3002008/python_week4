def oddEven():
	for i in range(1,2001):
		if i%2 == 0:
			print 'Number is',i,'. This is and even number'
		else:
			print 'Number is',i,'. This is and odd number'
# print oddEven()

def multiply(list1,num):
	for i in range(0,len(list1)):
		list1[i] = num * list1[i]
	return list1

def layered_multiples(arr):
	length = len(arr)
	new_array = []
	for i in range(length):
		new_array.append([])
		count = arr[i]
		for j in range(count):
			new_array[i].append(1)
	return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
