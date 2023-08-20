#importing necessary modules

from tkinter import *
 #importing google speech recognition module
import mysql.connector          #importing database connector module
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Comppr0j11A",database="project comp") #connecting to mysql database that has been created in the system
mycursor=mydb.cursor() #intitalizing the connection function
  #recognizing the microphone from the system

#Creating the mainscreen window
window=Tk()
lbl=Label(window, text="TECHNOMEDIC", fg='black',bg='#A7FFF0', font=("Helvetica", 20,'bold'))#printing the title
lbl2=Label(window, text="The aim of this application is to help manage COVID-19 data giving the user options to either enter or retrieve required data", fg='black',bg='#A7FFF0', font=("Helvetica", 14))#intro
lbl.place(x=520, y=50)#placement
lbl2.place(x=180, y=100)#placement
window.title('TECHNOMEDIC')#window name
window.geometry("1990x2020")#size
window['background']='#A7FFF0'#background color
#CODE FOR CREATING ENTERING DATA INTO MEDICAL TABLE

def create_MT_Window():
    global newWindow
    newWindow =Toplevel(InputWindow)#creating a window to open on click of 'input data' on mainscreen
    labelinput = Label(newWindow, text = "Input your data in the following fields",fg='black',bg='#9EFF7D',font=('Helvetica',14))
    newWindow.geometry("1990x2020")
    newWindow['background']='#9EFF7D'
    labelinput.place(x=80, y=50)

    aadhar=StringVar()
    Label(newWindow,text="aadhar",bg='#9EFF7D').pack()
    aadhar_entry=Entry(newWindow,textvariable=aadhar)
    aadhar_entry.pack()

    oximeter=StringVar()
    Label(newWindow,text="oxygen level",bg='#9EFF7D').pack()
    oximeter_entry=Entry(newWindow,textvariable=oximeter)
    oximeter_entry.pack()

    blood_group=StringVar()
    Label(newWindow,text="blood group",bg='#9EFF7D').pack()
         blood_group_entry=Entry(newWindow,textvariable=blood_group)
    blood_group_entry.pack()

    days=StringVar()
    Label(newWindow,text="days",bg='#9EFF7D').pack()
    days_entry=Entry(newWindow,textvariable=days)
    days_entry.pack()

    variant=StringVar()
    Label(newWindow,text="variant",bg='#9EFF7D').pack()
    variant_entry=Entry(newWindow,textvariable=variant)
    variant_entry.pack()

    def submit():
          submitted= Toplevel(newWindow)
        #creating new variables to pass through sql database that have values if address, aadhar and primary contacts that were entered from entry box
        
        an=aadhar_entry.get()
        o=oximeter_entry.get()
        blg=blood_group_entry.get()
        d=days_entry.get()
        v=variant_entry.get()

        labelExample = Label(submitted, text ="Successful submission",fg='green',bg='#ffffff',font=('Helvetica',14))
        submitted.geometry("800x500+10+10")
        submitted['background']='#FFFFFF'
        labelExample.place(x=80, y=10)

        sql1=""" insert into medical_data
        values (%s,%s,%s,%s,%s)"""
        val1=(an,o,blg,d,v) #passing values into database
        mycursor.execute(sql1,val1)  #executing functions
        mydb.commit()  #running function
        submitted.mainloop()

    button=Button(newWindow,text="submit",command=submit,bg='white')
    button.pack()


#CODE FOR ENTERING DATA INTO VACCINE TABLE

