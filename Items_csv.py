# SHOP ITEMS
import csv


def Add_New_Item():  # only Single Item , not for multiple Items, Use Startup for 1st Time
    INameIn = input("\t\t\t\tEnter Item Name:")
    ICodeIn = int(input("\t\t\t\tEnter Item Code(Code should be Unique):"))
    QtyIn = int(input("\t\t\t\tEnter Quantity of Item Available:"))
    Cost=int(input("\t\t\t\tEnter Cost of Item:"))
    Lst = [ICodeIn, INameIn, QtyIn,Cost]
    flag = True
    f = open("Items.csv", 'r')
    csv_r = csv.reader(f)
    for record in csv_r:
        if record[0] == ICodeIn:
            flag = False
            print("\t\tSorry,The Item couldnt be Inserted!, Please Enter Valid and Unique ICode")
            f.close()
            break
        else:
            flag = True
    if flag == True:
        f1 = open("Items.csv", 'a+')
        csv_w = csv.writer(f1, lineterminator='\n')
        csv_w.writerow(Lst)
        print("\t\t\t\tItem Successfully Added!")


def Update_Item():  # Changing Quantity Manually
    ICode = int(input("\t\t\t\tEnter the ICode of Record:"))
    with open("Items.csv") as f:
        flag = False
        csv_r = csv.reader(f)
        rows = []
        for record in csv_r:
            if record[0] == ICode:
                Urecord = record
                flag = True
                print("\t\t\t\tThe Record Which should be Updated:\n\t\t\t\t", Urecord)
                New_Qty = int(input("\t\t\t\tEnter the New Quantity:"))
                Urecord[2] = New_Qty
                rows.append(Urecord)
                break
            else:
                rows.append(record)

    if flag == False:
        print("\t\t\t\tRecord not Found")
    elif flag == True:
        with open("Items.csv", 'w') as f1:
            fields = ['ICode', 'IName', 'Quantity','Cost']
            csv_w = csv.writer(f1, lineterminator='\n')
            csv_w.writerow(fields)
            csv_w.writerows(rows)
        print("\t\t\t\tItem Quantity Successfully Updated\n\t\t\t\tUpdated Record:", Urecord)


def Remove_Item():
    with open("Items.csv") as f:
        csv_r = csv.reader(f)
        rows = []
        for record in csv_r:
            rows.append(record)

    ICode = input("\t\t\t\tEnter ICode whose Item is to be deleted")
    fields = ['ICode', 'IName', 'Quantity','Cost']
    with open("Items.csv", 'w') as f1:
        csv_w = csv.writer(f1, lineterminator='\n')
        csv_w.writerow(fields)
        for i in range(1, len(rows)):
            if rows[i][0] == ICode:
                pass
            else:
                csv_w.writerow(rows[i])
        print("\t\t\t\t Item Successfully Deleted and Removed")


def View_Items():
    import pandas
    df = pandas.read_csv('Items.csv')
    print("\t\t\t\tShop Items Details")
    print("\t\t\t",df)


def Store(rowlst):
    c = 0
    with open("Items.csv") as f:
        csv_r = csv.reader(f)
        rows = []
        nonel=[0,'',0,0]
        while c <= 17:
            for record in csv_r:
                rows.append(record)
                c = c+1
                print(c,rows)
            if c == 17:
                break
            else:
                rows.append(nonel)
                c = c+1
        rowlst = rows
        return rowlst
