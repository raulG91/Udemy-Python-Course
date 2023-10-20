numbers = [2,5,6,10,27]

def double(number):
    return number * 2

#Map applies the same function to all elements in the list
# and retruns an iterable
new_list = map(double,numbers)

print(list(new_list))