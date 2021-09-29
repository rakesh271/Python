#-------------------------------------------------------
#Description : Function with keyword based arguments 
#
#Function definition :
# def function_simple(name,number=12,members=0):
#   statements
#
#Function Call :
# function_simple(name="Happy",number=23);
#-------------------------------------------------------

#Function Definition :
def function_with_keyword_based_args(name,number=12,members=0):
  print(name+"'s","number is : ",number);

#Function Call :
function_with_keyword_based_args(number=4,name="Happy");

#Function Definition :
def function_with_keyword_based_args(name,number):
  print(name+"'s","number is",number);

#Function Call :
function_with_keyword_based_args(number=7,name="Rose");

