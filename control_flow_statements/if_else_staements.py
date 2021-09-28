#-------------------------------------------------------------------------------------
#Description : If -Else statements
#Syntax      : 
#   if(conition):
#     statements;
#   else:
#     statements;
#About      : if-else statements
#-------------------------------------------------------------------------------------
rcb_score = 187
csk_score = 153

print("-------------If-Else Statement----------------");
if(csk_score != rcb_score):
  print("Mistmatch");
else:
  print("Match");

#-------------------------------------------------------------------------------------
#Description : If -Else statements
#Syntax      : 
#   if(conition):
#     statements;
#   else:
#     if(condition):
#       statements;
#     else:
#       statements;
#About      : Nested if-else statements
#-------------------------------------------------------------------------------------

print("-------------Nested-If-Else Statement----------------");
if(rcb_score == csk_score):
  print("Match Tied");
else:
  if(rcb_score > csk_score):
    print("RCB Won the match");
  else:
    print("CSK won the match");

#-------------------------------------------------------------------------------------
#Description : If -Else statements
#Syntax      : 
#   if(conition):
#     statements;
#   elif(condition):
#     statements;
#   else:
#     statements;
#About      : if-elif-else statements
#-------------------------------------------------------------------------------------

print("-------------If-elif-Else Statement----------------");
if(rcb_score >= 150):
  print("Good Score by RCB");
elif(csk_score >= 150):
  print("Good score by CSK");
else:
  print("Bad score");