def create_VT_Window():
    global newWindow
    newWindow =Toplevel(InputWindow)#creating a window to open on click of 'input data' on mainscreen
    labelinput = Label(newWindow, text = "Input your data in the following fields",fg='black',bg='#9EFF7D',font=('Helvetica',14))
    newWindow.geometry("1990x2020")
    newWindow['background']='#9EFF7D'
    labelinput.place(x=80, y=50)

    COWIN_NO=StringVar()
    Label(newWindow,text="COWIN Number",bg='#9EFF7D').pack()
    COWIN_NO_entry=Entry(newWindow,textvariable=COWIN_NO)
    COWIN_NO_entry.pack()

    aadhar=StringVar()
    Label(newWindow,text="aadhar",bg='#9EFF7D').pack()
    aadhar_entry=Entry(newWindow,textvariable=aadhar)
    aadhar_entry.pack()

    vaccine=StringVar()
    Label(newWindow,text="vaccine",bg='#9EFF7D').pack()
    vaccine_entry=Entry(newWindow,textvariable=vaccine)
    vaccine_entry.pack()

    CAV=StringVar()
    Label(newWindow,text="Covid after vaccine? (Y/N)",bg='#9EFF7D').pack()
    CAV_entry=Entry(newWindow,textvariable=CAV)
    CAV_entry.pack()

    doses=StringVar()
    Label(newWindow,text="no of doses",bg='#9EFF7D').pack()
    doses_entry=Entry(newWindow,textvariable=doses)
    doses_entry.pack()

    side_effects=StringVar()
    Label(newWindow,text="side effects? (Y/N)",bg='#9EFF7D').pack()
  side_effects_entry=Entry(newWindow,textvariable=side_effects)
    side_effects_entry.pack()

    def submit():
        submitted= Toplevel(newWindow)

        CN=COWIN_NO_entry.get()
        an=aadhar_entry.get()
        v=vaccine_entry.get()
        cav=CAV_entry.get()
        d=doses_entry.get()
        se=side_effects_entry.get()

        labelExample = Label(submitted, text ="Successful submission",fg='green',bg='#ffffff',font=('Helvetica',14))
        submitted.geometry("800x500+10+10")
        submitted['background']='#FFFFFF'
        labelExample.place(x=80, y=10)

        sql1=""" insert into vaccine
        values (%s,%s,%s,%s,%s,%s)"""
        val1=(CN,an,v,cav,d,se) #passing values into database
        mycursor.execute(sql1,val1)  #executing functions
        mydb.commit()  #running function
        submitted.mainloop()
button=Button(newWindow,text="submit",command=submit,bg='white')
    button.pack()

#CODE FOR ENTERING DATA INTO PRIMARY TABLE
def create_PT_Window():
    global newWindow
    newWindow =Toplevel(InputWindow)#creating a window to open on click of 'input data' on mainscreen
    labelinput = Label(newWindow, text = "Input your data in the following fields",fg='black',bg='#9EFF7D',font=('Helvetica',14))
    newWindow.geometry("1990x2020")
    newWindow['background']='#9EFF7D'
    labelinput.place(x=80, y=50)

    
    #entry fields for data
    def fn_speak():
        import speech_recognition as sr
        r = sr.Recognizer()  
        global firstname  #creating a global variable
        # speech recognition code that records first name audio
        
        with sr.Microphone() as source:
            audio=r.record(source,duration=5) # using record function to record audio from pyAudio module
        try:
            firstname=r.recognize_google(audio) #calling the google speech recognition fuction- step where audio gets converted to text
            labelprint = Label(newWindow, text = "the first name that you spoke:"+ firstname,fg='black',bg='white',font=('Helvetica',14))
            labelprint.place(x=80, y=110)      
        except:
            pass
    def ln_speak():
        import speech_recognition as sr
        r = sr.Recognizer()
        # speech recognition code that records last name audio
        global lastname
        #code to record last name
        with sr.Microphone() as source:
            
            audio=r.record(source,duration=5) #using record function to record audio from pyAudio module
        try:
            lastname=r.recognize_google(audio)#calling the google speech recognition fuction- step where audio gets converted to text
            labelprint = Label(newWindow, text = "the last name that you spoke:"+lastname,fg='black',bg='white',font=('Helvetica',14))
            labelprint.place(x=80, y=170)
     
        except:
            pass
    address=StringVar()
    Label(newWindow,text="Address",bg='#9EFF7D').pack()
    address_entry=Entry(newWindow,textvariable=address)
    address_entry.pack()

    
    aadhar=StringVar()
    Label(newWindow,text="aadhar",bg='#9EFF7D').pack()
    aadhar_entry=Entry(newWindow,textvariable=aadhar)
    aadhar_entry.pack()

    
    primary=StringVar()
    Label(newWindow,text=" Number of primary contacts",bg='#9EFF7D').pack()
    primary_entry=Entry(newWindow,textvariable=primary)
    primary_entry.pack()


