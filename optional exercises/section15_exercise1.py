people=[]
#Read the file
with open("optional exercises/section15_exercise1.txt","r") as file:
    
   lines = file.readlines()
   for line in lines:
       list = line.split(";")
       dic = {
           "id":list[0],
           "name":list[1],
           "last_name":list[2],
           "birth_date":list[3]
       }
       
       people.append(dic)
       
print(people)   