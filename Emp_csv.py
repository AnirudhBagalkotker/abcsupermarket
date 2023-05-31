import csv


def Add_New_Emp():  # only Single Emp , not for multiple Emps, Use Startup for 1st Time
    ENameIn = input("\t\t\t\tEnter Emp Name:")
    ECodeIn = int(input("\t\t\t\tEnter Emp Code(Code should be Unique):"))
    Dept = input("\t\t\t\tEnter Emp Deptartment:")
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
            print("\t\tSorry,The Emp couldnt be Inserted!, Please Enter Valid and Unique ECode")
            f.close()
            break
        else:
            flag = True
    if flag == True:
        f1 = open("Emps.csv", 'a')
        csv_w = csv.writer(f1, lineterminator='\n')
        csv_w.writerow(Lst)
        print("Emp Successfully Added!")


def Update_Emp():  # Changing Manually
    ECode = int(input("\t\t\t\tEnter the ECode of Record:"))
    c = input('\t\t\t\tWhich Colounm is to be Updated? Dept, Add or Phone?:')
    i = None
    if c.lower() == 'dept':
        i = 2
    elif c.lower() == 'add':
        i = 3
    elif c.lower() == 'phone':
        i = 4
    else:
        print("\t\t\t\t\tInvalid Entry")

    with open("Emps.csv") as f:
        flag = False
        csv_r = csv.reader(f)
        rows = []
        for record in csv_r:
            if record[0] == ECode:
                Urecord = record
                flag = True
                print("\t\t\t\tThe Record Which should be Updated:\n\t\t\t\t", Urecord)
                New_Qty = int(input("\t\t\t\tEnter the Details:"))
                Urecord[i] = New_Qty
                rows.append(Urecord)
                break
            else:
                rows.append(record)

    if flag == False:
        print("\t\t\t\tRecord not Found")
    elif flag == True:
        with open("Emps.csv", 'a') as f1:
            csv_w = csv.writer(f1, lineterminator='\n')
            csv_w.writerows(rows)
        print("\t\t\t\tEmp Quantity Successfully Updated\n\t\t\t\tUpdated Record:", Urecord)


def Remove_Emp():
    with open("Emps.csv") as f:
        csv_r = csv.reader(f)
        rows = []
        for record in csv_r:
            rows.append(record)

    ECode = input("\t\t\t\tEnter ECode whose Emp is to be deleted")
    fields = ['ECode', 'EName', 'Dept', 'Address', 'Phone', 'DOB', 'DOJ']
    with open("Emps.csv", 'w') as f1:
        csv_w = csv.writer(f1, lineterminator='\n')
        csv_w.writerow(fields)
        for i in range(1, len(rows)):
            if rows[i][0] == ECode:
                pass
            else:
                csv_w.writerow(rows[i])
        print("\t\t\t\t Emp Successfully Deleted and Removed")


def View_Emps():
    import pandas
    df = pandas.read_csv('Emps.csv')
    print("\t\t\t\tEmployee Details")
    print("\t\t\t",df)
