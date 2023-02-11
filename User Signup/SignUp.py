from tkinter import *
from tkinter import messagebox
import ast
from PIL import ImageTk, Image



window=Tk()
window.title("Sign Up")
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)


# Open Image
signup_img = Image.open("SignUp.png")

#Resize Image
resized=signup_img.resize((348, 436), Image.ANTIALIAS)

new_signup_img = ImageTk.PhotoImage(resized)
# signup_img.place(x=100, y=100)


signup_label=Label(window, image=new_signup_img, border=0, bg="white")
signup_label.place(x=50,y=30)

frame=Frame(window,width=302,height=400,bg="white")
frame.place(x=560,y=70)



heading = Label(window, text="Sign Up", fg="#57a1f8", bg="white", font=("Century Gothic", 24))
heading.place(x=650,y=15)


def on_enter(e):
    full_name.delete(0, "end")
def on_exit(e):
    if full_name.get()=="":
        full_name.insert(0, "Enter Full Name")


full_name = Entry(frame, width = 25, fg = "black", border=0, bg = "white", font=("Century Gothic", 11))
full_name.place(x=50, y=30)
full_name.insert(0, "Enter Full Name")
full_name.bind("<FocusIn>", on_enter)
full_name.bind("<FocusOut>", on_exit)
Frame(frame, width=203, height=2, bg="black").place(x=50, y=51)


def on_enter(e):
    dob.delete(0, "end")
def on_exit(e):
    if dob.get()=="":
        dob.insert(0, "Enter Full Name")


dob = Entry(frame, width = 25, fg = "black", border=0, bg = "white", font=("Century Gothic", 11))
dob.place(x=50, y=60)
dob.insert(0, "Select D.o.B")
dob.bind("<FocusIn>", on_enter)
dob.bind("<FocusOut>", on_exit)
Frame(frame, width=203, height=2, bg="black").place(x=50, y=81)



def on_enter(e):
    userbox.delete(0, "end")
def on_exit(e):
    if userbox.get()=="":
        userbox.insert(0, "Enter Username")


userbox = Entry(frame, width = 25, fg = "black", border=0, bg = "white", font=("Century Gothic", 11))
userbox.place(x=50, y=110)
userbox.insert(0, "Enter Username")
userbox.bind("<FocusIn>", on_enter)
userbox.bind("<FocusOut>", on_exit)
Frame(frame, width=203, height=2, bg="black").place(x=50, y=131)


def on_enter(e):
    passbox.delete(0, "end")
def on_exit(e):
    if passbox.get()=="":
        passbox.insert(0, "Enter Password")


passbox = Entry(frame, width = 25, fg = "black", border=0, bg = "white", font=("Century Gothic", 11))
passbox.place(x=50, y=140)
passbox.insert(0, "Enter Password")
passbox.bind("<FocusIn>", on_enter)
passbox.bind("<FocusOut>", on_exit)
Frame(frame, width=203, height=2, bg="black").place(x=50, y=161)


def on_enter(e):
    confirm_passbox.delete(0, "end")
def on_exit(e):
    if confirm_passbox.get()=="":
        confirm_passbox.insert(0, "Re-enter Password")


confirm_passbox = Entry(frame, width = 25, fg = "black", border=0, bg = "white", font=("Century Gothic", 11))
confirm_passbox.place(x=50, y=170)
confirm_passbox.insert(0, "Re-enter Password")
confirm_passbox.bind("<FocusIn>", on_enter)
confirm_passbox.bind("<FocusOut>", on_exit)
Frame(frame, width=203, height=2, bg="black").place(x=50, y=191)


def on_enter(e):
    enter_email.delete(0, "end")
def on_exit(e):
    if enter_email.get()=="":
        enter_email.insert(0, "Enter Email")


enter_email = Entry(frame, width = 25, fg = "black", border=0, bg = "white", font=("Century Gothic", 11))
enter_email.place(x=50, y=200)
enter_email.insert(0, "Enter Email")
enter_email.bind("<FocusIn>", on_enter)
enter_email.bind("<FocusOut>", on_exit)

Frame(frame, width=203, height=2, bg="black").place(x=50, y=221)

signup_button=Button(frame, width=34,pady=7,text="Sign Up", bg="#57a1f8", fg="white",border=0).place(x=30,y=241)
# signup_button.place()
signin_label=Label(frame, text="Already have an account?", fg="#57a1f8", bg="white", font=("Century Gothic", 9))
signin_label.place(x=73,y=280)

signin_button=Button(frame,width=8, pady=7,border=0, text="Sign In", bg="#57a1f8", fg="white", cursor="hand2", font=("Century Gothic", 9))
signin_button.place(x=120,y=300)



window.mainloop()