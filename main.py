# Define a class in Python to store the details of a Ship (name, source, destination) with the following methods
# 1. get_details()--> to assign values to class attributes
# 2. print_details--> to display the sttribute values
# Create an object of the class and invoke the methods 

class Ship:
  def get_details(self):
    self.name=input() 
    self.source=input() 
    self.destination=input() 

  def print_details(self):
    print("\nShip Details:-")
    print("Name:",self.name)
    print("Source:",self.source)
    print("Destination:",self.destination)

S1=Ship()
S1.get_details()
S1.print_details()