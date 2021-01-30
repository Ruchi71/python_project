from tkinter import *
import datetime
import time




def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print(date)
        print(now)


        if now == set_alarm_timer:
            print("Time to Wake up")


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x400")

time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="purple",font=('calibri',15)).place(x=160,y=20)
addTime = Label(clock,text = "Hour       Min        Sec",font=('calibri',20)).place(x = 200,y=50)
setYourAlarm = Label(clock,text = "Wakeup time",fg="blue",relief =GROOVE,borderwidth=5,bg='light blue',font=("Helevetica",20,"bold")).place(x=5, y=90)


hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime= Entry(clock,textvariable = hour,bg = "yellow",font=('calibri',20),relief=GROOVE,width = 5,borderwidth=5).place(x=190,y=90)
minTime= Entry(clock,textvariable = min,bg = "yellow",font=('calibri',20),width = 5,relief=GROOVE,borderwidth=5).place(x=280,y=90)
secTime = Entry(clock,textvariable = sec,bg = "yellow",font=('calibri',20),width = 5,borderwidth=5,relief=GROOVE).place(x=370,y=90)


submit = Button(clock,text = "Set Alarm",fg="red",width = 10,bg='light blue',command = actual_time,font=("calibri",15)).place(x =200,y=190)

clock.mainloop()