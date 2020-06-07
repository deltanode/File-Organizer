import os
import shutil
import re
from tkinter import *
from tkinter import messagebox

current_path=os.getcwd()

#creating filters parameters
lst_images=["png","jpeg","jpg","gif","tiff","eps","psd","ai","indd","raw","ico"]
lst_music = ["mp3","wav","wma","dsd","alac","aac","flac","aiff"]
lst_videos = ["mp4","avi","moc","qt","mkv","avchd","flv","swf"]
lst_documents = ["txt","pdf","doc","docx","csv","xls","xlsx","ppt","pptx","ods","odt","html","htm"]
lst_skip= ["1-Documents","2-Images","3-Music","4-Videos","5-Miscellaneous"]


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def organise(received_path):
    path = received_path
    os.chdir(path)
    # creating directories
    create_dir("1-Documents")
    create_dir("2-Images")
    create_dir("3-Music")
    create_dir("4-Videos")
    create_dir("5-Miscellaneous")

    # moving files in Directories
    if __name__ ==  "__main__":
        for i in os.listdir():
            f_ext = re.split("[.]",i)[-1]      #using re module
            # f_ext = os.path.splitext(i)[-1]  #using os module

            if f_ext in lst_documents:
                shutil.move(i,os.path.join(path+"\\1-Documents\\",i))
                continue

            if f_ext in lst_images:
                shutil.move(i,os.path.join(path+"\\2-Images\\",i))
                continue

            elif f_ext in lst_music:
                shutil.move(i,os.path.join(path+"\\3-Music\\",i))
                continue

            elif f_ext in lst_videos:
                shutil.move(i,os.path.join(path+"\\4-Videos\\",i))
                continue

            elif f_ext in lst_skip:
                continue

            else:
                shutil.move(i,os.path.join(path+"\\5-Miscellaneous\\",i))

def set_path():
    path = path_input.get()
    # print(path)
    organise(path)


## Creating GUI  -----------------------------------

root = Tk()
root.title("File Organizer - [YYSCOOP.com]")
root.geometry("635x450")
#root.iconbitmap("images/favicon.ico")
#root.config(bg="white")

background_image = PhotoImage(file=current_path+"\img/a.png")
bg_label = Label(root, image=background_image, width=635)
bg_label.grid(row=0,columnspan=2,sticky=W+N,padx=0)

hfontstyle = ("Helvetica",30,"bold")
path_label = Label(root,text="File Organizer",font=hfontstyle)
path_label.grid(row=0,columnspan=2, sticky=W+N+E)

fontstyle = ("Helvetica",10,"bold")
path_label = Label(root,text="Enter File Location:",font=fontstyle)
path_label.grid(row=2,columnspan=2, sticky=W,padx=5,pady=5)

path_input = Entry(root,width=75,font=fontstyle)
path_input.grid(row=3,column=0, sticky=W, padx=5,pady=5)

submit_btn = Button(root,text="Organise File", command=set_path,fg="white",bg="#f57971")
submit_btn.grid(row=3,column=1,sticky=W,padx=5,pady=5)

ex_fontstyle = ("Helvetica",8,"normal")
path_label = Label(root,text=r"Ex : C:\Users\user\Desktop\doc\folder1\data",font=ex_fontstyle,fg="red")
path_label.grid(row=4,columnspan=2, sticky=W,padx=5)

root.mainloop()
