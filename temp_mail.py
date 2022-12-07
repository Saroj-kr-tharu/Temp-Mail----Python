from msvcrt import getch
from os import system
from mailtm import Email

class TempMail:
    
    def __init__(self):
        self.test = Email()
        print("\nDomain: " + self.test.domain)
    
    def listener(message):
        print("\nSubject: " + message['subject'])
        print("Content: " + message['text'] if message['text'] else message['html'])
    
    def QuickSetup(self):
        system("cls")
        # Make new email address
        self.test.register()
        print("\n\t\t Email Adress----> " + str(self.test.address))
        # Start listening
        self.test.start(TempMail.listener)
        print("\t\t\t Waiting for new emails...")
        
    def CustumSetup(self):
        system("cls")
        emailAddress=input("\n\t\t Enter Your Custum Email address ----> ")
        # Make new email address
        self.test.register(username=emailAddress)
        print("\n\t\t Email Adress----> " + str(self.test.address))
        # Start listening
        self.test.start(TempMail.listener)
        print("\t\t\t Waiting for new emails...")

    def AboutUs(self):
        ''' About Developer  '''
        system("cls")
        art="\n\t\t Tʜɪs Pʀᴏɢʀᴀᴍ ɪs Dᴇsɪɢɴᴇᴅ Bʏ  Sᴀʀᴏᴊ Kʀ. Tʜᴀʀᴜ."
        print("\n\t\t <--- Welcome to About us Section -----> ")
        print(art)
        getch()

    def ExitProgram(self):
        print("\n\t\t <---- Thanks for your our program -----> ")
        print("\t\t Exiting .... ")
        exit()

    def menu(self):
        # while(True):
            system("cls")
            print("\n\t\t <----- Welcome to Main Menu -----> ")
            print("\t\t\t 1 . Quick Temp Mail ")
            print("\t\t\t 2 . Custum Temp Mail ")
            print("\t\t\t 10. About Us ")
            print("\t\t\t 99. Exit ")

            choice=int(input("\t\t Enter Your Choice :-) "))

            if choice ==1:
                self.QuickSetup()
            elif choice ==2:
                self.CustumSetup()
            elif choice ==10:
                self.AboutUs()
            elif choice ==99:
                self.ExitProgram()
            else:
                print("\n\t\t <---- Invalid options ----> ")
                getch()

def main():
    mail=TempMail()
    mail.menu()

if __name__ == "__main__":
    main()


