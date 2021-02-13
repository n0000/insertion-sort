
arr = [21,35,17,48,52,15,21,14,23]

for i in range(1,len(arr)):
	smuch = arr[i]
	for j in range(i-1):
		if smuch < arr[j]:
			a=arr.pop(i)
			arr.insert(j,a)
		
			break
print(arr)
