from model import Model

obj = Model() # call child class (Model)

print("Model name is",obj.car_name) # output of Model class
print("Model type is",obj._vehical_type) # output of Car class
try:
    print("Model category is",obj.__name_var) # this output produced error because private variable is not accessed directly
except:
    print("variable __name_var is private")