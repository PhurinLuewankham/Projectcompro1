
import pandas as pd
from datetime import datetime
from prettytable import PrettyTable 
from itertools import product
from tkinter import *
import matplotlib.pyplot as plt

mt = PrettyTable(['Date','Description','Income','Expense','Total'])
T = 0
root = Tk()
root.title("Programe tracking income and expense")


#ข้อ1
def notetake():
    root2 = Tk()
    root2.title("Take note of expenses")

    myLabel2 = Label(root2,text="Enter item using format",fg="White",font=('arial',10)).pack()
    myLabel2 = Label(root2,text="Date/Month/Year +/- Price Type",fg="White",font=('arial',10)).pack()
    myLabel2 = Label(root2,text="Ex : 01/02/2020 -50 Food ",fg="red",font=('arial',10)).pack()
    entry1 = Entry(root2)
    entry1.pack()
    root2.geometry("300x300+190+220")

    def EXIT2():
        root2.destroy()

    def program1():
        value = entry1.get()

        file = open("Data.txt","a")                                  #Read and write at the same time
        file.write(value + "\n")
        file.close
        myLabel2 = Label(root2,text="---Data saved---",fg="green",bg="white",font=('arial',15)).pack(pady=5)
    def clear1():
        entry1.delete(0,END)
        

    btn8 = Button(root2,text="Save",fg="green",bg="white",font=('arial',13),command=program1).pack()
    btn10 = Button(root2,text="Clear",fg="black",bg="white",font=('arial',13),command=clear1).pack()
    btn9 = Button(root2,text="Exit",fg="red",bg="white",font=('arial',13),command=EXIT2).pack()

    root2.mainloop()

    
def EXIT():
    root.destroy()

#ข้อ2 แสดงค่าใช้จ่ายรายวัน
def Daily():
    root3 = Tk()
    root3.title("Daily Summary")
    root3.geometry("300x200+190+220")
    myLabel3 = Label(root3,text= '"If your number is 1-9 please place 0 before your number"',fg='red',font=('arial',10,'bold')).pack()
    myLabel4 = Label(root3,text= "Enter: Date/Month/Year",fg='white',font=('arial',10,'bold')).pack()

    entry2 = Entry(root3)
    entry2.pack() 

    def savec1():
        daily_screen = Tk()
        daily_screen.title("Record of the day")
        daily_screen.geometry("300x300+1010+220")
        myLabel4 = Label(daily_screen,text= "Today's expenses",fg='Green',bg="white",font=('arial',16,'bold')).pack()
        T = 0 
        n = entry2.get()
        with open ("Data.txt", "r") as myfile:                      #open file
            data = myfile.read().splitlines()
        lenght = len(data)  
                                                #check how much elements are
        for i in range(lenght):
            if(data[i][0:10] == str(n)) :  
                daily_data = data[i]                         #Date is stored as list element and each elemen t has date position between first 0 - 10 character
                #print (data[i])
                Label(daily_screen, text=daily_data).pack(pady=2)
                
        ending =  "-----End of the day-----"          
        Label(daily_screen, text=ending,fg='Red',bg="white",font=('arial',16,'bold')).pack(pady=5)    
        mt.add_autoindex('No')
        
    def EXIT4():
        root3.destroy()

    btn11 = Button(root3,text="Search",fg="green",bg="white",font=('arial',13),command=savec1).pack()
    btn12 = Button(root3,text="Cancel",fg="red",bg="white",font=('arial',13),command=EXIT4).pack()
#ข้อ3 แสดงค่าใช้จ่ายรายเดือน
def Month():
    root5 = Tk()
    root5.title("Month Summary")
    root5.geometry("300x200+190+220")
    myLabel3 = Label(root5,text= '"If your number is 1-9 please place 0 before your number"',fg='red',font=('arial',10,'bold')).pack()
    myLabel4 = Label(root5,text= "Enter: Month/Year",fg='white',font=('arial',10,'bold')).pack()
    entry2 = Entry(root5)
    entry2.pack() 
    def save3():
        T = 0
        n = entry2.get()
        monthly_screen = Tk()
        monthly_screen.title("Record of the month")
        monthly_screen.geometry("300x300+1010+220")
        myLabel4 = Label(monthly_screen,text= "Monthly expenses",fg='Green',bg="white",font=('arial',16,'bold')).pack()
        with open ("Data.txt", "r") as myfile:                      #open file
            data = myfile.read().splitlines()
        lenght = len(data)  
                                                #check how much elements are
        for i in range(lenght):
            if(data[i][3:10] == str(n)) :  
                daily_data = data[i]                         #Date is stored as list element and each elemen t has date position between first 0 - 10 character
                #print (data[i])
                Label(monthly_screen, text=daily_data).pack()
                
                
        ending =  "-----End of the month-----"             
        Label(monthly_screen, text=ending,fg='Red',bg="white",font=('arial',16,'bold')).pack(pady=5)    
        mt.add_autoindex('No')  
    
    def EXIT3():
        root5.destroy()
    btn8 = Button(root5,text="Search",fg="green",bg="white",font=('arial',13),command=save3).pack()
    btn9 = Button(root5,text="Cancel",fg="red",bg="white",font=('arial',13),command=EXIT3).pack()

