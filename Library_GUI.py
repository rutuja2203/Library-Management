from tkinter import *
from tkinter import ttk
import datetime as dt

base=Tk()
fr1=LabelFrame(base,padx=10)
fr1.grid(row=0,column=0)

temp=Toplevel(base)

class BookInfo:
    def accept_book_info(self):
        self.bk_num =str(e2.get())
        self.bk_title =str(e1.get())
        self.bk_author =str(e3.get())
        self.bk_publication =str(e4.get())

    def write_bk_data_into_file(self):
        fobj = open("book_info.txt","a")
        fobj.write(self.bk_num + "," + self.bk_title + "," + self.bk_author + "," + self.bk_publication + "\n")
        fobj.close()

class StudentInfo:
    def accept_stud_info(self):
        self.st_enr = str(e2.get())
        self.st_name = str(e1.get())
        self.st_email = str(e4.get())
        self.st_contact = str(e3.get())
        self.st_class = str(e5.get())

    def write_st_data_into_file(self):
        fobj = open("stud_info.txt", "a")
        fobj.write(self.st_enr + "," + self.st_name + "," + self.st_email + "," + self.st_contact + "," + self.st_class + "\n")
        fobj.close()

def add_new_book():
    b = BookInfo()
    b.accept_book_info()
    b.write_bk_data_into_file()
    l6.configure(text="ADDED SUCCSESSFULLY!!!!")

def add_new_student():
    s = StudentInfo()
    s.accept_stud_info()
    s.write_st_data_into_file()
    l6.configure(text="Added Successfully!!!")

class IssueBook:
    def issue_book_to_student(self):
        self.book_num = str(entry2.get())
        self.stud_enr = str(entry1.get())
        self.idate = str(dt.date.today())
        self.rdate = "NOT"
        self.ret_status = "NO"
        self.exp_rdate = str(dt.date.today() + dt.timedelta(7))

    def write_issue_data_into_file(self):
        fobj = open("issued_books.txt", "a")
        fobj.write(self.book_num + "," + self.stud_enr + "," + self.idate + "," + self.rdate + "," + self.ret_status + "," + self.exp_rdate)
        fobj.close()
        print("Warning..!! This Book must be returned ON or BEFORE :", self.exp_rdate)

def issue_book():
    i = IssueBook()
    i.issue_book_to_student()
    i.write_issue_data_into_file()
    label1.configure(text="ISSUED!!!!")

def new_issue_reset():
    entry1.delete(0,END)
    entry2.delete(0,END)

def return_book():
    ret_bnum = str(ent2.get())
    fobj = open("issued_books.txt","r")
    fdata_ls = fobj.readlines()
    fobj.close()

    fobj = open("issued_books.txt","w")
    for oneline in fdata_ls:
        if oneline.startswith(ret_bnum + ",") and oneline.__contains__(",NO,"):
            rdate = str(dt.date.today())
            new_oneline = oneline.replace(",NOT," , "," + rdate + ",")
            new_oneline2 = new_oneline.replace(",NO," , ",YES,")
            fobj.write(new_oneline2)
        else:
            fobj.write(oneline)
    fobj.close()
    lab.configure(text="RETURNED!!!!")

def new_return_reset():
    e2.delete(0,END)

def search_book_by_book_number():
    book_num=str(entr1.get())
    fobj=open("book_info.txt","r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_num):
            print(oneline)
        else:
            label3.configure(text="INVALID INPUT")


def search_book_by_book_title():
    book_title= str(entr1.get())
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_title):
            print(oneline)
        else:
            label3.configure(text="INVALID INPUT")

def search_book_by_book_author():
    book_author = str(entr1.get())
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_author):
            print(oneline)
        else:
            label3.configure(text="INVALID INPUT")


def search_book_by_book_publication():
    book_publication = str(entr1.get())
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_publication):
            print(oneline)
        else:
            label3.configure(text="INVALID INPUT!")


def search_book():
    if rbval.get()==0:
        search_book_by_book_number()
    elif rbval.get()==1:
        search_book_by_book_title()
    elif rbval.get()==2:
        search_book_by_book_number()
    elif rbval.get()==3:
        search_book_by_book_publication()

