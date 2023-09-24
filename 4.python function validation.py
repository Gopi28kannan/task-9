import re
def eid(data):
          pattern = "([a-z0-9_.])+\@+([a-z0-9])+(\.)+([a-z]{2,6})"
          if re.match(pattern, data):
                    return "valid email id"
          else:
                    return "invalid email id"

def bang_mob_no(data):
          pattern = "01[^1-4]\d{8}"
          if re.match(pattern, data):
                    return "valid mobile number in bangladesh"
          else:
                    return "invalid mobile number in bangladesh"

def usa_tele_no(data):
          pattern = "\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]"
          if re.match(pattern, data):

                    return "valid USA telephone number"
          else:
                    return "invalid USA telephone number"
def password(data):
          pattern = r"^.*[A-Za-z]+.*\d+.*$|^.*\d+.*[A-Za-z]+.*$"
          if re.match(pattern, data):
                    return "valid password"
          else:
                    return "invalid password"


i=1
while i<=4:
          print("""          press 1. check email address
          press 2.check mobile number of bangladesh
          press 3.check telephone numbers of USA
          press 4. check 16 character alpha-numeric password""")
          n=int(input("choice option = "))
          
          if n==1:
                    print(eid(input("enter email : ")))
                    input()
                    
          elif n==2:
                    print(bang_mob_no(input("enter phone no : ")))
                    input()
          elif n==3:
                    print(usa_tele_no(input("enter tele phone no : ")))
                    input()
          elif n==4:
                    print(password(input("enter password : ")))
                    input()
          else:
                    i=n
                    print("its exit")
