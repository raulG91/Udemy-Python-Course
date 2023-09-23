def modify(lista):
    
    #Delete duplicates
    
    list_copy = list(set(lista))
    print(list_copy)
    
    #Sort list
    list_copy.sort(reverse=True)
    print("Sort list ", list_copy)
    
    #Remove odd numbers 
    new_list = []
    for value in list_copy:
        if value%2==0:
            new_list.append(value)
            
    print("After remove odd numbers ", new_list)        
    
    #Sum remains numbers
    
    sum = 0
    for value in new_list:
        sum+=value
    print("Sum values", sum)
    
    #Add sum as first element
    
    new_list.insert(0,sum)
    print(new_list)
    
    
    
lista = [1,3,4,5,6,4,1,0,4,]   
 
modify(lista)
print("List original",lista)