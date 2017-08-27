a = [1, 7, 9, 11, 13]
b = [2, 4, 6, 8, 14]


def arr_sort(arr_1, arr_2):
	res = []
	i = 0
	j = 0
	while True:
		if arr_1[i] < arr_2[j]:
			res.append(arr_1[i])
			i += 1			
		else:
			res.append(arr_2[j])
			j += 1
	return res

print a[0]
result = arr_sort(a, b)
print result
