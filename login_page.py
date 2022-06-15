
from tkinter import *

#Root Window GUI
root=Tk()
root.geometry("600x450")
root.title("Private Variable Login Page")
root.configure(bg="white")

#Labels
name_label = Label(root,text="Name:",bg="black",font=("Inter",15,"bold"),fg="white")
name_label.place(relx=0.4,rely=0.2,anchor=CENTER)

pwd_label = Label(root,text="Password:",bg="black",font=("Inter",15,"bold"),fg="white")
pwd_label.place(relx=0.4,rely=0.3,anchor=CENTER)

captcha_label = Label(root,text="Captcha:",bg="black",font=("Inter",15,"bold"),fg="white")
captcha_label.place(relx=0.4,rely=0.4,anchor=CENTER)

#Input Boxes
name_input_box = Entry(root)
name_input_box.place(relx=0.6,rely=0.2,anchor=CENTER)

pwd_input_box = Entry(root)
pwd_input_box.place(relx=0.6,rely=0.3,anchor=CENTER)

captcha_IB = Entry(root)
captcha_IB.place(relx=0.6,rely=0.4,anchor=CENTER)

#Updated Labels
updated_name = Label(root,bg="black",font=("Inter",15,"bold"),fg="white")
updated_name.place(relx=0.5,rely=0.6,anchor=CENTER)

updated_pwd = Label(root,bg="black",font=("Inter",15,"bold"),fg="white")
updated_pwd.place(relx=0.5,rely=0.7,anchor=CENTER)

updated_cap = Label(root,bg="black",font=("Inter",15,"bold"),fg="white")
updated_cap.place(relx=0.5,rely=0.8,anchor=CENTER)

#Class
class class1:
    def __init__(self):
        self.__username = "Swarnim Nipankar"
        self.__password = "pythonisgreat"
        self.__captcha = "WhItEhAtJr"
        
    def show_profile(self):
        updated_name["text"] = "Name: "+self.__username
        updated_pwd["text"] = "Password: "+self.__password
        updated_cap["text"] = "Captcha: "+self.__captcha
        
#Object for class
user = class1()

#Function for 'update_details' button
def addUser():
    global user
    user.username = name_input_box.get()
    user.password = pwd_input_box.get()
    user.captcha = captcha_IB.get()
    print("Details Updated")
    
#Buttons
update_details = Button(root,text="Update Login Details",command=addUser,bg="black",fg="white",font=("Inter",15,"bold"))
update_details.place(relx=0.4,rely=0.5,anchor=CENTER)

show_profile = Button(root,text="Show Profile",command=user.show_profile,bg="black",fg="white",font=("Inter",15,"bold"))
show_profile.place(relx=0.6,rely=0.5,anchor=CENTER)

#Run Statement
root.mainloop()