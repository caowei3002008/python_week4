def integerFliter(num):
	if num >= 100:
		print "That's a big number!"
	else:
		print "That's a small number"
	return
# integerFliter(45)
def stringFliter(str):
	length = len(str)
	if length >=50:
		print "Long sentence."
	else:
		print "Short sentence."
	return
# stringFliter("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
def listFliter(list):
	length = len(list)
	if length >= 10:
		print "Big list!"
	else:
		print "Short list."
	return
# listFliter([4,34,22,68,9,13,3,5,7,9,2,12,45,923])