#function to submit data and insert to database
    def submit():
        submitted= Toplevel(newWindow)

        #creating new variables to pass through sql database that have values if address, aadhar and primary contacts that were entered from entry box
        ad=address_entry.get()
        an=aadhar_entry.get()
        pc=primary_entry.get()
       
        labelExample = Label(submitted, text ="Successful submission",fg='green',bg='#ffffff',font=('Helvetica',14))
        submitted.geometry("800x500+10+10")
        submitted['background']='#FFFFFF'
        labelExample.place(x=80, y=10)

        
        #passing values through sql function and inserting into sql database - using mysql query "insert into information"
        
        sql1=""" insert into primary_table
        values (%s,%s,%s,%s,%s)"""
        val1=(an,firstname,lastname,pc,ad) #passing values into database
        mycursor.execute(sql1,val1)  #executing functions
        mydb.commit()  #running function
        submitted.mainloop()

    button_fn=Button(newWindow,text="click here to speak out your first name!",command=fn_speak,bg='white')
    button_fn.pack()


    button_ln=Button(newWindow,text="click here to speak out your last name!",command=ln_speak,bg='white')
    button_ln.pack()
    #button to submit the inputted data
    button=Button(newWindow,text="submit",command=submit,bg='white')
    button.pack()


#CODE FOR CREATING MAIN INPUT WINDOW AND CALLING IT FROM MAIN PROGRAM
def create_Main_Input_Window():
    global InputWindow
    InputWindow =Toplevel(window)#creating a window to open on click of 'input data' on mainscreen
    labelinput = Label(InputWindow, text = "choose which table you want to enter data in. To enter data in Vaccine and Medical table, input first in primary table",fg='black',bg='#9EFF7D',font=('Helvetica',14))
    InputWindow.geometry("5000x5000")
    InputWindow['background']='#9EFF7D'
    labelinput.place(x=80, y=50)

    input_primary=Button(InputWindow,text="Input data into primary table",fg='black',bg='white', font=("Helvetica", 14),
              command=create_PT_Window)

    input_primary.place(x=555,y=150)

    input_vaccine=Button(InputWindow,text="Input data into vaccine table",fg='black',bg='white', font=("Helvetica", 14),
              command=create_VT_Window)

    input_vaccine.place(x=555,y=200)

    input_medical=Button(InputWindow,text="Input data into medical table",fg='black',bg='white', font=("Helvetica", 14),
              command=create_MT_Window)
    input_medical.place(x=555,y=250)

inputdata=Button(window,text="  Input data ",fg='black',bg='white', font=("Helvetica", 14),
              command=create_Main_Input_Window)
inputdata.place(x=555,y=150)


