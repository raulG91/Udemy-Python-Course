import sys

print(sys.argv)

if len(sys.argv) == 3:
    
    print("There is 2 arguments")
    
    for argument in sys.argv:
        print(argument)
        
else:
    print("We need 2 arguments")        