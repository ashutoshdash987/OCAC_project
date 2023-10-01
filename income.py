from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import subprocess

app = Tk()
app.title('income expense calculator')
app.state('zoomed')
def onenter_back(e):
    backk['background'] = 'black'
def onleave_back(e):
    backk['background'] = 'red'
def onenter(e):
    btn['background'] = 'mediumpurple4'
def onleave(e):
    btn['background'] = 'purple2'
def main():
    app.destroy()
    subprocess.Popen(["python","choose.py"])
def balance():
    balan.configure(text = '')
    if(e1.get() == ""):
        messagebox.showinfo("Warning" , "Income field of monday is empty")
    elif(e1a.get() == ""):
        messagebox.showinfo("Warning", "Expense field of monday is empty")
    elif(float(e1.get()) < 0):
        messagebox.showinfo("Warning" , "Income field of monday is negative")
    elif(float(e1a.get()) < 0):
        messagebox.showinfo("Warning" , "Expense field of monday is negative")
    elif(float(e1.get()) < float(e1a.get())):
        messagebox.showinfo("Warning" , "Expense of monday is greater than income")


    elif(e2.get() == ""):
        messagebox.showinfo("Warning" , "Income field of tuesday is empty")
    elif(e2a.get() == ""):
        messagebox.showinfo("Warning", "Expense field of tuesday is empty")
    elif(float(e2.get()) < 0):
        messagebox.showinfo("Warning" , "Income field of tuesday is negative")
    elif(float(e2a.get()) < 0):
        messagebox.showinfo("Warning" , "Expense field of tuesday is negative")
    elif(float(e2.get()) < float(e2a.get())):
        messagebox.showinfo("Warning" , "Expense of tuesday is greater than income")



    elif(e3.get() == ""):
        messagebox.showinfo("Warning" , "Income field of wednesday is empty")
    elif(e3a.get() == ""):
        messagebox.showinfo("Warning", "Expense field of wednesday is empty")
    elif(float(e3.get()) < 0):
        messagebox.showinfo("Warning" , "Income field of wednesday is negative")
    elif(float(e3a.get()) < 0):
        messagebox.showinfo("Warning" , "Expense field of wednesday is negative")
    elif(float(e3.get()) < float(e3a.get())):
        messagebox.showinfo("Warning" , "Expense of wednesday is greater than income")


    elif(e4.get() == ""):
        messagebox.showinfo("Warning" , "Income field of thursday is empty")
    elif(e4a.get() == ""):
        messagebox.showinfo("Warning", "Expense field of thursdayis empty")
    elif(float(e4.get()) < 0):
        messagebox.showinfo("Warning" , "Income field of thursday is negative")
    elif(float(e4a.get()) < 0):
        messagebox.showinfo("Warning" , "Expense field of friday is negative")
    elif(float(e4.get()) < float(e4a.get())):
        messagebox.showinfo("Warning" , "Expense of thursday is greater than income")


    elif(e5.get() == ""):
        messagebox.showinfo("Warning" , "Income field of friday is empty")
    elif(e5a.get() == ""):
        messagebox.showinfo("Warning", "Expense field of friday is empty")
    elif(float(e5.get()) < 0):
        messagebox.showinfo("Warning" , "Income field of friday is negative")
    elif(float(e5a.get()) < 0):
        messagebox.showinfo("Warning" , "Expense field of fridayis negative")
    elif(float(e5.get()) < float(e5a.get())):
        messagebox.showinfo("Warning" , "Expense of friday is greater than income")


    elif(e6.get() == ""):
        messagebox.showinfo("Warning" , "Income field of saturday is empty")
    elif(e6a.get() == ""):
        messagebox.showinfo("Warning", "Expense field of saturday is empty")
    elif(float(e6.get()) < 0):
        messagebox.showinfo("Warning" , "Income field of saturday is negative")
    elif(float(e6a.get()) < 0):
        messagebox.showinfo("Warning" , "Expense field of saturday is negative")
    elif(float(e6.get()) < float(e6a.get())):
        messagebox.showinfo("Warning" , "Expense of saturday is greater than income")


    elif(e7.get() == ""):
        messagebox.showinfo("Warning" , "Income field of sunday is empty")
    elif(e7a.get() == ""):
        messagebox.showinfo("Warning", "Expense field of sunday is empty")
    elif(float(e7.get()) < 0):
        messagebox.showinfo("Warning" , "Income field of sunday is negative")
    elif(float(e7a.get()) < 0):
        messagebox.showinfo("Warning" , "Expense field of sunday is negative")
    elif(float(e7.get()) < float(e7a.get())):
        messagebox.showinfo("Warning" , "Expense of sunday is greater than income")
    else:  
        mon_i = float(e1.get())
        mon_e = float(e1a.get())

        tue_i = float(e2.get())
        tue_e = float(e2a.get())

        wed_i = float(e3.get())
        wed_e = float(e3a.get())

        thurs_i = float(e4.get())
        thurs_e = float(e4a.get())

        fri_i = float(e5.get())
        fri_e = float(e5a.get())

        sat_i = float(e6.get())
        sat_e = float(e6a.get())

        sun_i = float(e7.get())
        sun_e = float(e7a.get())

        total_i = mon_i + tue_i + wed_i + thurs_i + fri_i + sat_i + sun_i
        total_e = mon_e + tue_e + wed_e + thurs_e + fri_e + sat_e + sun_e

        bal = float(total_i) - float(total_e)
        bal = format(bal,'.2f')

        balan.configure(text = f'Remaining Balance : {bal}')

