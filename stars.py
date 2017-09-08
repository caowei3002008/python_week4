def star_print(num):
	string = ''
	for count in range(0,num):
		string += '*'
	print string
	return num

def letterPrint(letter,num):
	string = ''
	for count in range(0,num):
		string += letter
	print string
	return letter	

def draw_stars(arr):
	for index in arr:
		if type(index) is int:
			star_print(index)
		elif type(index) is str:
			letterPrint(index[:1].lower(),len(index))
	return arr
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])



