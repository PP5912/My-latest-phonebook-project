"""CW Database for Module_Test_1"""
import MainProgramFileForGitHub
from time import sleep

print("Please enter the number after the word [contact] below:")
sleep(0.5)
personOneName = input("Contact: ")
convertPersonOneName = (personOneName.upper())

if convertPersonOneName == "1":
    print("The person that you're looking for: ", MainProgramFileForGitHub.contactOneName)
    print("His/Her phone number is: ", MainProgramFileForGitHub.contactOnePhoneNum)
    print("His/Her home address is: ", MainProgramFileForGitHub.contactOneAddress)
    sleep(0.5)
    print("Have a great day!")
elif convertPersonOneName == "2":
    print("The person that you're looking for: ", MainProgramFileForGitHub.contactTwoName)
    print("His/Her phone number is: ", MainProgramFileForGitHub.contactTwoPhoneNum)
    print("His/Her home address is: ", MainProgramFileForGitHub.contactTwoAddress)
    sleep(0.5)
    print("Have a great day!")
elif convertPersonOneName == "3":
    print("The person that you're looking for: ", MainProgramFileForGitHub.contactThreeName)
    print("His/Her phone number is: ", MainProgramFileForGitHub.contactThreePhoneNum)
    print("His/Her home address is: ", MainProgramFileForGitHub.contactThreeAddress)
    sleep(0.5)
    print("Have a great day!")
elif convertPersonOneName == "4":
    print("The person that you're looking for: ", MainProgramFileForGitHub.contactFourName)
    print("His/Her phone number is: ", MainProgramFileForGitHub.contactFourPhoneNum)
    print("His/Her home address is: ", MainProgramFileForGitHub.contactFourAddress)
    sleep(0.5)
    print("Have a great day!")
elif convertPersonOneName == "5":
    print("The person that you're looking for: ", MainProgramFileForGitHub.contactFiveName)
    print("His/Her phone number is: ", MainProgramFileForGitHub.contactFivePhoneNum)
    print("His/Her home address is: ", MainProgramFileForGitHub.contactFiveAddress)
    sleep(0.5)
    print("Have a great day!")
else:
    print("We couldn't find the contact that you were looking for.")


