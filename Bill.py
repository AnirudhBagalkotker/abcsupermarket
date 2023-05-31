from tkinter import *

import random

rowlst = []


def Store():
    global rowlst
    c = 0
    import csv
    with open("Items.csv") as f:
        csv_r = csv.reader(f)
        nonel = [0, '', 0, 0]
        while c <= 17:
            for record in csv_r:
                rowlst.append(record)
                c = c + 1
            if c == 17:
                break
            else:
                rowlst.append(nonel)
                c = c + 1


Store()
totalcost = 0


class Bill_App:
    global totalcost

    def __init__(self, root):
        global rowlst
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("SUPERMARKET BILL")

        # ====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()

        # For Generating Random Bill Numbers
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()

        # Setting Value to variable
        self.c_bill_no.set(str(x))
        self.a = IntVar()
        self.b = IntVar()
        self.c = IntVar()
        self.d = IntVar()
        self.e = IntVar()
        self.f = IntVar()
        self.g = IntVar()
        self.h = IntVar()
        self.i = IntVar()
        self.j = IntVar()
        self.k = IntVar()
        self.l = IntVar()
        self.m = IntVar()
        self.n = IntVar()
        self.o = IntVar()
        self.totalc = IntVar()
        self.tax = IntVar()

        # ===================================
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'

        # Title of App
        title = Label(self.root, text="CUSTOMER INVOICE", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                      font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        # ==========Customers Frame==========#
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # ===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # =================Customer Phone==============#
        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # ==================Items Frame=====================#
        F2 = LabelFrame(self.root, text='Items', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=0, y=180, width=920, height=380)

        # ===========Frame Content=================== #

        a_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[1][1])
        a_lbl.grid(row=0, column=0, padx=10, pady=20)
        a_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.a)
        a_en.grid(row=0, column=1, ipady=5, ipadx=5)

        b_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[2][1])
        b_lbl.grid(row=1, column=0, padx=10, pady=20)
        b_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.b)
        b_en.grid(row=1, column=1, ipady=5, ipadx=5)

        c_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[3][1])
        c_lbl.grid(row=2, column=0, padx=10, pady=20)
        c_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.c)
        c_en.grid(row=2, column=1, ipady=5, ipadx=5)

        d_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[4][1])
        d_lbl.grid(row=3, column=0, padx=10, pady=20)
        d_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.d)
        d_en.grid(row=3, column=1, ipady=5, ipadx=5)

        e_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[5][1])
        e_lbl.grid(row=4, column=0, padx=10, pady=20)
        e_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.e)
        e_en.grid(row=4, column=1, ipady=5, ipadx=5)

        f_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[6][1])
        f_lbl.grid(row=0, column=2, padx=10, pady=20)
        f_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.f)
        f_en.grid(row=0, column=3, ipady=5, ipadx=5)

        g_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[7][1])
        g_lbl.grid(row=1, column=2, padx=10, pady=20)
        g_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.h)
        g_en.grid(row=1, column=3, ipady=5, ipadx=5)

        h_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[8][1])
        h_lbl.grid(row=2, column=2, padx=10, pady=20)
        h_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.g)
        h_en.grid(row=2, column=3, ipady=5, ipadx=5)

        i_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[9][1])
        i_lbl.grid(row=3, column=2, padx=10, pady=20)
        i_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.i)
        i_en.grid(row=3, column=3, ipady=5, ipadx=5)

        j_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[10][1])
        j_lbl.grid(row=4, column=2, padx=10, pady=20)
        j_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.j)
        j_en.grid(row=4, column=3, ipady=5, ipadx=5)

        k_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[11][1])
        k_lbl.grid(row=0, column=4, padx=10, pady=20)
        k_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.k)
        k_en.grid(row=0, column=5, ipady=5, ipadx=5)

        l_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[12][1])
        l_lbl.grid(row=1, column=4, padx=10, pady=20)
        l_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.l)
        l_en.grid(row=1, column=5, ipady=5, ipadx=5)

        m_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[13][1])
        m_lbl.grid(row=2, column=4, padx=10, pady=20)
        m_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.m)
        m_en.grid(row=2, column=5, ipady=5, ipadx=5)

        n_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[14][1])
        n_lbl.grid(row=3, column=4, padx=10, pady=20)
        n_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.n)
        n_en.grid(row=3, column=5, ipady=5, ipadx=5)

        o_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=rowlst[15][1])
        o_lbl.grid(row=4, column=4, padx=10, pady=20)
        o_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.o)
        o_en.grid(row=4, column=5, ipady=5, ipadx=5)

        # ===================Bill Aera================#
        F3 = Label(self.root, bd=10, relief=GROOVE)
        F3.place(x=1125, y=180, width=400, height=380)

        bill_title = Label(F3, text="ABC SUPERMARKET", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Bill Menu Frame=============#
        F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=565, relwidth=1, height=235)

        total_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Bill")
        total_lbl.grid(row=1, column=0, padx=10, pady=20)
        total_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.totalc)
        total_en.grid(row=1, column=1, ipady=5, ipadx=5)

        tax_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Tax")
        tax_lbl.grid(row=2, column=0, padx=10, pady=20)
        tax_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax)
        tax_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ====================
        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.totalc)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)

        # ========================
        genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20)

        # ====================
        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=30)

        # ======================
        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20)

    # Function For Text Area

    def welcome_soft(self):
        import datetime as dt
        self.txt.delete('1.0', END)
        self.txt.insert(END, "          ABC SUPERMARKET\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, f"\nTime : {str(dt.datetime.now())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")

    # Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0', END)

    # Function to get total prices

    def total(self):
        global totalcost
        totalcost = int((self.a.get() * int(rowlst[1][3])) + (self.b.get() * int(rowlst[2][3])) + (self.c.get() * int(rowlst[3][3])) + (self.d.get() * int(rowlst[4][3])) + (self.e.get() * int(rowlst[5][3])) + (self.i.get() * int(rowlst[6][3])) + (self.h.get() * int(rowlst[7][3])) + (self.g.get() * int(rowlst[8][3])) + (self.f.get() * int(rowlst[9][3])) + (self.j.get() * int(rowlst[10][3]) + (self.k.get() * int(rowlst[11][3])) + (self.m.get() * int(rowlst[12][3])) + (self.l.get() * int(rowlst[13][3])) + (self.n.get() * int(rowlst[14][3])) + (self.o.get() * int(rowlst[15][3]))))
        tax = int(round(totalcost * 0.05))
        self.tax.set(int(tax))
        self.totalc.set(int(totalcost))
        totalcost = totalcost + tax

    # Add Product name , qty and price to bill area
    def bill_area(self):
        global rowlst
        global totalcost
        self.total()
        self.welcome_soft()
        if self.a.get() != 0:
            self.txt.insert(END, f"\n{rowlst[1][1]}          \t\t{self.a.get()}            {self.a.get() * int(rowlst[1][3])}")
        if self.b.get() != 0:
            self.txt.insert(END, f"\n{rowlst[2][1]}          \t\t{self.b.get()}            {self.b.get() * int(rowlst[2][3])}")
        if self.c.get() != 0:
            self.txt.insert(END, f"\n{rowlst[3][1]}          \t\t{self.c.get()}            {self.c.get() * int(rowlst[3][3])}")
        if self.d.get() != 0:
            self.txt.insert(END, f"\n{rowlst[4][1]}          \t\t{self.d.get()}            {self.d.get() * int(rowlst[4][3])}")
        if self.e.get() != 0:
            self.txt.insert(END, f"\n{rowlst[5][1]}          \t\t{self.e.get()}            {self.e.get() * int(rowlst[5][3])}")
        if self.i.get() != 0:
            self.txt.insert(END, f"\n{rowlst[6][1]}          \t\t{self.i.get()}            {self.i.get() * int(rowlst[6][3])}")
        if self.h.get() != 0:
            self.txt.insert(END, f"\n{rowlst[7][1]}          \t{self.h.get()}            {self.h.get() * int(rowlst[7][3])}")
        if self.g.get() != 0:
            self.txt.insert(END, f"\n{rowlst[8][1]}          \t\t{self.g.get()}            {self.g.get() * int(rowlst[8][3])}")
        if self.f.get() != 0:
            self.txt.insert(END, f"\n{rowlst[9][1]}          \t\t{self.f.get()}            {self.f.get() * int(rowlst[9][3])}")
        if self.j.get() != 0:
            self.txt.insert(END, f"\n{rowlst[10][1]}         \t\t{self.j.get()}            {self.j.get() * int(rowlst[10][3])}")
        if self.k.get() != 0:
            self.txt.insert(END, f"\n{rowlst[11][1]}         \t\t{self.k.get()}            {self.k.get() * int(rowlst[11][3])}")
        if self.m.get() != 0:
            self.txt.insert(END, f"\n{rowlst[12][1]}         \t\t{self.m.get()}            {self.m.get() * int(rowlst[12][3])}")
        if self.l.get() != 0:
            self.txt.insert(END, f"\n{rowlst[13][1]}         \t\t{self.l.get()}            {self.l.get() * int(rowlst[13][3])}")
        if self.n.get() != 0:
            self.txt.insert(END, f"\n{rowlst[14][1]}         \t\t{self.n.get()}            {self.n.get() * int(rowlst[14][3])}")
        if self.o.get() != 0:
            self.txt.insert(END, f"\n{rowlst[15][1]}         \t\t{self.o.get()}            {self.o.get() * int(rowlst[15][3])}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, f"\nTotal : {totalcost}")
        self.txt.insert(END, f"\nThank you for visiting")
        self.txt.insert(END, f"\n ")

    # Function to exit
    def exit(self):
        self.root.destroy()

    # Function To Clear All Fields


root = Tk()
root.resizable(True,True)
object = Bill_App(root)
root.mainloop()
