from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import subprocess

# Function to calculate attendance percentage
def onenter_back(e):
    backk['background'] = 'black'
def onleave_back(e):
    backk['background'] = 'red'

def onenter(e):
    calculate_button['background'] = 'mediumpurple4'
def onleave(e):
    calculate_button['background'] = 'purple2'

def main():
    app.destroy()
    subprocess.Popen(["python","choose.py"])

def calculate_percentage():
    try:
        result_label.config(text=f"Attendance Percentage: ")
        classs.config(text=f'')
        held.config(text=f'')
        flag = 0
        cls = 0
        lst=[]
        # Get attendance for each day from input fields
        attendance = []
        for i in range(1, 16):
            day_attendance = day_entries[i - 1].get()
            attendance.append(int(day_attendance))
        
        # Calculate total attendance
        total_present = sum(attendance)
        
        # Calculate percentage
        percentage = (total_present / 15) * 100
        
        # Display the result
        for i in attendance:
            if(int(i) == 1):
                cls += 1
            if(int(i) == 1 or int(i) == 0):
                flag += 1
            else:
                j = attendance.index(i) + 1
                lst.append(j)
        if(flag == 15):
            result_label.config(text=f"Attendance Percentage: {percentage:.2f}%")
            classs.config(text=f'Classes attended : {cls}')
            held.config(text=f'Classes absent : {15-int(cls)}')
        else:
            a = lst[0]
            messagebox.showinfo('warning',f'You must enter 1 or 0 in day {a}')
    except ValueError:
        messagebox.showerror("Error", "No fields should be empty")

# Create the main application window
app = Tk()
app.title("Attendance Calculator")
app.state("zoomed")
app.configure(background= 'SteelBlue1')
Label(text='Attendance  Percentage  Calculator',bg='orange',fg='black',font=('Algerian',22)).pack(fill='x')
# Labels and Entry fields for 15 days
day_labels = []
day_entries = []

img = Image.open('attend.jpg')
img = img.resize((1750,950))
image = ImageTk.PhotoImage(img)


label = Label(app,image=image)
label.pack()
lf11 = LabelFrame(app,bd='5',bg='azure',fg='green',font='impact 16 italic')
lf11.place(x=260,y=80,width=150,height=50)
Label(lf11,text='0 ➜ absent',font='aerial 14').pack()


lf0 = LabelFrame(app,bd='5',bg='azure',fg='green',font='impact 16 italic')
lf0.place(x=260,y=130,width=150,height=50)
Label(lf0,text='1 ➜ present',font='aerial 14').pack()

lf = LabelFrame(app,bd='5',text='Day Wise Attendance',bg='azure',fg='green',font=('Comic Sans MS',14))
lf.place(x=420,y=70,width=500,height=720)

for i in range(1, 16):
    label = Label(lf, text=f"Day {i}:",font='aerial 14',bg = 'azure')
    entry = Entry(lf,font='aerial 14')
    day_labels.append(label)
    day_entries.append(entry)
    
    label.grid(row=i, column=100, padx=10, pady=5, sticky="w")
    entry.grid(row=i, column=200, padx=10, pady=5)


calculate_button = Button(lf, text="Calculate Percentage", command=calculate_percentage,bg='purple2',fg='white',cursor='hand2',font='aerial 12')
calculate_button.place(x=150,y=600)
calculate_button.bind("<Enter>",onenter)
calculate_button.bind("<Leave>",onleave)

lf1 = LabelFrame(app,bd='5',text='Attendance Percentage',bg='white',fg='green',font=('Comic Sans MS',14))
lf1.place(x=1020,y=270,width=500,height=320)
result_label = Label(lf1, text="Attendance Percentage:",bg='white',font='aerial 16')



result_label.grid(row=17, column=0, columnspan=2, pady=10)

classs = Label(lf1, text="",bg='white',font='aerial 16')
classs.place(x = 110, y = 100)

held = Label(lf1, text="",bg='white',font='aerial 16')
held.place(x = 110, y = 150)

backk = Button(text='<--  back',bg='red',fg='white',width=10,font='aerial 16',cursor='hand2',command=main)
backk.place(x=10,y=700)
backk.bind("<Enter>",onenter_back)
backk.bind("<Leave>",onleave_back)

app.mainloop()