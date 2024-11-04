"""class rajendra:
    def naidu(self,name,gender):  #method
        self.name=name   #attr  name gender
        self.gender=gender
        print("name",self.name)
        print("gender",self.gender)

obj=rajendra()  #obj created     in heep memory  ()-<constructor will decide size of memeory
obj1=rajendra()
obj.naidu("boyapati","king")  #calling the method
obj1.naidu("wise","gelio")

"""

#--init-- like c++ constructor   F-strings are a powerful feature in Python for creating dynamic strings that include 
# variable values or expressions, making string manipulation more efficient 
'''
class car:
    def __init__(self,model,year):
       self.model=model
       self.name=year

    def model_car(self):
      # return f"this car model {self.model}"
       print("model",self.model)
    def year_car(self):
       #return f"this car year {self.year}"
       print("year",self.year)
obj=car("maruthi",2000)
print(obj.model_car())
print(obj.year_car())
'''
'''
class Car:
    def __init__(self, model, year):
        self.model = model  # Set the car model
        self.year = year    # Set the car year

    def model_car(self):
        """Method to describe the car model."""
        return f"This car model is {self.model}"

    def year_car(self):
        """Method to describe the car year."""
        return f"This car year is {self.year}"

# Creating an instance of the Car class
obj = Car("Maruthi", 2000)

# Using the methods
print(obj.model_car())  # Output: This car model is Maruthi
print(obj.year_car())    # Output: This car year is 2000
'''

#print(f"string literals {2+3}")

#i=1
#while(i<5):
 #   i+=1
#print(i)

for i in range(1,6):
    print(i)