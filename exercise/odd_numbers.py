def odd_numbers(low,high):
	odd=[]
	if (type(low) == int and type(high) == int) and low < high:
		for n in range(low,high+1):
			if n%2:
				odd.append(n)
		return odd
	else:
		print "Input numbers are not integers, or ar not in correct order"
