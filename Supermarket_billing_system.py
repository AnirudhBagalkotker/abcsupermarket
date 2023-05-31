import Setup_csv as II
import Items_csv as SI
import Emp_csv as EI

def setup():
    import os.path
    if os.path.exists('Items.csv') and os.path.exists('Emps.csv'):
        pass
    else:
        II.Add_Items()
        II.Add_Emp()


def login():
    import datetime as dt
    print("\t\t\t   Time   ", dt.datetime.now())
    count = 0
    while True:
        username = input("\t\t\tHELLO! WELCOME TO ABC SUPERMARKET! \n\n\t\t\t\tUsername: ")
        password = input("\t\t\t\tPassword: ")
        count += 1
        if count == 3:
            print("\t\t\t\tAll Your Attempts Failed, Sorry!")
            exit()
        else:
            if username.lower() == 'anirudh' and password.lower() == 'aryan':
                print("\n\t\t\tWELCOME TO ABC SUPERMARKET \n\t\t\t\t  Login Successful")
                break
            else:
                if password.lower() != 'aryan':
                    print("\t\t\t\tWrong Password!, Please Try Again")
                    continue
                else:
                    print("\t\t\t\tWrong Username and Password!,Try Again")
                    continue


def Emp_details():
    print("\t\t\t\t1.ADD NEW EMPLOYEE\t\t\t\t\t")
    print("\t\t\t\t2.UPDATE EMPLOYEE DETAILS\t\t\t\t\t")
    print("\t\t\t\t3.REMOVE EMPLOYEE\t\t\t\t\t")
    print("\t\t\t\t4.VIEW EMPLOYEE DETAILS\t\t\t\t\t")
    choiceE = int(input("\t\t\t\tEnter Your Choice :\n\t\t\t\t\t"))
    if choiceE == 1:
        EI.Add_New_Emp()
    elif choiceE == 2:
        EI.Update_Emp()
    elif choiceE == 3:
        EI.Remove_Emp()
    elif choiceE == 4:
        EI.View_Emps()


def Shop_Items():
    print("\t\t\t\t1.ADD NEW ITEM\t\t\t\t\t")
    print("\t\t\t\t2.UPDATE ITEM DETAILS\t\t\t\t\t")
    print("\t\t\t\t3.REMOVE ITEMS\t\t\t\t\t")
    print("\t\t\t\t4.VIEW ITEM DETAILS\t\t\t\t\t")
    choiceS = int(input("\t\t\t\tEnter Your Choice :\n\t\t\t\t\t"))
    if choiceS == 1:
        SI.Add_New_Item()
    elif choiceS == 2:
        SI.Update_Item()
    elif choiceS == 3:
        SI.Remove_Item()
    elif choiceS == 4:
        SI.View_Items()


def mainmenu():
    login()
    setup()
    while True:
        print("\t\t\t\tMAIN MENU\t\t\t\t\t")
        print()
        print("\t\t\t\t1.GENERATE NEW BILL\t\t\t\t\t")
        print("\t\t\t\t2.EMPLOYEE DETAILS\t\t\t\t\t")
        print("\t\t\t\t3.SHOP ITEMS\t\t\t\t\t")
        print("\t\t\t\t4.QUIT\t\t\t\t\t")
        choice1 = int(input("\t\t\t\tEnter Your Choice :\n\t\t\t\t\t"))
        if choice1 == 4:
            quit()
        elif choice1 == 2:
            Emp_details()
        elif choice1 == 3:
            Shop_Items()
        elif choice1 == 1:
            import Bill


if __name__ == "__main__":
    mainmenu()
