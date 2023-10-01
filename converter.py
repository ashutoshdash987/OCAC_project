from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import subprocess

app = Tk()
app.title('Unit Converter')
app.state('zoomed')

def onenter(e):
    change['background'] = 'mediumpurple4'
def onleave(e):
    change['background'] = 'purple2'

def main():
    app.destroy()
    subprocess.Popen(["python","choose.py"])

def onenter_back(e):
    backk['background'] = 'black'
def onleave_back(e):
    backk['background'] = 'red'

def value():
    val = var.get()
    val = int(val)

    if(val == 1):
        unit.configure(text='f')
        change.configure(text='Convert Unit to celcius')
    if(val == 2):
        unit.configure(text='m')
        change.configure(text='Convert Unit to Kilometer')
    if(val == 3):
        unit.configure(text='km')
        change.configure(text='Convert Unit to meter')
    if(val == 4):
        unit.configure(text='cm')
        change.configure(text='Convert Unit to meter')
    if(val == 5):
        unit.configure(text='m')
        change.configure(text='Convert Unit to CentiMeter')

def convert():
    val = var.get()
    val = int(val)
    
    num = e1.get()
    

    if(num == "" and val == 0):
        messagebox.showerror('error','Select Any operation first !!')
    elif(num == "" and val != 0):
        messagebox.showinfo('warniing','Field is empty')
    elif(float(num) < 0):
        messagebox.showinfo('warning','Cannot enter negative values')
    else:
        num = float(num)
        if(val == 1):
            res = (5/9)*(num-32)
            res = format(res,".4f")
            result.configure(text=f'{num} fahrenheit = {res} celcius')

        elif(val == 2):
            res = num * 0.001
            res = format(res,".4f")
            result.configure(text=f'{num} m = {res} km')

        elif(val == 3):
            res = num * 1000
            res = format(res,".4f")
            result.configure(text=f'{num} km = {res} m')
        
        elif(val == 4):
            res = num * 0.01
            res = format(res,".4f")
            result.configure(text=f'{num} cm = {res} m')
        
        elif(val == 5):
            res = num * 100
            res = format(res,".4f")
            result.configure(text=f'{num} m = {res} cm')

Label(text='Unit Converter',bg='orange',fg='black',height=1,font=('Algerian',26)).pack(fill='x')

img = Image.open('convert.jpg')
img = img.resize((1750,1150))
image = ImageTk.PhotoImage(img)


label = Label(app,image=image)
label.pack()

var = IntVar()

rd1 = Radiobutton(app,text='degree to celcius',variable=var,value=1,font='aerial 16',command=value,bg='gray92')
rd1.place (x = 100, y = 250)

rd2 = Radiobutton(app,text='m to km',variable=var,value=2,font='aerial 16',command=value,bg='gray92')
rd2.place (x = 400, y = 250)

rd2 = Radiobutton(app,text='km to m',variable=var,value=3,font='aerial 16',command=value,bg='gray92')
rd2.place (x = 700, y = 250)

rd3 = Radiobutton(app,text='cm to m',variable=var,value=4,font='aerial 16',command=value,bg='gray92')
rd3.place (x = 1000, y = 250)

rd4 = Radiobutton(app,text='m to cm',variable=var,value=5,font='aerial 16',command=value,bg='gray92')
rd4.place (x = 1300, y = 250)

old = Label(text='Enter the value ',font='aerial 16',bg='gray92')
old.place(x = 400, y = 400)

e1 = Entry(font='aerial 16')
e1.place(x = 600,y = 400)

unit = Label(text='',font='aerial 12')
unit.place(x = 850,y = 400)

change = Button(text='Convert Unit',font= 'aerial 12',bg='purple2',fg='white',command=convert,cursor='hand2')
change.place(x = 900,y = 400)
change.bind("<Enter>",onenter)
change.bind("<Leave>",onleave)

result = Label(text='',font='aerial 16',fg='red',bg='gray92')
result.place(x = 600, y = 450)

backk = Button(text='<--  back',bg='red',fg='white',width=10,font='aerial 16',cursor='hand2',command=main)
backk.place(x=10,y=700)
backk.bind("<Enter>",onenter_back)
backk.bind("<Leave>",onleave_back)

app.mainloop()