class Example:
    #privaste attribute
    __private_attribute = "Test"
    
    def return_private_attribute(self):
         return self.__private_attribute
     

e = Example()
print(e.return_private_attribute())     