from prettytable import PrettyTable
mt = PrettyTable(['Date','Description','Income','Expense','Total'])
def C1():
    print('"If your number is 1-9 please place 0 before your number. \n "Enter item using format : date +income/-expense description or <ENTER> to end.')
    while True:
        Word = str(input(": ")) 
                                        
        if Word == "":
            wt = ""
            file = open("Data.txt","a+")                                  #Read and write at the same time
            file.write(wt+"\n")
            file.close
            break

        file = open("Data.txt","a+")                                  #Read and write at the same time
        file.write(Word+"\n")
        file.close
def C2():
    T = 0
    n = input('"If your number is 1-9 please place 0 before your number." \n Enter Date/Month/Year to display : ')                      #input specific date 
    with open ("Data.txt", "r") as myfile:                      #open file
        data = myfile.read().splitlines()
                
    lenght = len(data)                                          #check how much elements are
    for i in range(lenght):
        if(data[i][0:10] == str(n)) :                           #Date is stored as list element and each elemen t has date position between first 0 - 10 character
            #print (data[i])
            Data = data[i].partition(" ")[0]
            MDT = data[i].partition(" ")[2]
            M = MDT.partition(" ")[0] 
            DT = MDT.partition(" ")[2]
            T += int(M)
            if(data[i][11] == str("+")):
                mt.add_row([Data,DT,M," ",T])
                        #print(mt)
                        
            elif(data[i][11] == str("-")):
                mt.add_row([Data,DT," ",M,T])
    mt.add_autoindex('No')
    print(mt)
def C3():
    T=0
    n = input("If your number is 1-9 please place 0 before your number.\nEnter Month/Year to display : ")  
    with open ("Data.txt", "r") as myfile:         
        data = myfile.read().splitlines()

    lenght = len(data) 
        
    for i in range(lenght):
        if(data[i][3:10] == n): 
            Data = data[i].partition(" ")[0]
            MDT = data[i].partition(" ")[2]
            M = MDT.partition(" ")[0] 
            DT = MDT.partition(" ")[2]
            T += int(M)
            if(data[i][11] == str("+")):
                mt.add_row([Data,DT,M," ",T])
                        #print(mt)
            elif(data[i][11] == str("-")):
                mt.add_row([Data,DT," ",M,T])
    mt.add_autoindex('No')
    print(mt)
def C4():
    print(" 1) Save the day \n 2) Monthly record \n 3) Eecord for years  " )
    Ch = int(input('Please select : '))
    if Ch == 1:
        DMY = input("If your number is 1-9 please place 0 before your number.\nEnter Date/Month/Year to save : ")
        name = input("What is the name of the file: ")        
        completeName = name + ".txt"  
        with open ("Data.txt", "r") as myfile:                      
            data = myfile.read().splitlines()
                
        lenght = len(data)
        for i in range(lenght):
            if(data[i][0:10] == str(DMY)) :
                File = data[i]
                    #print(File)
                file1 = open(completeName , "a+")
                file1.write(File+"\n")
                file1.close() 
        print("''''''''''''''''''''''''''''upload completed''''''''''''''''''''''''''''")

    elif Ch == 2:
        MY = input("If your number is 1-9 please place 0 before your number.\nEnter Month/Year to save : ")
        name = input("What is the name of the file: ")        
        completeName = name + ".txt"  
        with open ("Data.txt", "r") as myfile:                      
            data = myfile.read().splitlines()
                
        lenght = len(data)
        for i in range(lenght):
            if(data[i][3:10] == str(MY)) :
                File = data[i]
                    #print(File)
                file1 = open(completeName , "a+")
                file1.write(File+"\n")
                file1.close() 
        print("''''''''''''''''''''''''''''upload completed''''''''''''''''''''''''''''")

    elif Ch == 3:
        Year = input("If your number is 1-9 please place 0 before your number.\nEnter Year to save : ")
        name = input("What is the name of the file: ")        
        completeName = name + ".txt"  
        with open ("Data.txt", "r") as myfile:                      
            data = myfile.read().splitlines()
                
        lenght = len(data)
        for i in range(lenght):
            if(data[i][6:10] == str(Year)) :
                File = data[i]
                    #print(File)
                file1 = open(completeName , "a+")
                file1.write(File+"\n")
                file1.close() 
        print("''''''''''''''''''''''''''''upload completed''''''''''''''''''''''''''''")
while True:
    print("*** Main Menu *** \n       " )
    print(" 1) Enter item \n 2) Display daily summary \n 3) Display month summary \n 4) Save to file \n 5) Load file \n 6) Exit \n     " )
    Choice = int(input('Please select : '))
    
    if Choice==1:
        C1()

    elif Choice==2:
        C2() 
        
    elif Choice==3:
        C3()

    elif Choice==4:
        C4()

    elif Choice==5:
        pass
                
    elif Choice==6:
        break