def search_stud_by_roll():
    stud_roll = str(entr2.get())
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_roll):
            print(oneline)
        else:
            label10.configure(text="INVALID INPUT")

def search_stud_by_name():
    stud_name = str(entr2.get())
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_name):
            print(oneline)
        else:
            label10.configure(text="INVALID INPUT")
def search_stud_by_email():
    stud_email = str(entr2.get())
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_email):
            print(oneline)
        else:
            label10.configure(text="INVALID INPUT")

def search_stud_by_cellno():
    stud_cellno = str(entr2.get())
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_cellno):
            print(oneline)
        else:
            label10.configure(text="INVALID INPUT")
def search_stud_by_class():
    stud_class = str(entr2.get())
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_class):
            print(oneline)
        else:
            label10.configure(text="INVALID INPUT")

def  search_student():
    if rbval2.get()==0:
        search_stud_by_name()
    elif rbval2.get()==1:
        search_stud_by_roll()
    elif rbval2.get()==3:
        search_stud_by_email()
    elif rbval2.get()==4:
        search_stud_by_cellno()
    elif rbval2.get()==2:
        search_stud_by_class()

def check_book_history():
    # i will open issued_book.txt file and print all the lines containing book number as provided in input
    count = 0
    b_num = str(en.get())

    #displaying this book's info to verify

    fobj = open("book_info.txt","r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0]==b_num:
            print("Book Title :", ls[1])
            print("Book Author :",ls[2])
            print("Book Publication :", ls[3])
            break
    fobj.close()

    #displaying book's history
    fobj = open("issued_books.txt","r")
    fdata_ls = fobj.readlines()
    print("Stud_Enr\t\tIssued_Date\t\tReturned_Date")
    print("-"*45)
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0] == b_num:
            print(ls[1] + "\t\t" + ls[2] + "\t\t" + ls[3], end="")
            count = count + 1
    print("\n\nThis Book was issued",count,"time(s)")

def check_student_history():
    count = 0

    fobj = open("stud_info.txt","r")
    fdata_ls = fobj.readlines()
    s_enr=str(entry.get())
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0]==s_enr:
            print("Student Name :", ls[1])
            print("Student Email Address :",ls[2])
            print("Student Contact Number :", ls[3])
            print("Student Class :", ls[4])
            break
    fobj.close()

    # displaying student's history
    fobj = open("issued_books.txt", "r")
    fdata_ls = fobj.readlines()
    print("Book_Num\t\tIssued_Date\t\tReturned_Date")
    print("-" * 45)
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[1] == s_enr:
            print(ls[0] + "\t\t" + ls[2] + "\t\t" + ls[3])
            count = count + 1
    print("\n\nThis Student borrowed", count, "book(s)")

def not_returned_books():
    # i will open issued_book.txt file and print all the books having return status NO and returned date NOT
    fobj = open("issued_books.txt","r")
    fdata_ls = fobj.readlines()
    print("Bk_Number\t\tSt_Enr\t\tIssue-Date\t\tExpected Return-Date")
    print("-"*70)
    for oneline in fdata_ls:
        if oneline.__contains__(",NOT,") and oneline.__contains__(",NO,"):
            # this is the book which is not returned
            ls = oneline.split(",")
            print(ls[0] + "\t\t" + ls[1] + "\t\t" + ls[2] + "\t\t" + ls[5], end="")
    fobj.close()

def show_frame_5(del_win):
    new05=Toplevel(base,height=300,width=300)
    new05.title("Not returned books!")
    bt=Button(new05,text="view not returned books",command=not_returned_books)
    bt.place(x=100,y=100)

