def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mob = mobval.get()
        em = emval.get()
        address =adressval.get()
        gen = genval.get()
        dob = dobval.get()
        date  = time.strftime('%H:%M:%S')
        addedtime = time.strftime('%d/%m/%y')

        try:
            strr = 'insert into studentdata1 values(%s,s%,s%,s%,s%,s%,s%,s%,s%)'
            mycursor.execute(strr,(id,name,mob,em,address,gen,dob,date,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification','Id {} Name{} Added successfully..and want to clean the form'.format(id,name),parent=addroot)
            if (res==True):
                idval.set()
                nameval.set()
                mobval.set()
                emval.set()
                adressval.set()
                genval.set()
                dobval.set()
        except:
            pass



    addroot = Toplevel(master=Dataentryframe)
    addroot.grab_set()
    addroot.geometry('400x400+220+220')
    addroot.title('student management system')
    addroot.resizable(False,False)
    idlabel = Label(addroot,text='Enter Id:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter name:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=60)

    mobilelabel = Label(addroot,text='Enter mobile:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=110)

    emaillabel = Label(addroot,text='Enter email:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=160)

    addresslabel = Label(addroot,text='Enter Address:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=210)

    genderlabel = Label(addroot,text='Enter Gender:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=260)

    doblabel = Label(addroot,text='Enter D.O.B:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=310)
#---------------------------------------  add student entry
    idval = StringVar()
    nameval = StringVar()
    mobval = StringVar()
    emval = StringVar()
    adressval = StringVar()
    genval = StringVar()
    dobval = StringVar()

    identry  = Entry(addroot,font=('calibri',15),textvariable=idval,width=18,borderwidth=5)
    identry.place(x=200,y=10)

    nameentry  = Entry(addroot,font=('calibri',15),textvariable=nameval,width=18,borderwidth=5)
    nameentry.place(x=200,y=60)

    mobentry  = Entry(addroot,font=('calibri',15),textvariable=mobval,width=18,borderwidth=5)
    mobentry.place(x=200,y=110)

    ementry  = Entry(addroot,font=('calibri',15),textvariable=emval,width=18,borderwidth=5)
    ementry.place(x=200,y=160)

    addressentry  = Entry(addroot,font=('calibri',15),textvariable=adressval,width=18,borderwidth=5)
    addressentry.place(x=200,y=210)

    genentry  = Entry(addroot,font=('calibri',15),textvariable=genval,width=18,borderwidth=5)
    genentry.place(x=200,y=260)

    dobentry  = Entry(addroot,font=('calibri',15),textvariable=dobval,width=18,borderwidth=5)
    dobentry.place(x=200,y=310)
#------------------------------------- button
    submitbtn = Button(addroot,text='Submit',font=('calibri',15),bg='red',activebackground='green',command=submitadd)
    submitbtn.place(x=150,y=350)


    addroot.mainloop()
def searchstudent():
    def search():
        print("searched")
    searchroot = Toplevel(master=Dataentryframe)
    searchroot.grab_set()
    searchroot.geometry('500x500+220+220')
    searchroot.title('student management system')
    searchroot.resizable(False,False)
    idlabel = Label(searchroot,text='Enter Id:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter name:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=60)

    mobilelabel = Label(searchroot,text='Enter mobile:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=110)

    emaillabel = Label(searchroot,text='Enter email:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=160)

    addresslabel = Label(searchroot,text='Enter Address:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=210)

    genderlabel = Label(searchroot,text='Enter Gender:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=260)

    doblabel = Label(searchroot,text='Enter D.O.B:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=310)

    datelabel = Label(searchroot,text='Enter Date:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=360)
#---------------------------------------  add student entry
    idval = StringVar()
    nameval = StringVar()
    mobval = StringVar()
    emval = StringVar()
    adressval = StringVar()
    genval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry  = Entry(searchroot,font=('calibri',15),textvariable=idval,width=18,borderwidth=5)
    identry.place(x=200,y=10)

    nameentry  = Entry(searchroot,font=('calibri',15),textvariable=nameval,width=18,borderwidth=5)
    nameentry.place(x=200,y=60)

    mobentry  = Entry(searchroot,font=('calibri',15),textvariable=mobval,width=18,borderwidth=5)
    mobentry.place(x=200,y=110)

    ementry  = Entry(searchroot,font=('calibri',15),textvariable=emval,width=18,borderwidth=5)
    ementry.place(x=200,y=160)

    addressentry  = Entry(searchroot,font=('calibri',15),textvariable=adressval,width=18,borderwidth=5)
    addressentry.place(x=200,y=210)

    genentry  = Entry(searchroot,font=('calibri',15),textvariable=genval,width=18,borderwidth=5)
    genentry.place(x=200,y=260)

    dobentry  = Entry(searchroot,font=('calibri',15),textvariable=dobval,width=18,borderwidth=5)
    dobentry.place(x=200,y=310)

    dateentry  = Entry(searchroot,font=('calibri',15),textvariable=dateval,width=18,borderwidth=5)
    dateentry.place(x=200,y=360)
#------------------------------------- button
    submitbtn = Button(searchroot,text='Submit',font=('calibri',15),bg='red',activebackground='green',command=search)
    submitbtn.place(x=150,y=410)


    searchroot.mainloop()

def deletestudent():
    print('student delete')

def updatestudent():
    def update():
        print("searched")
    updateroot = Toplevel(master=Dataentryframe)
    updateroot.grab_set()
    updateroot.geometry('600x600+220+220')
    updateroot.title('student management system')
    updateroot.resizable(False,False)
    idlabel = Label(updateroot,text='Enter Id:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter name:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=60)

    mobilelabel = Label(updateroot,text='Enter mobile:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=110)

    emaillabel = Label(updateroot,text='Enter email:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=160)

    addresslabel = Label(updateroot,text='Enter Address:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=210)

    genderlabel = Label(updateroot,text='Enter Gender:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=260)

    doblabel = Label(updateroot,text='Enter D.O.B:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=310)

    datelabel = Label(updateroot,text='Enter Date:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=360)

    timelabel = Label(updateroot,text='Enter time:',font=('calibri',15),bg='light green',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=410)
#---------------------------------------  add student entry
    idval = StringVar()
    nameval = StringVar()
    mobval = StringVar()
    emval = StringVar()
    adressval = StringVar()
    genval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry  = Entry(updateroot,font=('calibri',15),textvariable=idval,width=18,borderwidth=5)
    identry.place(x=200,y=10)

    nameentry  = Entry(updateroot,font=('calibri',15),textvariable=nameval,width=18,borderwidth=5)
    nameentry.place(x=200,y=60)

    mobentry  = Entry(updateroot,font=('calibri',15),textvariable=mobval,width=18,borderwidth=5)
    mobentry.place(x=200,y=110)

    ementry  = Entry(updateroot,font=('calibri',15),textvariable=emval,width=18,borderwidth=5)
    ementry.place(x=200,y=160)

    addressentry  = Entry(updateroot,font=('calibri',15),textvariable=adressval,width=18,borderwidth=5)
    addressentry.place(x=200,y=210)

    genentry  = Entry(updateroot,font=('calibri',15),textvariable=genval,width=18,borderwidth=5)
    genentry.place(x=200,y=260)

    dobentry  = Entry(updateroot,font=('calibri',15),textvariable=dobval,width=18,borderwidth=5)
    dobentry.place(x=200,y=310)

    dateentry  = Entry(updateroot,font=('calibri',15),textvariable=dateval,width=18,borderwidth=5)
    dateentry.place(x=200,y=360)

    timeentry  = Entry(updateroot,font=('calibri',15),textvariable=timeval,width=18,borderwidth=5)
    timeentry.place(x=200,y=410)
#------------------------------------- button
    submitbtn = Button(updateroot,text='Submit',font=('calibri',15),bg='red',activebackground='green')
    submitbtn.place(x=150,y=460)


    updateroot.mainloop()
def showstudent():
    print('student show')
def datatudent():
    print('student data')
def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    if res== True:
        root.destroy()











def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    timelabel.config(text='Date:'+date_string+ '\n'+ 'Time:'+time_string)
    timelabel.after(200,tick)


def connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()

        except:
            messagebox.showerror('notification','data is incorrect please try again')
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int ,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),time varchar(50),date varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected to database....',parent=dbroot)
        except:
            strr= "use studentmanagementsystem1"
            mycursor.execute(strr)
            messagebox.showinfo('Notification','now you are connected to the database.....',parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.geometry('500x300+480+300')
    dbroot.grab_set()
    dbroot.resizable(False,False)
    dbroot.config(bg='purple')
    ############################################ Id labels
    hostlabel = Label(dbroot,text='Enter host:',bg='light blue',font=('calibri',15),relief=GROOVE,borderwidth=4,width=14,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text='Enter User:',bg='light blue',font=('calibri',15),relief=GROOVE,borderwidth=4,width=14,anchor='w')
    userlabel.place(x=10,y=60)

    passwordlabel = Label(dbroot,text='Enter Password:',bg='light blue',font=('calibri',15),relief=GROOVE,borderwidth=4,width=14,anchor='w')
    passwordlabel.place(x=10,y=110)
    #_________________________________-__________________________ Entery box
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()


    hostentry = Entry(dbroot,font=('calibri',15),borderwidth=5,width=25,textvariable=hostval)
    hostentry.place(x=230,y=10)
    userentry = Entry(dbroot,font=('calibri',15),borderwidth=5,width=25,textvariable=userval)
    userentry.place(x=230,y=60)
    passwordentry = Entry(dbroot,font=('calibri',15),borderwidth=5,width=25,textvariable=passwordval)
    passwordentry.place(x=230,y=110)

    ################################################### connectdb
    submitbutton = Button(dbroot,text='Submit',font=('calibri',15),width=20,borderwidth=5,command=submitdb,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=200)


    dbroot.mainloop()






from tkinter import *
from tkinter import Toplevel,messagebox
import time
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql

root = Tk()
root.title('Library Management System')
root.config(bg='yellow')
root.geometry('800x600+200+100')
root.iconbitmap()
root.resizable(False,False)
################################################### Frames
Dataentryframe = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
Dataentryframe.place(x=10,y=80,width=350,height=500)
############################################################### frame intro
frontlabel = Label(Dataentryframe,text='-----------------WELCOME-----------------------',width=30,font=('calibri',15),bg='yellow',)
frontlabel.pack(side='top',expand=True)

addbutton = Button(Dataentryframe,font=('calibri',15),width=30,bg='grey',text='1. Add Student',relief=GROOVE,bd=5,activebackground='blue',activeforeground='white',command=addstudent)
addbutton.pack(side='top',expand=True)

searchbutton = Button(Dataentryframe,font=('calibri',15),width=30,bg='grey',text='2. Search Student',relief=GROOVE,bd=5,activebackground='blue',activeforeground='white',command=searchstudent)
searchbutton.pack(side='top',expand=True)

delbutton = Button(Dataentryframe,font=('calibri',15),width=30,bg='grey',text='3. Delete Student',relief=GROOVE,bd=5,activebackground='blue',activeforeground='white',command=deletestudent)
delbutton.pack(side='top',expand=True)

upbutton = Button(Dataentryframe,font=('calibri',15),width=30,bg='grey',text='4. Update Student',relief=GROOVE,bd=5,activebackground='blue',activeforeground='white',command=updatestudent)
upbutton.pack(side='top',expand=True)

shbutton = Button(Dataentryframe,font=('calibri',15),width=30,bg='grey',text='5. Show All',relief=GROOVE,bd=5,activebackground='blue',activeforeground='white',command=showstudent)
shbutton.pack(side='top',expand=True)

dtbutton = Button(Dataentryframe,font=('calibri',15),width=30,bg='grey',text='6. Export data',relief=GROOVE,bd=5,activebackground='blue',activeforeground='white',command=datatudent)
dtbutton.pack(side='top',expand=True)

exbutton = Button(Dataentryframe,font=('calibri',15),width=30,bg='grey',text='7. Exit',relief=GROOVE,bd=5,activebackground='blue',activeforeground='white',command=exitstudent)
exbutton.pack(side='top',expand=True)
########################################################################### SHOWDATA
showdataframe1 = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
showdataframe1.place(x=380,y=80,width=400,height=500)
#------------------------------------------------------------------------------ showdata frame
style = ttk.Style()
style.configure('Treeview.Heading',font=('calibri',20),foreground='blue')
style.configure('Treeview',font=('calibri',15,'bold'),foreground='black',background='cyan')



scroll_x = Scrollbar(showdataframe1,orient=HORIZONTAL)
scroll_y = Scrollbar(showdataframe1,orient=VERTICAL)

studenttable = Treeview(showdataframe1,columns=('ID','Name','Mobile No.','Gender','Email',
                                                'Address','Dob','Added date','added time'),
                        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Gender',text='Gender')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Dob',text='Dob')
studenttable.heading('Added date',text='Added date')
studenttable.heading('added time',text='added time')
studenttable['show'] = 'headings'

studenttable.pack(fill=BOTH,expand=1)


################################################### label

introlabel = Label(root,text='Student Management System',font=('calibri',15),relief=GROOVE,borderwidth=5)
introlabel.place(x=250,y=0)

timelabel = Label(root,font=('calibri',13),relief=GROOVE,borderwidth=5,)
timelabel.place(x=0,y=0)
tick()
######################################################### connect button
connectbutton = Button(root,text='Connect To Database',font=('calibri',14),relief=GROOVE,borderwidth=5,
                       activebackground='blue',activeforeground='white',command=connectdb)
connectbutton.place(x=610,y=0)












root.mainloop()