#CODE TO ACCESS PRIMARY TABLE
def access_PT_Window():
    global newAccessWindow
    
    newAccessWindow =Toplevel(newWindow2)
    labelExample2 = Label(newAccessWindow, text = "Access data by saying out the FIRST NAME",fg='black',font=('Helvetica',14),bg='#9EFF7D')
    
    newAccessWindow.geometry("1990x2020")
    labelExample2.place(x=495, y=50)
    newAccessWindow['background']='#9EFF7D’
    def search_fn():
        import speech_recognition as sr
        r = sr.Recognizer()  
        global name
        #speech recognition code to receive name from user
        with sr.Microphone() as source:
            audio=r.record(source,duration=5)
        try:
            name=r.recognize_google(audio)
            labelFN = Label(newAccessWindow, text = "the name that you spoke"+name,fg='black',bg='white',font=('Helvetica',14))
            labelFN.place(x=80, y=110)
    
        except:
            pass
    #function to access data and display details
    def access():
        accessed= Toplevel(newAccessWindow)
        
        labelExample = Label(accessed, text = "Details are given below:",fg='green',bg='#ffffff',font=('Helvetica',14))
        accessed.geometry("800x500+10+10")
        accessed['background']='#FFFFFF'
        labelExample.place(x=80, y=50)

        #sql query to receive data from the user 
    
        sql="""select * from primary_table
        where FirstName= %s"""
        val=(name,) #passing values 
   
        mycursor.execute(sql,val) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        
        mydb.commit()
        #separating elements from tuple that receives data 
        x=myresult[0]
        aadhar,firstname,lastname,primary_contacts,address= x
        aadhar=str(aadhar)
        primary_contacts=str(primary_contacts)

        #printing elements separately\
        ano=Label(accessed,text="Aadhar: "+aadhar,bg='white',font=12,fg='green')
        ano.place(x=80,y=80)
        fn=Label(accessed,text="First Name: "+firstname,bg='white',font=12,fg='green')
        fn.place(x=80,y=110)
        ln=Label(accessed,text="Last Name :  "+lastname,bg='white',font=12,fg='green')
        ln.place(x=80,y=140)
        pc=Label(accessed,text="Number of primary contacts :  "+primary_contacts,bg='white',font=12,fg='green')
        pc.place(x=80,y=170)
        add=Label(accessed,text="Address:  "+address,bg='white',font=12,fg='green')
        add.place(x=80,y=200)
    
    #creating button to receive audio from user 
    button_fn=Button(newAccessWindow,text="click here to speak the first name of whose data you want to search!",command=search_fn,bg='white')
    button_fn.pack()
    

#button to access- will lead to the display window
    button=Button(newAccessWindow,text="Access",font=('Helvetica',14),command=access,bg='white')
    button.pack(padx=612,pady=100)
    newAccessWindow.mainloop()


#CODE TO ACCESS MEDICAL TABLE
def access_MT_Window():
    global newAccessWindow
    
    newAccessWindow =Toplevel(newWindow2)
    labelExample2 = Label(newAccessWindow, text = "Access data by saying out the FIRST NAME",fg='black',font=('Helvetica',14),bg='#9EFF7D')
    
    newAccessWindow.geometry("1990x2020")
    labelExample2.place(x=495, y=50)
    newAccessWindow['background']='#9EFF7D'
    
    

    def search_fn():
        import speech_recognition as sr
        r = sr.Recognizer()  
        global name
        

        #speech recognition code to receive name from user
        with sr.Microphone() as source:
            audio=r.record(source,duration=5)
        try:
            name=r.recognize_google(audio)
            labelFN = Label(newAccessWindow, text = "the name that you spoke"+name,fg='black',bg='white',font=('Helvetica',14))
            labelFN.place(x=80, y=110)
    
        except:
            pass


    def access():
            
            
        accessed= Toplevel(newAccessWindow)
            
        labelExample = Label(accessed, text = "Details are given below:",fg='green',bg='#ffffff',font=('Helvetica',14))
        accessed.geometry("800x500+10+10")
        accessed['background']='#FFFFFF'
        labelExample.place(x=80, y=50)

        #sql query to receive data from the user 
        
        sql="""select * from primary_table
        where FirstName= %s"""
        val=(name,) #passing values 
       
        mycursor.execute(sql,val) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        mydb.commit()
        #separating elements from tuple that receives data 
        x=myresult[0]
        aadhar,firstname,lastname,primary_contacts,address= x
        aadhar=str(aadhar)
        primary_contacts=str(primary_contacts)

        sql2="""select * from medical_data
        where AadharNumber= %s"""
        val2=(aadhar,)
        mycursor.execute(sql2,val2) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        mydb.commit()
        x=myresult[0]
        
        an,oxi,blood_g,d,v=x
        oxi=str(oxi)
        d=str(d)
        #printing elements separately\
        ano=Label(accessed,text="Aadhar: "+aadhar,bg='white',font=12,fg='green')
        ano.place(x=80,y=80)
        fn=Label(accessed,text="First Name: "+firstname,bg='white',font=12,fg='green')
        fn.place(x=80,y=110)
        ln=Label(accessed,text="Last Name :  "+lastname,bg='white',font=12,fg='green')
        ln.place(x=80,y=140)
        pc=Label(accessed,text="Number of primary contacts :  "+primary_contacts,bg='white',font=12,fg='green')
        pc.place(x=80,y=170)
        add=Label(accessed,text="Address:  "+address,bg='white',font=12,fg='green')
        add.place(x=80,y=200)
        oxl=Label(accessed,text="oximeter: "+oxi,bg='white',font=12,fg='green')
        oxl.place(x=80,y=230)
        bgl=Label(accessed,text="blood group: "+blood_g,bg='white',font=12,fg='green')
        bgl.place(x=80,y=260)
        dl=Label(accessed,text="days: "+d,bg='white',font=12,fg='green')
        dl.place(x=80,y=290)
        vl=Label(accessed,text="variant: "+v,bg='white',font=12,fg='green')
        vl.place(x=80,y=320)
                    
    button_fn=Button(newAccessWindow,text="click here to speak the first name of whose data you want to search!",command=search_fn,bg='white')
    button_fn.pack()
    button=Button(newAccessWindow,text="Access",font=('Helvetica',14),command=access,bg='white')
    button.pack(padx=612,pady=100)
    newAccessWindow.mainloop()

