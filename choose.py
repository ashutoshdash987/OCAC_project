from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import subprocess

app = Tk()
app.title('Main menu')
app.state('zoomed')
app.configure(background='')

def onenter(e):
    income['background'] = 'green'
def onleave(e):
    income['background'] = 'purple2'
def onenter2(e):
    converter['background'] = 'green'
def onleave2(e):
    converter['background'] = 'purple2'
def onenter3(e):
    attendance['background'] = 'green'
def onleave3(e):
    attendance['background'] = 'purple2'
def onenter4(e):
    electricity['background'] = 'green'
def onleave4(e):
    electricity['background'] = 'purple2'
def onenter_back(e):
    back['background'] = 'black'
def onleave_back(e):
    back['background'] = 'red'
def back():
    app.destroy()
    subprocess.Popen(["python","index.py"])
def income():
    app.destroy()
    subprocess.Popen(["python","income.py"])
def convert():
    app.destroy()
    subprocess.Popen(["python","converter.py"])
def electric():
    app.destroy()
    subprocess.Popen(["python","electricity.py"])
def attend():
    app.destroy()
    subprocess.Popen(["python","attendance.py"])


Label(text='Welcome   To   Powerpro   Calculator',bg='orange',fg='black',font=('ROG Fonts' ,26)).pack(fill='x')
img = Image.open('option.png')
img = img.resize((1750,950))
image = ImageTk.PhotoImage(img)


label = Label(app,image=image)
label.pack()


lf1 = LabelFrame(bd='5',text='  Options  ',bg='azure',fg='red',font=('Comic Sans MS',14))
lf1.place(x=500,y=180,width=500,height=420)


income = Button(lf1,text='Income Calculator',bg='purple2',fg='white',width=25,height=1,font='aerial 16',cursor='hand2',command=income)
income.place(x=80,y=30)
income.bind("<Enter>",onenter)
income.bind("<Leave>",onleave)

converter = Button(lf1,text='Unit Converter',bg='purple2',fg='white',width=25,height=1,font='aerial 16',cursor='hand2',command=convert)
converter.place(x=80,y=110)
converter.bind("<Enter>",onenter2)
converter.bind("<Leave>",onleave2)

attendance = Button(lf1,text='Attendance Calculator',bg='purple2',fg='white',width=25,height=1,font='aerial 16',cursor='hand2',command=attend)
attendance.place(x=80,y=190)
attendance.bind("<Enter>",onenter3)
attendance.bind("<Leave>",onleave3)

electricity = Button(lf1,text='Electricity Calculator',bg='purple2',fg='white',width=25,height=1,font='aerial 16',cursor='hand2',command=electric)
electricity.place(x=80,y=270)
electricity.bind("<Enter>",onenter4)
electricity.bind("<Leave>",onleave4)

back = Button(text='<--  back',bg='red',fg='white',width=10,font='aerial 16',cursor='hand2',command=back)
back.place(x=10,y=700)
back.bind("<Enter>",onenter_back)
back.bind("<Leave>",onleave_back)

app.mainloop()