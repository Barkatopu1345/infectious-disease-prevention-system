from face_recognization import *
from mask import *
from arduino_main import *


print("Enter 1 for attendence system")

print("Enter 2 for face mask system")

decission = input("Enter your decission: ")

main_face()
maskMain()
handCommand()
voiceCommand()