def two_sum(num,target):
	dic={}
	index_list = range(len(num))
	for n in index_list:
		a = target-num[n]#difference
		if dic.has_key(a):
			return [dic[a],n]
		else:
			dic[num[n]]=n



	
		
