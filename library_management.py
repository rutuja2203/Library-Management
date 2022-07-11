import datetime as dt
class BookInfo:
    def accept_book_info(self):
        self.bk_num = input("Enter Book Number : ")
        self.bk_title = input("Enter Book Title : ")
        self.bk_author = input("Enter Book Author : ")
        self.bk_publication = input("Enter Book Publication : ")

    def write_bk_data_into_file(self):
        fobj = open("book_info.txt","a")
        fobj.write(self.bk_num + "," + self.bk_title + "," + self.bk_author + "," + self.bk_publication + "\n")
        fobj.close()

class StudentInfo:
    def accept_stud_info(self):
        self.st_enr = input("Enter Student Enrollment Number : ")
        self.st_name = input("Enter Student Name : ")
        self.st_email = input("Enter Student Email : ")
        self.st_contact = input("Enter Student Contact Number : ")
        self.st_class = input("Enter Student Class : ")

    def write_st_data_into_file(self):
        fobj = open("stud_info.txt", "a")
        fobj.write(self.st_enr + "," + self.st_name + "," + self.st_email + "," + self.st_contact + "," + self.st_class + "\n")
        fobj.close()

class IssueBook:
    def issue_book_to_student(self):
        self.book_num = input("Enter Book Number to Issue : ")
        self.stud_enr = input("Enter Student Enrollment Number : ")
        self.idate = str(dt.date.today())
        self.rdate = "NOT"
        self.ret_status = "NO"
        self.exp_rdate = str(dt.date.today() + dt.timedelta(7))
        # setting expected return_date after 7 days

    def write_issue_data_into_file(self):
        fobj = open("issued_books.txt", "a")
        fobj.write(self.book_num + "," + self.stud_enr + "," + self.idate + "," + self.rdate + "," + self.ret_status + "," + self.exp_rdate)
        fobj.close()
        print("Warning..!! This Book must be returned ON or BEFORE :", self.exp_rdate)

def issue_book():
    i = IssueBook()
    i.issue_book_to_student()
    i.write_issue_data_into_file()

def return_book():
    ret_bnum = input("Enter Book Number which you want to return : ")
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

def add_new_book():
    b = BookInfo()
    b.accept_book_info()
    b.write_bk_data_into_file()

def add_new_student():
    s = StudentInfo()
    s.accept_stud_info()
    s.write_st_data_into_file()

def search_book_by_book_number():
    book_num=input("Enter the book number")
    fobj=open("book_info.txt","r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_num):
            print(oneline)
        else:
            print("invalid book number!!")

def search_book_by_book_title():
    book_title= input("Enter the book title")
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_title):
            print(oneline)
        else:
            print("invalid book title!!")


def search_book_by_book_author():
    book_author = input("Enter the book author")
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_author):
            print(oneline)
        else:
            print("invalid book author name!!")


def search_book_by_book_publication():
    book_publication = input("Enter the book number")
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(book_publication):
            print(oneline)
        else:
            print("invalid book publication!!")


def search_book():
    print("\t1 - Search by Book Number")
    print("\t2 - Search by Book Title")
    print("\t3 - Search by Book Author")
    print("\t4 - Search by Book Publication")
    ch = int(input("\tProvide your choice : "))
    if ch==1:
        search_book_by_book_number()
    elif ch==2:
        search_book_by_book_title()
    elif ch==3:
        search_book_by_book_number()
    elif ch==4:
        search_book_by_book_publication()

def search_stud_by_roll():
    stud_roll = input("Enter the enrollment no. of student")
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_roll):
            print(oneline)
        else:
            print("Roll number not found!!")

def search_stud_by_name():
    stud_name = input("Enter the name of student")
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_name):
            print(oneline)
        else:
            print("Name not found!!")
def search_stud_by_email():
    stud_email = input("Enter the enrollment no. of student")
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_email):
            print(oneline)
        else:
            print("EMAIL not found!!")
def search_stud_by_cellno():
    stud_cellno = input("Enter the contact no. of student")
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_cellno):
            print(oneline)
        else:
            print("contact number not found!!")
def search_stud_by_class():
    stud_class = input("Enter the class of student")
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    for oneline in fdata_ls:
        if oneline.__contains__(stud_class):
            print(oneline)
        else:
            print("class not found!!")

def  search_student():
    print("\t1 - Search by Enrollment Number")
    print("\t2 - Search by Student Name")
    print("\t3 - Search by Email Address")
    print("\t4 - Search by Contact Number")
    print("\t5 - Search by Class")
    ch = int(input("\tProvide your choice : "))
    if ch==1:
        search_stud_by_roll()
    elif ch==2:
        search_stud_by_name()
    elif ch==3:
        search_stud_by_email()
    elif ch==4:
        search_stud_by_cellno()
    elif ch==5:
        search_stud_by_class()


def check_book_history():
    # i will open issued_book.txt file and print all the lines containing book number as provided in input
    count = 0
    b_num = input("Enter Book number to print History : ")

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
    s_enr = input("Enter Student Enrollment Number : ")

    fobj = open("stud_info.txt","r")
    fdata_ls = fobj.readlines()
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
    ch = input("\n\nDo you want to send Reminder to all these students? (Y/N) : ")
    if ch=='y' or ch=='Y':
        send_reminder()
    else:
        print("Later you can do it manually...")

def take_backup():
    pass

def send_reminder():
    pass



while True:
    print("\n")
    print("1 - ISSUE BOOK")
    print("2 - RETURN BOOK")
    print("3 - ADD NEW BOOK")
    print("4 - ADD NEW STUDENT")
    print("5 - SEARCH BOOK")
    print("6 - SEARCH STUDENT")
    print("7 - CHECK BOOK HISTORY")
    print("8 - CHECK STUDENT HISTORY")
    print("9 - NOT RETURNED BOOKS")
    print("* - TAKE BACKUP")
    print("# - SEND REMINDER EMAIL & SMS")
    print("0 - EXIT")
    ch = input("Provide your choice : ")

    if ch=="1":
        issue_book()
    elif ch=="2":
        return_book()
    elif ch=="3":
        add_new_book()
    elif ch=="4":
        add_new_student()
    elif ch=="5":
        search_book()
    elif ch=="6":
        search_student()
    elif ch=="7":
        check_book_history()
    elif ch=="8":
        check_student_history()
    elif ch=="9":
        not_returned_books()
    elif ch=="*":
        take_backup()
    elif ch=="#":
        send_reminder()
    elif ch=="0":
        exit(0)

