from collections import  Counter
from collections import defaultdict

list = [1,2,4,5,2,1,3,2,2,1,1,0]

c= Counter(list)

print(c)


#Method to returns most common elements
print(c.most_common())

#default dict is a dictionay but if we check a key that doesn´t exist it will create it 
# and it will be initializate with a default value

d = defaultdict(int)
# Any doesn´t exist as a  key 
d['any']
print(d['any'])
#A different value could be assigned
d['char'] = 'string'
print(d['char'])