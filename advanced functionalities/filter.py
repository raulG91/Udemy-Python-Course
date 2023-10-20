numbers = [3,5,10,25,45,46]

def multiple(num):
    if num % 5 == 0:
        return True
#Filter function receives a function an one iterable
#It returns also an iterable object
numbers_filter = filter(multiple,numbers)    
print(list(numbers_filter))