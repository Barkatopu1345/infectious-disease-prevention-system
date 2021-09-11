from face_recognization import *
from mask import *
from arduino_main import *


print("Enter 1 for attendence system")

print("Enter 2 for face mask system")




def menu():
    decission = int(input("Enter your decission: "))
    if decission == 1:
        main_face()

    elif decission == 2:
        maskMain()
    elif decission == 3:
        handCommand()
    elif decission == 4:
    
        voiceCommand()
    x = input("Do you want to close? y/n: ")
    if x != "y":
        menu()
    else: return


menu()
