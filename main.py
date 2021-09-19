from face_recognization import *
from mask import *
from arduino_main import *





def menu():
    decission = int(input("Enter your decission: "))
    if decission == 1:
        maskMain()
        

    elif decission == 2:
        main_face()
    elif decission == 3:
        handCommand()
    elif decission == 4:
        voiceCommand()
    x = input("Do you want to close? y/n: ")
    if x != "y" and x != "Y":
        menu()
    else: return


menu()
