def typeList(list1):
	count1 = 0
	count2 = 0
	total = 0
	strOutput = ''
	for i in list1:
		if type(i) is int:
			count1 +=1
			total += i
		elif type(i) is float:
			count1 +=1
			total += i
		elif type(i) is str:
				count2 +=1
				strOutput += i
				strOutput += ' '
	length = len(list1)
	if count1 == length:
		print 'The list you entered is of integer type'	
		print 'sum:',total
	elif count2 == length:
		print 'The list you entered is of string type'
		print 'String:',strOutput
	else:
		print "The list you entered is of mixed type"
		print 'String:',strOutput
		print 'sum:',total
	return
typeList(['magical unicorns',19,'hello',98.98,'world'])
typeList([2,3,1,7,4,12])
typeList(['magical','unicorns'])

