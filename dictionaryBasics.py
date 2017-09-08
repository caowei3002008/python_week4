personaldata = {"name":"Anna","age":101,"country":"The United States","language":"Python"}
for key,data in personaldata.iteritems():
	if key is 'name':
		print "My name is",data
	elif key is 'age':
		print "My age is",data
	elif key is 'country':
		print "My country of birth is",data
	elif key is 'language':
		print "My favorite language is",data
