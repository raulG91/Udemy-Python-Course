import json

contacts = [
    
    
    ("Juan","Analista","juan@analista.com"),
    ("Manolo","Desarrollador","manolo@test.com")
]

data=[]

for name, job, email in contacts:
    data.append({"name":name, "job":job,"email":email})
#write data into json file    
with open("files/contacts.json","w") as jsonfile:
    json.dump(data,jsonfile)    
    
#Read the data from JSON file

data = None

with open("files/contacts.json","r") as jsonfile:
   data = json.load(jsonfile)
    
#Loop over the data read

for contact in data:
    print(contact["name"], contact["job"],contact["email"])        