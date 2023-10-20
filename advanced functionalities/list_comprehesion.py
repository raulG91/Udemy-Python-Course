list = [letter for letter in "casa"]

print(list)


list2 = [numero**2 for numero in range(0,11)]
print(list2)

list3 = [numero for numero in range(0,11) if numero % 2 == 0]
print(list3)

list4 = [ number for number in range(0,501) if number % 2 == 0 and number % 3 == 0 and number % 4 == 0 and number % 8 == 0]
print(list4)