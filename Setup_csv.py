# -------------------------------INITIALIZING CSV FILES FOR ITEM AND EMP-----------------------------#
import csv


def Add_Items():
    print("\t\tWELCOME TO ABC SUPERMARKET, PLEASE FINISH THE SETUP")
    f2 = open("Items.csv", 'w')
    fields = ['ICode', 'IName', 'Quantity', 'Cost']
    csv_w = csv.writer(f2, lineterminator="\n")
    csv_w.writerow(fields)
    f2.close()
    n = int(input("\t\t\t\tEnter no. of Items to be added:"))
    print()
    for times in range(n):
        print("\t\t\t\t\t", times + 1)
        INameIn = input("\t\t\t\tEnter Item Name:")
        ICodeIn = int(input("\t\t\t\tEnter Item Code(Code should be Unique):"))
        QtyIn = int(input("\t\t\t\tEnter Quantity of Item Available:"))
        Cost = int(input("\t\t\t\tEnter Cost of Item"))
        Lst = [ICodeIn, INameIn, QtyIn, Cost]
        flag = True
        f = open("Items.csv", 'r')
        csv_r = csv.reader(f)
        for record in csv_r:
            if record[0] == ICodeIn:
                flag = False
                print("\t\tSorry,The Item couldn't be Inserted!, Please Enter Valid and Unique ICode")
                f.close()
                break
            else:
                flag = True
        if flag == True:
            f1 = open("Items.csv", 'a+')
            csv_w = csv.writer(f1, lineterminator="\n")
            csv_w.writerow(Lst)
            print("\t\t\t\tItem Successfully Added!")
            f1.close()


def Add_Emp():
    print("\t\t\t\tCONGRATULATIONS,SHOP ITEMS FILE IS NOW READY\n\t\t\t\tPLEASE COMPLETE EMPLOYEE FILE")
    f2 = open("Emps.csv", 'w')
    fields = ['ECode', 'EName', 'Dept', 'Address', 'Phone', 'DOB', 'DOJ']
    csv_w = csv.writer(f2, lineterminator="\n")
    csv_w.writerow(fields)
    f2.close()
    n = int(input("\t\t\t\tEnter no. of Employees to be added:"))
    print()
    for times in range(n):
        print("\t\t\t\t\t", times + 1)
        ENameIn = input("\t\t\t\tEnter Emp Name:")
        ECodeIn = int(input("\t\t\t\tEnter Emp Code(Code should be Unique):"))
        Dept = input("\t\t\t\tEnter Emp Department:")
        Add = input("\t\t\t\tEnter Emp Address:")
        Phone = input("\t\t\t\tEnter Emp Phone:")
        DOB = input("\t\t\t\tEnter Emp DOB:")
        DOJ = input("\t\t\t\tEnter Emp DOJ:")
        Lst = [ECodeIn, ENameIn, Dept, Add, Phone, DOB, DOJ]
        flag = True
        f = open("Emps.csv", 'r')
        csv_r = csv.reader(f)
        for record in csv_r:
            if record[0] == ECodeIn:
                flag = False
                print("\t\tSorry,The Employee couldn't be Inserted!, Please Enter Valid and Unique ECode")
                f.close()
                break
            else:
                flag = True
        if flag == True:
            f1 = open("Emps.csv", 'a+')
            csv_w = csv.writer(f1, lineterminator="\n")
            csv_w.writerow(Lst)
            print("\t\t\t\tEmployee Details Successfully Added!")
            f1.close()
