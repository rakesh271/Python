#-----------------------------------------------------------------------
#Description : Opening a file and searching for a pattern in read mode
#Function Used : search()
#-----------------------------------------------------------------------
import re

print("----------------Using Search()---------------");
with open("file.py",'r') as f:
  for line in f:
    match = re.search('(Writing) (into)',line);
    if(match):
      print(match.groups());
      break;
  else:
    print("Match Not Found");

#-----------------------------------------------------------------------
#Description : Opening a file and searching for a pattern in read mode
#Function Used : split()
#-----------------------------------------------------------------------
print("-------------Using split()-------------------");
with open("file.py",'r') as f:
  for line in f:
    match = re.split('li',line);
    print(match);


#-----------------------------------------------------------------------
#Description : Opening a file and searching for a pattern in read mode
#Function Used : sub()
#-----------------------------------------------------------------------
print("------------Using sub()----------------------");
with open("file.py",'r') as f:
  for line in f:
    match = re.sub('line','number',line);
    print(match);

#-----------------------------------------------------------------------
#Description : Opening a file and searching for a pattern in read mode
#Function Used : findall()
#-----------------------------------------------------------------------
print("-----------------Using findall()----------------");
with open("file.py",'r') as f:
  for line in f:
    match = re.findall('line',line);
    print(match);
