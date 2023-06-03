# -*- coding: utf-8 -*-
"""
Created on Thu april 31 12:35:55 2023

@author: jigyasu
"""
from tkinter import*
import tkinter.messagebox as tkm
from tkinter import Frame
from tkinter import Label

import mysql.connector

# databse connection

conn=mysql.connector.connect(host='localhost',username='root',password='Admin@123',database='mydata')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Connection Succesfully Created!")


ids=[10]


#the GUI window using tkinter
class Mainfile:
    def __init__(self,master):
        self.master=master
        self.master.title("Doctor Appointment App(DAA) ")
        self.master.geometry("1540x800+0+0")
        
        #Frame creation inmaster
        self.left=Frame(master,width=850,height=720,bg='black')
        self.left.pack(side=LEFT)
        self.right=Frame(master,width=800,height=720,bg='steelblue')
        self.right.pack(side=RIGHT)
        
        self.heading=Label(self.left,bd=20,relief=RIDGE,text="Doctor Appointment ⛨",font=("Times new roman" ,60, "bold"),fg='white',bg='black')
        self.heading.place(x=0,y=0)

        

        ##name of patient
        self.name=Label(self.left,text="Patient Name:",font=('arial 18 bold'),fg='white',bg='black')
        self.name.place(x=50,y=200)
        #age of patient
        self.age=Label(self.left,text="Age:",font=('arial 18 bold'),fg='white',bg='black')
        self.age.place(x=50,y=250)
        #gender of patient
        self.gender=Label(self.left,text="Gender:",font=('arial 18 bold'),fg='white',bg='black')
        self.gender.place(x=50,y=300)
        #address
        self.address=Label(self.left,text="Address:",font=('arial 18 bold'),fg='white',bg='black')
        self.address.place(x=50,y=350)
        #problem
        self.problem=Label(self.left,text="Problem:",font=('arial 18 bold'),fg='white',bg='black')
        self.problem.place(x=50,y=400)
        #Appointment-Date
        self.problem=Label(self.left,text="Appointment Date:",font=('arial 18 bold'),fg='white',bg='black')
        self.problem.place(x=25,y=450)
        #Appointment-time
        self.problem=Label(self.left,text="Appointment Time:",font=('arial 18 bold'),fg='white',bg='black')
        self.problem.place(x=25,y=500)
        #phone
        self.phone=Label(self.left,text="Phone No:",font=('arial 18 bold'),fg='white',bg='black')
        self.phone.place(x=50,y=550)
        
        #Since we have created the labels for all the info
        #Now we need to create lables to accept entries
        
        self.nameEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.nameEntry.place(x=250,y=210)
        self.ageEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.ageEntry.place(x=250,y=260)
        self.genderEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.genderEntry.place(x=250,y=310)
        self.addressEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.addressEntry.place(x=250,y=360)
        self.problemEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.problemEntry.place(x=250,y=410)
        self.AdateEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.AdateEntry.place(x=250,y=460)
        self.AtimeEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.AtimeEntry.place(x=250,y=510)
       
        self.phoneEntry=Entry(self.left,width=20,font=("Times new roman" ,20, "bold"))
        self.phoneEntry.place(x=250,y=560)
        
        #creating a button
        self.done=Button(self.left,text='Fix Appointment',font=("Times new roman" ,15, "bold"),width=30,height=3,bg='steelblue',command=self.addAppointment)
        self.done.place(x=200,y=620)
       
      
    

         # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Today's Appointment", font=('arial 20 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "\nTotal Appointments till now :  " + (str(self.final_id)))
        self.box.insert(END,"\nAvailable Slots: " +(str(self.new)))

          
     
     

    def addAppointment(self):
        #print("AllSet this was for checking")
        #get() for user inputs
        #somewhat similar to C++/object oriented programming
        self.x1=self.nameEntry.get()
        self.x2=self.ageEntry.get()
        self.x3=self.genderEntry.get()
        self.x4=self.addressEntry.get()
        self.x5=self.problemEntry.get()
        self.x6=self.AdateEntry.get()
        self.x7=self.AtimeEntry.get()
        self.x8=self.phoneEntry.get()
        
        #To check if the above thoings are working or not....
        #Dummy Print
        #print(self.x1)
        #print(self.x2)
        #print(self.x3)
        #print(self.x4)
        #print(self.x5)
        #print(self.x6)
        if self.x1=='' or self.x2=='' or self.x3=='' or self.x4=='' or self.x5=='' or self.x6=='' or self.x7==''or self.x8=='':
            #print("All boxes are cumpolsury")
            tkm.showinfo("ERROR!!!","All boxes are cumpulsory")
        elif self.x1.isdigit(): 
            tkm.showinfo("Error","Invalid name")   
        elif self.x2.isalpha():
            
            tkm.showinfo("Error","Invalid age")
        elif self.x3.isdigit(): 
            tkm.showinfo("Error","Invalid gender")       
        elif self.x8.isalpha():
            tkm.showinfo("Error","Invalid Phone no.")        
        else:
            print("ALL INPUTS Done")
            #database transfer of details
            con=mysql.connector.connect(host='localhost',username='root',password='Admin@123',database='mydata')
            my_cursor=con.cursor()
            my_cursor.execute("insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.x1,self.x2,self.x3,self.x4,self.x5,self.x6,self.x7,self.x8,)) 

            con.commit()
            con.close()
            tkm.showinfo("Success"," Successfully Appointment booked for  " + self.x1 + "  at " + self.x7 + " on " + self.x6 )
#Objects   
root=Tk()
b=Mainfile(root)
#Dimensions of the window are being set
#root.geometry('%dx%d+%d+%d' % (width, height, x, y))----got to know from StackOverflow
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()