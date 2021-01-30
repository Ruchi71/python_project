from tkinter import *
import pytube
root = Tk()
root.title("Youtube Downloader")
root.geometry("600x400")
root.config(bg="purple")

def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("C:\\Users\\R N CHOUBEY\\Desktop\\vids")
        notif.config(fg="green",text="download complete")

    except Exception as e:
        print(e)

        notif.config(fg="red",text="video could not be downloaded")



Label(root,text = "Youtube Downloader",font = ("calibri",30,"bold"),width=25,fg = "black",bg ="yellow",relief = GROOVE,borderwidth=5).place(x=50,y=30)
Label(root,text = "Enter the link of your video",font = ("calibri",20,"bold"),width=25,fg = "black",bg ="light blue",relief = GROOVE,borderwidth=5).place(x=120,y=120)

notif = Label(root,font=("calibri",12)).place(x=100,y=340)

url =StringVar()

Entry(root,width=50,textvariable =url,font=("calibri",13),relief=GROOVE,borderwidth=5).place(x=100,y=200)

Button(root,width=20,text="Download",font=("calibri",13)).place(x=190,y=280)


root.mainloop()