Label(text='Income Expense Calculator',font=('Algerian',22),bg='orange',fg='black').pack(fill='x')

img = Image.open('income.jpg')
img = img.resize((1750,950))
image = ImageTk.PhotoImage(img)


label = Label(app,image=image)
label.pack()



lf = LabelFrame(app,bd='5',text='Income Sheet',fg='green',font=('Comic Sans MS',14))
lf.place(x=370,y=40,width=800,height=750)

Label(lf,text='Day',font='imperial 12 italic underline').place(x = 30, y = 5)
Label(lf,text='Income',font='imperial 12 italic underline').place(x = 270, y = 5)
Label(lf,text='Expenses',font='imperial 12 italic underline').place(x = 550, y = 5)
mon = Label(lf,text='Monday',font='aerial 14',fg = 'purple3')
mon.place(x = 30, y = 60)
e1 = Entry(lf,font='aerial 14')
e1.place(x = 200, y = 60)
e1a = Entry(lf,font='aerial 14')
e1a.place(x = 480, y = 60)

tue = Label(lf,text='Tuesday',font='aerial 14',fg = 'purple3')
tue.place(x = 30, y = 140)
e2 = Entry(lf,font='aerial 14')
e2.place(x = 200, y = 140)
e2a = Entry(lf,font='aerial 14')
e2a.place(x = 480, y = 140)

wed = Label(lf,text='Wednesday',font='aerial 14',fg = 'purple3')
wed.place(x = 30, y = 220)
e3 = Entry(lf,font='aerial 14')
e3.place(x = 200, y = 220)
e3a = Entry(lf,font='aerial 14')
e3a.place(x = 480, y = 220)

thurs = Label(lf,text='Thursday',font='aerial 14',fg = 'purple3')
thurs.place(x = 30, y = 300)
e4 = Entry(lf,font='aerial 14')
e4.place(x = 200, y = 300)
e4a = Entry(lf,font='aerial 14')
e4a.place(x = 480, y = 300)

fri = Label(lf,text='Friday',font='aerial 14',fg = 'purple3')
fri.place(x = 30, y = 380)
e5 = Entry(lf,font='aerial 14')
e5.place(x = 200, y = 380)
e5a = Entry(lf,font='aerial 14')
e5a.place(x = 480, y = 380)

sat = Label(lf,text='Saturday',font='aerial 14',fg = 'purple3')
sat.place(x = 30, y = 460)
e6 = Entry(lf,font='aerial 14')
e6.place(x = 200, y = 460)
e6a = Entry(lf,font='aerial 14')
e6a.place(x = 480, y = 460)

sun = Label(lf,text='Sunday',font='aerial 14',fg = 'purple3')
sun.place(x = 30, y = 540)
e7 = Entry(lf,font='aerial 14')
e7.place(x = 200, y = 540)
e7a = Entry(lf,font='aerial 14')
e7a.place(x = 480, y = 540)

btn = Button(lf,text='Check Balance',bg='purple2',fg='white',cursor='hand2',command=balance,font='aerial 12')
btn.place(x=240,y = 650)
btn.bind("<Enter>",onenter)
btn.bind("<Leave>",onleave)

balan = Label(lf,text='',fg='red',font='aerial 16')
balan.place(x = 410, y = 650)

backk = Button(text='<--  back',bg='red',fg='white',width=10,font='aerial 16',cursor='hand2',command=main)
backk.place(x=10,y=700)
backk.bind("<Enter>",onenter_back)
backk.bind("<Leave>",onleave_back)

app.mainloop()