import os
import shutil
import re

def view_dir():
    print(os.getcwd(),"\n")
    print(os.listdir())

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

#path=r"C:\Users\yogesh\desktop\python practice\PycharmProjects\testFolder"
#os.chdir(path)
path=os.getcwd()

#creating directories
create_dir("nImages")
create_dir("nMusic")
create_dir("nFiles")
create_dir("nOthers")

#creating filters parameters
lst_images=["png","jpeg","gif"]
lst_music = ["mp3","mp4"]
lst_files = ["txt","pdf","docx","csv","xlsx"]
lst_default_folder= ["nFiles","nImages","nMusic","nOthers"]

#moving files
if __name__ ==  "__main__":
    for i in os.listdir():
        f_ext = re.split("[.]",i)[-1]      #using re module
        # f_ext = os.path.splitext(i)[-1]  #using os module

        if f_ext in lst_images:
            shutil.move(i,os.path.join(path+"\\nImages\\",i))
            continue

        elif f_ext in lst_music:
            shutil.move(i,os.path.join(path+"\\nMusic\\",i))
            continue

        elif f_ext in lst_files:
            shutil.move(i,os.path.join(path+"\\nFiles\\",i))
            continue

        elif f_ext in lst_default_folder:
            continue

        # elif i == "fileCLeaner.py":
        #     pass

        else:
            shutil.move(i,os.path.join(path+"\\nOthers\\",i))




