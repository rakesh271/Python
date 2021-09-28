#-------------------------------------------------------
#Description : for loop
#syntax      : 
#     for item in items:
#       statements;
#About       : Iterates over single character of a string
#-------------------------------------------------------

player = 'Kohli';
print("------------Iterating over a String----------------");
for i in player:
  print(i);

#-------------------------------------------------------
#Description : for loop
#syntax      : 
#     for item in items:
#       statements;
#About       : iterates over a list
#-------------------------------------------------------

teams = ['RCB','MI','KXIP','RR','CSK'];
print("--------------Iterating over a list----------------");
for team in teams:
  print(team);

#-------------------------------------------------------
#Description : for loop
#syntax      : 
#     for key,value in parameters.items():
#       statements;
#About       : Iterates over a associative array
#-------------------------------------------------------

players = {'RCB':'Virat Kohli','CSK':'MSD','Rahul':'Punjab'}; 
print("----------Iterating over a associate array---------------");
for team,player in players.items():
  print(team,"->",player);
