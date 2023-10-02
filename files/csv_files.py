import csv

contacts = [
    
    
    ("Juan","Analista","juan@analista.com"),
    ("Manolo","Desarrollador","manolo@test.com")
]

#Write a csv file with all contacts
with open("files/contactos.csv","w",newline="\n") as file:
    #Create a writer from  class csv
    writer =csv.writer(file,delimiter=",")
    for contact in contacts:
        writer.writerow(contact)
#Read file        
with open("files/contactos.csv","r",newline="\n") as file: 
    reader = csv.reader(file,delimiter=",")
    for contact in reader:
        print(contact)