#CODE TO ACCESS VACCINE TABLE

def access_VT_Window():
    global newAccessWindow
    
    newAccessWindow =Toplevel(newWindow2)
    labelExample2 = Label(newAccessWindow, text = "Access data by saying out the FIRST NAME",fg='black',font=('Helvetica',14),bg='#9EFF7D')
    
    newAccessWindow.geometry("1990x2020")
    labelExample2.place(x=495, y=50)
    newAccessWindow['background']='#9EFF7D'
    
    

    def search_fn():
        import speech_recognition as sr
        r = sr.Recognizer()  
        global name
        

        #speech recognition code to receive name from user
        with sr.Microphone() as source:
            audio=r.record(source,duration=5)
        try:
            name=r.recognize_google(audio)
            labelFN = Label(newAccessWindow, text = "the name that you spoke"+name,fg='black',bg='white',font=('Helvetica',14))
            labelFN.place(x=80, y=110)
    
        except:
            pass


    def access():
    
        accessed= Toplevel(newAccessWindow)
        
        labelExample = Label(accessed, text = "Details are given below:",fg='green',bg='#ffffff',font=('Helvetica',14))
        accessed.geometry("800x500+10+10")
        accessed['background']='#FFFFFF'
        labelExample.place(x=80, y=50)

        #sql query to receive data from the user 
    
        sql="""select * from primary_table
        where FirstName= %s"""
        val=(name,) #passing values 
   
        mycursor.execute(sql,val) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        mydb.commit()
        #separating elements from tuple that receives data 
        x=myresult[0]
        aadhar,firstname,lastname,primary_contacts,address= x
        aadhar=str(aadhar)
        primary_contacts=str(primary_contacts)

        sql2="""select * from vaccine
        where AadharNumber= %s"""
        val2=(aadhar,)
        mycursor.execute(sql2,val2) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        mydb.commit()
        x=myresult[0]
        cowin,aad,vn,cav,doses,sex
        cowin=str(cowin)
        doses=str(doses)
        
        #printing elements separately\
        ano=Label(accessed,text="Aadhar: "+aadhar,bg='white',font=12,fg='green')
        ano.place(x=80,y=80)
        fn=Label(accessed,text="First Name: "+firstname,bg='white',font=12,fg='green')
        fn.place(x=80,y=110)
        ln=Label(accessed,text="Last Name :  "+lastname,bg='white',font=12,fg='green')
        ln.place(x=80,y=140)
        pc=Label(accessed,text="Number of primary contacts :  "+primary_contacts,bg='white',font=12,fg='green')
        pc.place(x=80,y=170)
        add=Label(accessed,text="Address:  "+address,bg='white',font=12,fg='green')
        add.place(x=80,y=200)
        cwl=Label(accessed,text="cowin number: "+cowin,bg='white',font=12,fg='green')
        cwl.place(x=80,y=230)
        vn=Label(accessed,text="vaccine"+vn,bg='white',font=12,fg='green')
        vn.place(x=80,y=260)
        cavl=Label(accessed,text="covid after vaccine?: "+cav,bg='white',font=12,fg='green')
        cavl.place(x=80,y=290)
        dosl=Label(accessed,text="doses: "+doses,bg='white',font=12,fg='green')
        dosl.place(x=80,y=320)
        sel=Label(accessed,text="side effects: "+se,bg='white',font=12,fg='green')
        sel.place(x=80,y=350)

            
    button_fn=Button(newAccessWindow,text="click here to speak the first name of whose data you want to search!",command=search_fn,bg='white')
    button_fn.pack()
    button=Button(newAccessWindow,text="Access",font=('Helvetica',14),command=access,bg='white')
    button.pack(padx=612,pady=100)
    newAccessWindow.mainloop()


