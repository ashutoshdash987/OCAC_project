from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import subprocess

app = Tk()
app.title('Login')
app.state('zoomed')
app.configure(background='salmon1')

def onenter(e):
    login['background'] = 'green'
def onleave(e):
    login['background'] = 'red'
def onenter2(e):
    cancel['background'] = 'green'
def onleave2(e):
    cancel['background'] = 'red'
def check():
    username = e1.get()
    password = e2.get()

    if username == "":
        messagebox.showinfo("warning","First Field is empty")
    elif password == "":
        messagebox.showinfo("warning","Second Field is empty")
    else:
        if(username == 'ocac') and (password == 'ocac'):
            app.destroy()
            subprocess.Popen(["python","choose.py"])
        else:
            messagebox.showerror("Invalid credentials","username or password is wrong")
def back():
    app.destroy()
Label(app,text="Login To PowerPro Calculator",font=('Cascadia Code SemiBold',24),bg='orange',fg='black').pack(fill='x')

img = Image.open('login.jpg')
img = img.resize((1750,950))
image = ImageTk.PhotoImage(img)

label = Label(app,image=image)
label.place(x=0,y=54)


username = StringVar()
password = StringVar()

lf1 = LabelFrame(bd='5',text=' Login ',bg='lavender',fg='red',font=('Copperplate Gothic Bold',20))
lf1.place(x=500,y=240,width=500,height=420)

Label(lf1,text='username',font=('Copperplate Gothic Bold',18),bg='lavender',fg='black').pack()

e1 = Entry(lf1,bd='0.8',font='impack 13',bg='white',textvariable = username)
e1.pack()


Label(lf1,text='password',font=('Copperplate Gothic Bold',18),bg='lavender',fg='black').pack()

e2 = Entry(lf1,bd='0.8',font='impack 13',show='*',bg='white',textvariable=password)
e2.pack()


login = Button(lf1,text='Login',font='ariel 15 bold',bg='red',fg='white',bd='2',cursor='hand2',command=check)
login.place(x=70,y=200,width=150)
login.bind("<Enter>",onenter)
login.bind("<Leave>",onleave)

cancel = Button(lf1,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd='2',cursor='hand2',command=back)
cancel.place(x=270,y=200,width=150)
cancel.bind("<Enter>",onenter2)
cancel.bind("<Leave>",onleave2)

lf2 = LabelFrame(bd='5',text='  Developed By  ',bg='white',fg='black',font=('Comic Sans MS',20))
lf2.place(x=1125,y=600,width=410,height=200)


Label(lf2,text='Ashutosh Dash',font='aerial 16',bg='white',fg='black').place(x=120,y=10)
Label(lf2,text='Subhrajit Swain',font='aerial 16',bg='white',fg='black').place(x=120,y=60)
Label(lf2,text='Omm Prakash Sahoo',font='aerial 16',bg='white',fg='black').place(x=100,y=110)


app.mainloop()