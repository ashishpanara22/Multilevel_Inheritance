class Vehical(): # main class or parent class
    __name_var = "Vehical" # this variable is private

class Car(Vehical): # child class of Vehical and Parent class of Model
    _vehical_type = "car" # this variable is protected

class Model(Car): # Child class of Car
    car_name = "Suzuki" # this variable is public

obj = Model() # call child class (Model)

print("Model name is",obj.car_name) # output of Model class
print("Model type is",obj._vehical_type) # output of Car class
print("Model category is",obj.__name_var) # this output produced error because private variable is not accessed directly