def isprime(x):
	for i in range(2,x-1):
		if x%i == 0:
			return False
		else:
			return True
def fooAndBar(num):
	if num<100 or num >100000:
		return 'out of range'
	else:
		for j in range(2,317):
			if j*j == num:
				return "Bar"
		result = isprime(num)
		if result == True:
			return "Foo"
		else:
			return "FooBar"

print fooAndBar(10000)

