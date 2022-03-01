#Ascii art creator
import pyfiglet
import sys,time,os
from tqdm import tqdm
ascii_banner = pyfiglet.figlet_format("WFISD")
print(ascii_banner)
#Ascii art creator end
message = "Welcome to the West Frenchgat ISD virtual managment system (VMS); please enter your password the administrators gave to you in the fields below"

def Terminal():
  message = "Error! ALL main power generators OFFLINE; Most features disabled "  
  letters = 0
  letters2 = 0
  for char in message:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.1)
  print("                                      ")
  message2 = "Please select an option: 1) Reboot power 2) Reboot Vents. 3) View CCTVs 4) Turn on alarms"
  for char in message2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
    letters2 = letters2 + 1
  print("                           ")  
  terminal = int(input("Enter your choice: "))
  if terminal == int(1):
    for i in tqdm(range(20)):
      time.sleep(0.5)

    
def ScriptedPassword():
  password = int(input("Password: "))
  message = "Password ACCEPTED"
  message2 = "Password DENIED"
  if password == 1111:
    for char in message:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.1)
    print("                           ")  
    Terminal()
  else:
    for char in message2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
      
for char in message:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.1)
print("                                          ")
print("                                          ")

Username = str(input("Username: "))
if Username == "C.Jefferson":
  print("Welcome Cave Jefferson")
  print("Please provide your password ")
  ScriptedPassword()
  
elif Username == "Jeremy.Dell.Conoger":
  print("Error, student username detected, please go back to you're class please")
else:
  print("Invalid username")

