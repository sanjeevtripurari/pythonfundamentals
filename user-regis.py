## REGISTER
## Accept the Username
## Accept the Password. Minimum lenght of the Password = 8. 
## Password should be AlphaNumeric and it should have atleast one special character
## login process
## Verify Username and Password
## Accept the Username
## Accept the Password. Minimum lenght of the Password = 8. 
## Password should be AlphaNumeric and it should have atleast one special character
## If Username and Password both are validated then VERIFY with the Registration details


#program to read file having name value pair for user and password

user_info = 'user_info.txt'
users={}
with open(user_info, 'r+') as ui:
  for line in ui:
    f_user_name, f_password = line.strip().split(',')
    users[f_user_name] = f_password


user_name=input("Enter username: ")

# Check if user exists
if user_name in users.keys():
  user_pass=input("Enter password: ")

  if users[user_name]==user_pass:
    print("Login Successful")
  else:
    print("Login Failed")
else:
  print("User does not exist")
  print("Register user")
  user_name=input("Enter username: ")
  user_pass=input("Enter password: ")

  special_char=False
  length=False

  while True:
    for i in range(len(user_pass)):
      if not user_pass[i].isalnum():
        special_char=True
        break
      
    if i==len(user_pass)-1 and not special_char:
      special_char=False
    if len(user_pass)>=8:
      length=True
    else:
      length=False
      
    if not (special_char and length):
      print("password should be alpanumeric with 1 special character and of length atleast 8 ")  
      user_pass=input("Enter password: ")
    else:
      break   
    
  if special_char and length:
    users[user_name]=user_pass
    with open(user_info, 'a') as ui:
      ui.write(f"{user_name},{user_pass}\n")
    print("Registration Successful")




