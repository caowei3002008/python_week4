def compareLists(list1,list2):
	if len(list1) != len(list2):
		print "The lists are not the same."
		return

	for i in range(0,len(list1)):
		if(list1[i] == list2[i]):
			continue
		else:
			print "The lists are not the same."
			return
	print "The lists are the same"
	return
compareLists([1,2,5,6,2],[1,2,5,2,2])


