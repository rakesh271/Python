#--------------------------------------------------------------------
#Description : File Reading
#Used Function : read()
#--------------------------------------------------------------------

with open('file.py','r') as f:
  print("read(Mention the character length) :");
  print(f.read());

#--------------------------------------------------------------------
#Description : File Reading
#Used Function : readline()
#--------------------------------------------------------------------

with open('file.py','r') as f:
  print("readline(Mention the character length) :");
  print(f.readline());


#--------------------------------------------------------------------
#Description : File Reading
#Used Function : readlines()
#--------------------------------------------------------------------



with open('file.py','r') as f:
  print("readlines(Mention the character length) :");
  print(f.readlines());

#--------------------------------------------------------------------
#Description : Differnce between read() and readlines()
#read()      : read returns all the lines in the file line by line. 
#readlines() : returns as list of stings. Each string is each line.
#--------------------------------------------------------------------


#--------------------------------------------------------------------
#Description : File Reading
#Used Function : read()
#Iterates through every line and prints it
#This way is more effective
#--------------------------------------------------------------------

with open('file.py','r') as f:
  print("Using For loop to iterate");
  for line in f:
    print(line, end="");

