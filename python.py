a = [25,56,58,45,78,25]

print(max(a))
print(min(a))
print(set(a))
duplicate = []
for i in range(len(a)):
	temp = i+1
	for j in range(temp,len(a)):
		if a[i]==a[j]:
			duplicate.append(a[i])
	 
print("This is the repeated no =",duplicate)