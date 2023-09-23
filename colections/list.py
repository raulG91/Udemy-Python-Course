l1 = [1,2,3]
l2 = [4,5,6]
#Inset pos 0 value -1
l1.insert(0,-1)
print(l1)
#Remove last element
l1.pop()
print(l1)
#Remove first element
l1.pop(0)
print(l1)

l1.append(23)
l1.reverse()
print(l1)

#OSort

l1.append(-8)
l1.append(100)
l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)