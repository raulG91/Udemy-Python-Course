import sys
from io import open

arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]    
counter = 0
try:
    file = open("counter.txt","r")
    counter = int(file.readline())
    file.close()
except:
    #File doesn't exist let's create it
    file = open("counter.txt","x")
    file.close()
    
    
        
#Reduce the number in the file
if arg.lower() == 'dec':
    counter = counter - 1
elif arg.lower() == "inc":
    counter +=1
else:
    print(counter) 
    
#write in the file new value
file = open("counter.txt","w")
file.write(str(counter))
            
    