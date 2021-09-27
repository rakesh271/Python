#-------------------------------------------------------
#Description : Function with return value 
#
#Function definition :
# def function_with_return_value():
#   statements
#   return(value);
#
#Function Call :
# function__with_return_value();
#-------------------------------------------------------

#Function Definition :
def function_with_return_value():
  name = "Nadeem";
  return("(Without Args)My name is "+name);

name_value = function_with_return_value();
print(name_value);

#-------------------------------------------------------
#Description : Function with return value with parameters 
#
#Function definition :
# def function_with_return_value(name):
#   statements
#   return(name);
#
#Function Call :
# function__with_return_value("value");
#-------------------------------------------------------


#Function Definition :
def function_with_return_value1(name):
  return("(With Args) My Name is " + name);

name_value2 =  function_with_return_value1('Nadeem');
print(name_value2);
