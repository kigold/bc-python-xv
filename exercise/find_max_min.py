def find_max_min(num):
	min = num[0]
	max = num[0]
	for i in num:
		if i<min:
			min = i
		if i>max:
			max = i
        if max == min :
                return min
        else:
                return [min,max]
