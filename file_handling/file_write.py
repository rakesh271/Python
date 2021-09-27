#--------------------------------------------------------------------
#Description : Writing into the file 
#Used Function : write()
#Mode : 'w'
#--------------------------------------------------------------------

with open('file.py','w') as f:
  print("write(Data you want to write)");
  f.write("Hey this the write function");

#--------------------------------------------------------------------
#Description : Adding data into the file
#Used Function : write()
#Mode : 'a'
#--------------------------------------------------------------------

with open('file.py','a') as f:
  print("write(Data you want to append it at the end)");
  f.write("--Adding this line --");

