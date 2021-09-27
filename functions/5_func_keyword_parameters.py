#-------------------------------------------------------
# 
#Description : Function with non_keyword based arguments
#
#Function definition :
# def function_with_non-keyword_based_arguments(*parameters):
#   statements
#
#Function Call :
# function_with_non-keyword_based_arguments("Rose",23,"Flower");
#-------------------------------------------------------

#Function Definition :
def function_non_keyword_parameters(*members):
  print(members);
  for member in members:
    print(member);

#Function Call :
function_non_keyword_parameters("Happy",4,23,"Rose");


#-------------------------------------------------------
# 
#Description : Function with keyword based arguments
#
#Function definition :
# def function_with_non-keyword_based_arguments(**parameters):
#   statements
#
#Function Call :
# function_with_non-keyword_based_arguments(name="name",number=1,name2="name2");
#-------------------------------------------------------

#Function Definition :
def function_keyword_parameters2(**parameters):
  for key,value in parameters.items():
    print('{}:{}'.format(key,value));

#Function Call :
function_keyword_parameters2(number=7,name="Paul");

#Accessing elements using key
#Function Definition
def function_key_params(**parameters):
  print(parameters["name"]);

#Function Call:
function_key_params(name="Happy",number=333);
