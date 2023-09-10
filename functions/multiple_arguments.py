#function with multiple arguments position
def inderminate_pos(*args):
    print(args)

inderminate_pos("String",20,[1,2,3,4])    

#Function with multiple arguments with names
def indeterminate_name(**kwargs):
    print(kwargs)

indeterminate_name(c="Cadena",n=8,l=[1,2.3])