#CODE TO ACCESS STATISTICS

def access_statistics_window():

    import numpy as np
    import matplotlib.pyplot as plt
     #fetchingdata
    mycursor.execute("select count(*),LOWER(vaccine_name) from vaccine where covid_check_after_vaccine='Y' group by vaccine_name ;")
    result=list(mycursor.fetchall())
    count=[]
    vaccinename=[]
    for i in result:
        
        count.append(i[0])
        vaccinename.append(i[1])
        
# creating the bar plot
    fig = plt.figure(figsize = (10, 5))
    plt.bar(vaccinename, count, color ='maroon', width = 0.4)
    plt.xlabel("vaccine name")
    plt.ylabel("Number of people")
    plt.title("Share of people who got Covid after different vaccines(close to view next graph)")
    plt.show()
    #fetching data
    mycursor.execute("select count(*),covid_check_after_vaccine from vaccine_table group by covid_check_after_vaccine;")
    result=list(mycursor.fetchall())
    count=[]
    for i in result:
        
        count.append(i[0])


#CODE TO ACCESS DATA FROM ALL THREE TABLES
def access_all_Window():
    global newAccessWindow
    newAccessWindow =Toplevel(newWindow2)
    labelExample2 = Label(newAccessWindow, text = "Access data by saying out the FIRST NAME",fg='black',font=('Helvetica',14),bg='#9EFF7D')
    newAccessWindow.geometry("1990x2020")
    labelExample2.place(x=495, y=50)
    newAccessWindow['background']='#9EFF7D'
    def search_fn():
        import speech_recognition as sr
        r = sr.Recognizer()  
        global name
        

        #speech recognition code to receive name from user
        with sr.Microphone() as source:
            audio=r.record(source,duration=5)
        try:
            name=r.recognize_google(audio)
            labelFN = Label(newAccessWindow, text = "the name that you spoke"+name,fg='black',bg='white',font=('Helvetica',14))
            labelFN.place(x=80, y=110)
    
        except:
            pass


    def access():
        
        
        accessed= Toplevel(newAccessWindow)
        
        labelExample = Label(accessed, text = "Details are given below:",fg='green',bg='#ffffff',font=('Helvetica',14))
        accessed.geometry("800x500+10+10")
        accessed['background']='#FFFFFF'
        labelExample.place(x=80, y=50)

        #sql query to receive data from the user 
    
        sql="""select * from primary_table
        where FirstName= %s"""
        val=(name,) #passing values 
   
        mycursor.execute(sql,val) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        mydb.commit()
        #separating elements from tuple that receives data 
        x=myresult[0]
        aadhar,firstname,lastname,primary_contacts,address= x
        aadhar=str(aadhar)
        primary_contacts=str(primary_contacts)

        sql2="""select * from medical_data
        where AadharNumber= %s"""
        val2=(aadhar,)
        mycursor.execute(sql2,val2) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        mydb.commit()
        x=myresult[0]
        
        an,oxi,blood_g,d,v=x
        oxi=str(oxi)
        d=str(d)

        sql3="""select * from vaccine
        where AadharNumber= %s"""
        val3=(aadhar,)
        mycursor.execute(sql3,val3) #executing function
        myresult=mycursor.fetchall() #function to fetch data
        mydb.commit()
        x=myresult[0]

        cowin,aad,vn,cav,doses,se=x
        cowin=str(cowin)
        doses=str(doses)

        #printing elements separately\
        ano=Label(accessed,text="Aadhar: "+aadhar,bg='white',font=12,fg='green')
        ano.place(x=80,y=80)
        fn=Label(accessed,text="First Name: "+firstname,bg='white',font=12,fg='green')
        fn.place(x=80,y=110)
        ln=Label(accessed,text="Last Name :  "+lastname,bg='white',font=12,fg='green')
        ln.place(x=80,y=140)
        pc=Label(accessed,text="Number of primary contacts :  "+primary_contacts,bg='white',font=12,fg='green')
        pc.place(x=80,y=170)
        add=Label(accessed,text="Address:  "+address,bg='white',font=12,fg='green')
        add.place(x=80,y=200)
        oxl=Label(accessed,text="oximeter: "+oxi,bg='white',font=12,fg='green')
        oxl.place(x=80,y=230)
        bgl=Label(accessed,text="blood group: "+blood_g,bg='white',font=12,fg='green')
        bgl.place(x=80,y=260)
        dl=Label(accessed,text="days: "+d,bg='white',font=12,fg='green')
        dl.place(x=80,y=290)
        vl=Label(accessed,text="variant: "+v,bg='white',font=12,fg='green')
        vl.place(x=80,y=320)
        cwl=Label(accessed,text="cowin number: "+cowin,bg='white',font=12,fg='green')
        cwl.place(x=80,y=350)
        vn=Label(accessed,text="vaccine"+vn,bg='white',font=12,fg='green')
        vn.place(x=80,y=380)
        cavl=Label(accessed,text="covid after vaccine?: "+cav,bg='white',font=12,fg='green')
        cavl.place(x=80,y=410)
        dosl=Label(accessed,text="doses: "+doses,bg='white',font=12,fg='green')
        dosl.place(x=80,y=440)
        sel=Label(accessed,text="side effects: "+se,bg='white',font=12,fg='green')
        sel.place(x=80,y=470)   
        
    button_fn=Button(newAccessWindow,text="click here to speak the first name of whose data you want to search!",command=search_fn,bg='white')
    button_fn.pack()
    button=Button(newAccessWindow,text="Access",font=('Helvetica',14),command=access,bg='white')
    button.pack(padx=612,pady=100)
    newAccessWindow.mainloop()