def show_frame_4(del_win):
    new04=Toplevel(base,height=300,width=400)
    new04.title("Search book")

    global rbval,entr1,label3
    rbval=IntVar()
    r1=Radiobutton(new04,text="Search By Book Number",variable=rbval,value=0)
    r1.place(x=20,y=20)
    r2=Radiobutton(new04,text="Search By Book Title",variable=rbval,value=1)
    r2.place(x=150,y=20)
    r3=Radiobutton(new04,text="Search by Book Author",variable=rbval,value=2)
    r3.place(x=20,y=50)
    r4=Radiobutton(new04,text="Search by book publication",variable=rbval,value=3)
    r4.place(x=150,y=50)

    l1=Label(new04,text="Enter value here")
    l1.place(x=60,y=80)
    entr1=Entry(new04,width="15")
    entr1.place(x=150,y=80)
    bt1=Button(new04,text="Search",command=search_book)
    bt1.place(x=250,y=80)
    label3=Label(new04,text="")
    label3.place(x=150,y=120)

def show_frame_6(del_win):
    new06=Toplevel(base,height=400,width=400)
    new06.title("Search Student")

    global rbval2,label10,entr2
    rbval2=IntVar()
    rb1=Radiobutton(new06,text="Search By Name",variable=rbval2,value=0)
    rb1.place(x=10,y=10)
    rb2=Radiobutton(new06,text="Search by Roll no.",variable=rbval2,value=1)
    rb2.place(x=150,y=10)
    rb3=Radiobutton(new06,text="Search by class",variable=rbval2,value=2)
    rb3.place(x=10,y=40)
    rb4=Radiobutton(new06,text="Search by Email",variable=rbval2,value=3)
    rb4.place(x=150,y=40)
    rb5=Radiobutton(new06,text="Search by cell no.",variable=rbval2,value=4)
    rb5.place(x=10,y=70)

    lbl1=Label(new06,text="Enter value here")
    lbl1.place(x=60,y=100)
    entr2=Entry(new06,width="15")
    entr2.place(x=150,y=100)
    bttn1=Button(new06,text="Search",command=search_student)
    bttn1.place(x=250,y=100)
    label10=Label(new06,text="")
    label10.place(x=150,y=140)

def show_frame_3(del_win):
    new03=Toplevel(base,height=200,width=400)
    new03.title("Return books")

    global ent2,lab
    l2=Label(new03,text="Enter book number")
    l2.place(x=40,y=30)
    ent2=Entry(new03,width="10")
    ent2.place(x=180,y=30)
    bt2=Button(new03,text="Return",command=return_book)
    bt2.place(x=40,y=80)
    bt3=Button(new03,text="Reset",command=new_return_reset)
    bt3.place(x=130,y=80)
    lab=Label(new03,text="")
    lab.place(x=100,y=140)

def show_frame_2(del_win):
    new02=Toplevel(base,height=300,width=450)
    new02.title("ISSUE BOOK")
    lab1 = Label(new02, text="Enter Student Enrollment Number")
    lab1.place(x=10, y=30)
    lab2 = Label(new02, text="Enter Book Number")
    lab2.place(x=80, y=60)

    global entry1,entry2,label1
    entry1 = Entry(new02, width="20")
    entry1.place(x=200, y=30)
    entry2 = Entry(new02, width="20")
    entry2.place(x=200, y=60)

    btn1 = Button(new02, text="Issue Book", command=issue_book)
    btn1.place(x=80, y=90)
    btn2 = Button(new02, text="Reset",command=new_issue_reset)
    btn2.place(x=200, y=90)

    label1=Label(new02,text="")
    label1.place(x=100,y=130)



def show_frame_7(del_win):
    new07=Toplevel(base,height=300,width=300)
    new07.title("STUDENT HISTORY")


    lb1=Label(new07,text="click here to check student history")
    lb1.place(x=30,y=110)
    lb2=Label(new07,text="Enter student enrollment no.")
    lb2.place(x=30,y=70)
    global entry
    entry=Entry(new07,width=10)
    entry.place(x=30,y=90)
    bt1=Button(new07,text="show",command=check_student_history)
    bt1.place(x=30,y=140)

