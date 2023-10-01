from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import subprocess

add = Tk()
add.title('Electricity Calculator')
add.state('zoomed')

def onenter_back(e):
    backk['background'] = 'black'
def onleave_back(e):
    backk['background'] = 'red'
def onenter(e):
    checkk['background'] = 'steel blue'
def onleave(e):
    checkk['background'] = 'sky blue'
def main():
    add.destroy()
    subprocess.Popen(["python","choose.py"])
    
def check():

    price.configure(text='')
    breakd.configure(text='')
    first.configure(text='')
    second.configure(text='')
    
    unit = e1.get()

    if(unit == ""):
        messagebox.showinfo('warning','first field is empty')

    elif(float(unit) < 0):
        messagebox.showinfo('warning','Total Units cannot be negative')

    else:
        unit = float(unit)
        if(unit > 50):
            extra = unit - 50
            res = (50*6) + (extra*6.5)
            res = format(res,'.2f')
        else:
            res = unit*6
        price.configure(text=f'Total Price is {res}')
        breakd.configure(text=f'Breakdown')
        first.configure(text=f'First 50 units : ₹6')
        second.configure(text=f'Rest all units : ₹6.5')


Label(add,text='Electricity Bill Calculator',bg='orange',fg='black',height=1,font=('Algerian',22)).pack(fill='x')

img = Image.open('electric.jpg')
img = img.resize((1750,950))
image = ImageTk.PhotoImage(img)


label = Label(add,image=image)
label.pack()

lf = LabelFrame(add,bd='5',text=' Electricity Bill Calculator ',bg='white',fg='green',font=('Comic Sans MS',14))
lf.place(x=120,y=200,width=500,height=320)

units = Label(lf,text='Total Units',font='aerial 16',fg = 'black',bg='white')
units.place(x =190,y = 35)

e1 = Entry(lf,font='aerial 12',bg='lavender')
e1.place(x = 150,y = 80)

checkk = Button(lf,text='Check Price',bg='sky blue',fg='black',font='aerial 12',command=check,cursor='hand2')
checkk.place(x = 190, y = 150)
checkk.bind("<Enter>",onenter)
checkk.bind("<Leave>",onleave)

lf1 = LabelFrame(add,bd='5',text=' Price ',bg='white',fg='green',font=('Comic Sans MS',14))
lf1.place(x=920,y=200,width=500,height=320)

price = Label(lf1,text='',font='aerial 16',fg = 'red',bg='white')
price.place(x = 150,y = 10)

breakd = Label(lf1,text='',font='aerial 16 underline',fg = 'purple3',bg='white')
breakd.place(x = 170,y = 80)

first = Label(lf1,text='First 50 units : ₹6',font='aerial 16',fg = 'black',bg='white')
first.place(x = 150,y = 120)

second = Label(lf1,text='Rest all units : ₹6.5',font='aerial 16',fg = 'black',bg='white')
second.place(x = 150,y = 170)

backk = Button(add,text='<--  back',bg='red',fg='white',width=10,font='aerial 16',cursor='hand2',command=main)
backk.place(x=10,y=700)
backk.bind("<Enter>",onenter_back)
backk.bind("<Leave>",onleave_back)

add.mainloop()