#CREATING MAIN ACCESS WINDOW AND CALLING IT FROM MAIN PROGRAM
def createAccessWindow():
    global newWindow2
    newWindow2 =Toplevel(window)
    labelExample2 = Label(newWindow2, text = "Access data by according to the given buttons",fg='black',font=('Helvetica',14),bg='#9EFF7D')
    
    newWindow2.geometry("1990x2020")
    labelExample2.place(x=495, y=50)
    newWindow2['background']='#9EFF7D'

    access_primary=Button(newWindow2,text="Access data from primary table only",fg='black',bg='white', font=("Helvetica", 14),
              command=access_PT_Window)
    access_primary.place(x=555,y=150)

    access_vaccine=Button(newWindow2,text="Access data from primary and vaccine table",fg='black',bg='white', font=("Helvetica", 14),
              command=access_VT_Window)
    access_vaccine.place(x=555,y=200)

    access_medical=Button(newWindow2,text="Access data from primary and medical",fg='black',bg='white', font=("Helvetica", 14),
              command=access_MT_Window)
    access_medical.place(x=555,y=250)
    
    access_all=Button(newWindow2,text="Access data from primary,medical, and vaccine table",fg='black',bg='white', font=("Helvetica", 14),
              command=access_all_Window)
    access_all.place(x=555,y=300)

    access_statistics=Button(newWindow2,text="Access statistics",fg='black',bg='white', font=("Helvetica", 14),
              command=access_statistics_window)
    access_statistics.place(x=555,y=350)

    #button on main window which will lead to the 'access data page'
accessdata = Button(window, 
              text="Access data",fg='black',bg='white', font=("Helvetica", 14),
              command=createAccessWindow)
accessdata.place(x=555,y=250)

window.mainloop()
