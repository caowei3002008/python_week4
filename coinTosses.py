import random
def coinTosses(num):
	tail = 0
	head = 0
	print 'Starting the program...'
	for count in range(1,num+1):
		random_num = random.randint(0,1)
		if random_num == 0:
			head +=1
			print 'Attempt #',count,": Throwing a coin... It's a head! ... Got", head,"head(s) so far and",tail,"tail(s) so far"
		else:
			tail +=1
			print 'Attempt #',count,": Throwing a coin... It's a tail! ... Got", head,"head(s) so far and",tail,"tail(s) so far"
	print 'Ending the program, thank you!'

coinTosses(5000)