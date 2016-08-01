a = [2, 4, 10, 16]

def multiply(arr,num):
	for i in range(len(arr)):
		arr[i] = arr[i] * num
	return arr

b = multiply(a,5)
print b


[10, 20, 50, 80]
