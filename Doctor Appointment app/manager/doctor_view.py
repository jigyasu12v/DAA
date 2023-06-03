from tkinter import *
import mysql.connector
import tkinter as tk
import sys

# databse connection

conn=mysql.connector.connect(host='localhost',username='root',password='Admin@123',database='mydata')
my_cursor=conn.cursor()


print("Connection Succesfully Created!")
number = []
patients = []


query = "SELECT * FROM doctor"
my_cursor.execute(query)
doctor= my_cursor.fetchall()


class PrintRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)

# Create the tkinter window
window = tk.Tk()

# Create a text box to display the messages
text_box = tk.Text(window)
text_box.pack()

for appointment in doctor:
    name = appointment[0]
    age = appointment[1]
    problem =appointment[4]
    date= appointment[5]
    time=appointment[6]



# window
class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Display Application(PDD)")
        self.master.geometry("1540x800+0+0")
        self.x = 0
        
        # heading
        self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
        self.heading.place(x=350, y=0)
        

        # button to change patients
        self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=500, y=600)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 200 bold'))
        self.n.place(x=500, y=100)

        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=300, y=400)
    # function to speak the text and update the text
    def func(self):
       sys.stdout = PrintRedirector(text_box)

       print("Patient Name:",name)
       print("Age",age)
       print("Problem:",problem)
       print("Appointment Date:",date)
       print("Appointment Time:",time)




       window.mainloop()
       my_cursor.close()
       conn.close()
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()