#หน้ากราฟรายเดือน
def graphmonth():
    gt = Tk()
    gt.title("Month summary graph")
    gt.geometry("300x200+190+220")
    myLabel2 = Label(gt,text="Enter: Month/Year",fg="white",font=('arial',12)).pack()
    myLabel3 = Label(gt,text="Ex : 01/2020",fg="red",font=('arial',12)).pack()
    entry1 = Entry(gt)
    entry1.pack()
    def graphtt():
        n = entry1.get()
        spending_type = []          #Storing type of spending 
        spending_amount = []        #Storing amount of spending 
        with open ("Data.txt", "r") as myfile:                      #open file
            data = myfile.read().splitlines()
        lenght = len(data)                                          #check how much elements are
        for i in range(lenght):
            if(data[i][3:10] == str(n)) :                      #Date is stored as list element and each elemen t has date position between first 0 - 10 character
                Data = data[i].partition(" ")[0]
                MDT = data[i].partition(" ")[2]
                M = MDT.partition(" ")[0] 
                DT = MDT.partition(" ")[2]
                
                if M[0] == str("-"):        #Check if outcome or income
                    spending_type.append(DT)                #if outcome -> spending_type, spending_amount
                    spending_amount.append(abs(int(M)))
                
                elif M[0] == str("+"):     #if income pass this 
                    pass            # <------
                

                
        plt.pie(spending_amount,labels=spending_type,autopct="%.1f%%")  #<----- ploting 
        plt.show()
    def EXIT2():
        gt.destroy()
    btn8 = Button(gt,text="Search",fg="green",bg="white",font=('arial',13),command=graphtt).pack()
    btn9 = Button(gt,text="Cancel",fg="red",bg="white",font=('arial',13),command=EXIT2).pack()

#แสดงกราฟรายวัน
def graphdaily():
    gt = Tk()
    gt.title("Daily sammary graph")
    gt.geometry("300x200+190+220")
    myLabel2 = Label(gt,text="Enter: Day/Month/Year",fg="white",font=('arial',12)).pack()
    myLabel3 = Label(gt,text="Ex : 01//02/2020",fg="red",font=('arial',12)).pack()
    entry1 = Entry(gt)
    entry1.pack()
    def graphtt():
        n = entry1.get()
        spending_type = []          #Storing type of spending 
        spending_amount = []        #Storing amount of spending 
        with open ("Data.txt", "r") as myfile:                      #open file
            data = myfile.read().splitlines()
        lenght = len(data)                                          #check how much elements are
        for i in range(lenght):
            if(data[i][0:10] ==str(n)) :                      #Date is stored as list element and each elemen t has date position between first 0 - 10 character
                Data = data[i].partition(" ")[0]
                MDT = data[i].partition(" ")[2]
                M = MDT.partition(" ")[0] 
                DT = MDT.partition(" ")[2]
                
                if M[0] == str("-"):        #Check if outcome or income
                    spending_type.append(DT)                #if outcome -> spending_type, spending_amount
                    spending_amount.append(abs(int(M)))
                
                elif M[0] == str("+"):     #if income pass this 
                    pass            # <------
                

                
        plt.pie(spending_amount,labels=spending_type,autopct="%.1f%%")  #<----- ploting 
        plt.show()
    def EXIT2():
        gt.destroy()
    btn8 = Button(gt,text="Search",fg="green",bg="white",font=('arial',13),command=graphtt).pack()
    btn9 = Button(gt,text="Cancel",fg="red",bg="white",font=('arial',13),command=EXIT2).pack()
    
myLabel1 = Label(root,text="Main menu",fg="green",bg="white",font=('arial',30,'bold')).pack(pady=5)
btn1 = Button(root,text="Take notes",fg="black",font=('arial',20),command=notetake).pack(pady=5)
btn2 = Button(root,text="Daily summary display",fg="black",font=('arial',20),command=Daily).pack(pady=3)
btn3 = Button(root,text="Month summary display",fg="black",font=('arial',20),command=Month).pack(pady=3)
btn7 = Button(root,text="Daily graph display",fg="black",font=('arial',20),command=graphdaily).pack(pady=3)
btn7 = Button(root,text="Monthly graph display",fg="black",font=('arial',20),command=graphmonth).pack(pady=3)
btn6 = Button(root,text="Exit",fg="red",font=('arial',20),command=root.quit).pack(pady=5)
root.geometry("500x320+500+150")

root.mainloop()