def show_frame_8(del_win):
    new08=Toplevel(base,height=300,width=300)
    new08.title("BOOK HISTORY")

    bt1 = Button(new08, text="show", command=check_book_history)
    bt1.place(x=30, y=140)
    lb1 = Label(new08, text="click here to check book history")
    lb1.place(x=30, y=110)
    lb2 = Label(new08, text="Enter Book number")
    lb2.place(x=30, y=70)
    global en
    en = Entry(new08, width=10)
    en.place(x=30, y=90)

def show_frame_9(del_win):
    new09=Toplevel(base,height=400,width=400)
    new09.title("ADD NEW STUDENT")

    global e1,e2,e3,e4,e5,l6
    l1=Label(new09,text="Enter name of student")
    l1.place(x=10,y=10)
    e1=Entry(new09,width=15)
    e1.place(x=160,y=10)
    l2=Label(new09,text="Enter roll number")
    l2.place(x=10,y=40)
    e2=Entry(new09,width=10)
    e2.place(x=160,y=40)
    l3=Label(new09,text="Enter contact number")
    l3.place(x=10,y=70)
    e3=Entry(new09,width=15)
    e3.place(x=160,y=70)
    l4=Label(new09,text="Enter the email")
    l4.place(x=10,y=110)
    e4=Entry(new09,width=15)
    e4.place(x=160,y=110)
    l5=Label(new09,text="Enter the class")
    l5.place(x=10,y=140)
    e5=Entry(new09,width=10)
    e5.place(x=160,y=140)
    bt=Button(new09,text="ADD",command=add_new_student)
    bt.place(x=150,y=170)
    l6=Label(new09,text="")
    l6.place(x=150,y=200)


def show_frame_10(del_win):
    new10 = Toplevel(base, height=400, width=400)
    new10.title("ADD NEW BOOK")

    global e1,e2,e3,e4,e5,l6
    l1 = Label(new10, text="Enter name of Book")
    l1.place(x=10, y=10)
    e1 = Entry(new10, width=15)
    e1.place(x=160, y=10)
    l2 = Label(new10, text="Enter Book number")
    l2.place(x=10, y=40)
    e2 = Entry(new10, width=10)
    e2.place(x=160, y=40)
    l3 = Label(new10, text="Enter book's author name")
    l3.place(x=10, y=70)
    e3 = Entry(new10, width=15)
    e3.place(x=160, y=70)
    bt = Button(new10, text="ADD", command=add_new_book)
    bt.place(x=150, y=150)
    l5 = Label(new10, text="")
    l5.place(x=150, y=180)
    l4=Label(new10,text="Enter book's publication")
    l4.place(x=10,y=100)
    e4=Entry(new10,width=15)
    e4.place(x=160,y=100)
    l6=Label(new10,text="")
    l6.place(x=20,y=200)

def show_desktop_frame(del_win):
    del_win.destroy()
    new01=Toplevel(base,height=500,width=300)
    new01.title("desktop frame")

    b1=Button(new01,text="Issue Book" ,command=lambda: show_frame_2(new01))
    b1.place(x=10,y=10)
    b2=Button(new01,text="Return Book",command=lambda: show_frame_3(new01))
    b2.place(x=10,y=40)
    b3=Button(new01,text="Not Returned Books",command=lambda: show_frame_5(new01))
    b3.place(x=10,y=70)
    b4=Button(new01,text="Search Book",command=lambda: show_frame_4(new01))
    b4.place(x=10,y=100)
    b5=Button(new01,text="Search Student",command=lambda: show_frame_6(new01))
    b5.place(x=10,y=130)
    b7=Button(new01,text="check student history",command=lambda: show_frame_7(new01))
    b7.place(x=10,y=160)
    b8=Button(new01,text="Check book history",command=lambda: show_frame_8(new01))
    b8.place(x=10,y=190)
    b9=Button(new01,text="Add new student",command=lambda: show_frame_9(new01))
    b9.place(x=10,y=220)
    b10=Button(new01,text="Add new book",command=lambda: show_frame_10(new01))
    b10.place(x=10,y=250)
    b6=Button(new01,text="EXIT",command=exit)
    b6.place(x=10,y=280)

show_desktop_frame(temp)
base.mainloop()



