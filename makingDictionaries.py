name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
	new = zip(arr1,arr2)
	new_dict = dict(new)
	return new_dict
print make_dict(name,favorite_animal)