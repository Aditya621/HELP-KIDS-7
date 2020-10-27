#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import*
from tkinter import messagebox
from math import*
master=Tk()
master.geometry('1600x820')
master.configure(bg='cyan')
master.title('HELP KIDS 7')
Label(master,text='HELP KIDS 7',bg='yellow',fg='green',font=("Arial Bold", 70)).place(relx=.33,rely=.0)
#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------
#--------------------------------------area of circle--------------------------------------------------------
def areaofcircle(): 
    myw = Tk() 
    myw.title("AREA OF CIRCLE") 
    myw.geometry("1600x820")
    myw.configure(bg='cyan')
    def radius():
        myw=Tk()
        myw.geometry('800x400')
        myw.configure(bg='cyan')
        myw.title("Radius Of Circle")
        ltitle=Label(myw,text="Enter data in Meter....",bg="orange",anchor="w")
        ltitle.place(x=9,y=9)
        #left frame
        lframe=Frame(myw,width=400,height=300,bg="red")
        lframe.place(x=10,y=30)
        #left label1 
        l1=Label(lframe,text="Enter Radius of circle in meter",width=25,anchor="w")
        l1.place(x=10,y=10) 
        e1=Entry(lframe,width=13)
        e1.place(x=200,y=10) 
        #left label2
        l2=Label(lframe,text="Circumference of circle in meter",width=25,anchor="w")
        l2.place(x=10,y=65)
        e2=Entry(lframe,width=13)
        e2.place(x=200,y=65)

        
        #right frame
        #this is only for showing heading 
        ltitle=Label(myw,text="Enter data in Centimeter...",bg="orange",anchor="w")
        ltitle.place(x=420,y=9)
        #right frame 
        rframe=Frame(myw,width=350,height=300,bg="red")
        rframe.place(x=420,y=30)
        #right label13
        l3=Label(rframe,text="Enter Radius of circle in centimeter",width=27,anchor="w")
        l3.place(x=10,y=10)
        e3=Entry(rframe,width=13)
        e3.place(x=215,y=10)
        #right label4
        l4=Label(rframe,text="Circumference of circle in centimeter",width=27,anchor="w")
        l4.place(x=10,y=65)
        e4=Entry(rframe,width=13)
        e4.place(x=215,y=65)
        
        
        
        def circumM():                                       #this function help us to calculate radius of curcumference in meter
            e2.delete(0,END)
            e2.insert(0,float(float(e1.get())*6.28318))     #curcumferenc=(2*pie*r)
            #messagebox.showinfo("FORMULA OF CIRCUMFERENCE","radius = "+e1.get()+ ", value of pie = 3.14")
        def circumD():                                      #this function help us to calculate diameter of curcumference in meter
            e4.delete(0,END)
            e4.insert(0,float(float(e3.get())*6.28318))    #curcumferenc=(2*pie*r)
            
            
        
        b1=Button(lframe,text="circumference(m)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumM)
        b1.place(x=10,y=35)
        b1=Button(rframe,text="circumference(cm)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumD)
        b1.place(x=10,y=35)
        
#*************************************************************************************************************************      
#-----------------------for diameter of circumference-----------------------------------------------------------------
#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------

    def diameter(): 
        myw=Tk()
        myw.geometry('800x400')
        myw.configure(bg='cyan')
        myw.title("Radius Of Circle")
        ltitle=Label(myw,text="Enter data in Meter....",bg="orange",anchor="w")
        ltitle.place(x=9,y=9)
        #left frame
        lframe=Frame(myw,width=400,height=300,bg="red")
        lframe.place(x=10,y=30)
        
        l1=Label(lframe,text="Enter Diameter of circle in meter",width=25,anchor="w")
        l1.place(x=10,y=10) 
        e1=Entry(lframe,width=13)
        e1.place(x=200,y=10) 
        
        l2=Label(lframe,text="Circumference of circle in meter",width=25,anchor="w")
        l2.place(x=10,y=65)
        e2=Entry(lframe,width=13)
        e2.place(x=200,y=65)

        
        #right frame
        
        ltitle=Label(myw,text="Enter data in Centimeter...",bg="orange",anchor="w")
        ltitle.place(x=420,y=9)
        rframe=Frame(myw,width=350,height=300,bg="red")
        rframe.place(x=420,y=30)
        
        l3=Label(rframe,text="Enter Diameter of circle in centimeter",width=27,anchor="w")
        l3.place(x=10,y=10)
        e3=Entry(rframe,width=13)
        e3.place(x=215,y=10)
        
        l4=Label(rframe,text="Circumference of circle in centimeter",width=27,anchor="w")
        l4.place(x=10,y=65)
        e4=Entry(rframe,width=13)
        e4.place(x=215,y=65)
        
        
        
        def circumM():                                      #this function help us to calculate diameter of curcumference in meter
            e2.delete(0,END)
            e2.insert(0,float(float(e1.get())*6.28318/2))   #curcumferenc=(2*pie*d)/2
            #messagebox.showinfo("FORMULA OF CIRCUMFERENCE","radius = "+e1.get()+ ", value of pie = 3.14")
        def circumD():                                      #this function help us to calculate diameter of curcumference in meter
            e4.delete(0,END)
            e4.insert(0,float(float(e3.get())*6.28318/2))   #curcumferenc=(2*pie*d)/2
        
        b1=Button(lframe,text="circumference(m)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumM)
        b1.place(x=10,y=35)
        b1=Button(rframe,text="circumference(cm)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumD)
        b1.place(x=10,y=35)
#******************************************************************************************************************************     
#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------   
#*********************** for area of circle***********************************************************************
    def radius_area():
        myw=Tk()
        myw.geometry('800x400')
        myw.configure(bg='cyan')
        myw.title("Area Of Circle")
        ltitle=Label(myw,text="Enter data in Meter....",bg="orange",anchor="w")
        ltitle.place(x=9,y=9)
        #left frame
        lframe=Frame(myw,width=400,height=300,bg="red")
        lframe.place(x=10,y=30)
        
        l1=Label(lframe,text="Enter Radius of circle in meter",width=25,anchor="w")
        l1.place(x=10,y=10) 
        e1=Entry(lframe,width=13)
        e1.place(x=200,y=10) 
        
        l2=Label(lframe,text="Area of circle in meter",width=25,anchor="w")
        l2.place(x=10,y=65)
        e2=Entry(lframe,width=13)
        e2.place(x=200,y=65)

        
        #right frame
        
        ltitle=Label(myw,text="Enter data in Centimeter...",bg="orange",anchor="w")
        ltitle.place(x=420,y=9)
        rframe=Frame(myw,width=350,height=300,bg="red")
        rframe.place(x=420,y=30)
        
        l3=Label(rframe,text="Enter Area of circle in centimeter",width=27,anchor="w")
        l3.place(x=10,y=10)
        e3=Entry(rframe,width=13)
        e3.place(x=215,y=10)
        
        l4=Label(rframe,text="Area of circle in centimeter",width=27,anchor="w")
        l4.place(x=10,y=65)
        e4=Entry(rframe,width=13)
        e4.place(x=215,y=65)
        
        def circumM():                                       #this function help us to calculate area of circle in meter
            e2.delete(0,END)
            e2.insert(0,float(float(e1.get())*float(e1.get())*3.14159))# area=pie*r*2
            #messagebox.showinfo("FORMULA OF CIRCUMFERENCE","radius = "+e1.get()+ ", value of pie = 3.14")
        def circumD():                                  #this function help us to calculate area of circle in centimeter
            e4.delete(0,END)
            e4.insert(0,float(float(e3.get())*float(e3.get())*3.14159))# area=pie*r*2
            
            
        
        b1=Button(lframe,text="Area of Circle(m)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumM)
        b1.place(x=10,y=35)
        b1=Button(rframe,text="Area of Circle(cm)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumD)
        b1.place(x=10,y=35) 

    def diameter_area(): 
        myw=Tk()
        myw.geometry('800x400')
        myw.configure(bg='cyan')
        myw.title("Radius Of Circle")
        ltitle=Label(myw,text="Enter data in Meter....",bg="orange",anchor="w")
        ltitle.place(x=9,y=9)
        #left frame
        lframe=Frame(myw,width=400,height=300,bg="red")
        lframe.place(x=10,y=30)
        
        l1=Label(lframe,text="Enter Diameter of circle in meter",width=25,anchor="w")
        l1.place(x=10,y=10) 
        e1=Entry(lframe,width=13)
        e1.place(x=200,y=10) 
        
        l2=Label(lframe,text="Area of circle in meter",width=25,anchor="w")
        l2.place(x=10,y=65)
        e2=Entry(lframe,width=13)
        e2.place(x=200,y=65)

        
        #right frame
        
        ltitle=Label(myw,text="Enter data in Centimeter...",bg="orange",anchor="w")
        ltitle.place(x=420,y=9)
        rframe=Frame(myw,width=350,height=300,bg="red")
        rframe.place(x=420,y=30)
        
        l3=Label(rframe,text="Enter Diameter of circle in centimeter",width=27,anchor="w")
        l3.place(x=10,y=10)
        e3=Entry(rframe,width=13)
        e3.place(x=215,y=10)
        
        l4=Label(rframe,text="Area of circle in centimeter",width=27,anchor="w")
        l4.place(x=10,y=65)
        e4=Entry(rframe,width=13)
        e4.place(x=215,y=65)
                    
        def circumM():                                       #this function help us to calculate area of circle in meter(diameter)
            myvar=float(float(e1.get())/2)
            e2.delete(0,END)
            e2.insert(0,float(myvar*myvar*3.14159))         # area=pie*r**2
            #messagebox.showinfo("FORMULA OF CIRCUMFERENCE","radius = "+e1.get()+ ", value of pie = 3.14")
        def circumD():                                      #this function help us to calculate area of circle in meter(diameter)
            myvar=float(float(e3.get())/2) 
            e4.delete(0,END)
            e4.insert(0,float(myvar*myvar*3.14159))            # area=pie*r**2
        
        b1=Button(lframe,text="Area of Circle(m)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumM)
        b1.place(x=10,y=35)
        b1=Button(rframe,text="Area of Circle(cm)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumD)
        b1.place(x=10,y=35)
#*******************************************************************************************************************************   
#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------
#********************** for circumference of circle***************************************************************
    def circumference():
        myw=Tk()
        myw.geometry('800x400')
        myw.configure(bg='cyan')
        myw.title("Area Of Circle")
        ltitle=Label(myw,text="Enter data in Meter....",bg="orange",anchor="w")
        ltitle.place(x=9,y=9)
        #left frame
        lframe=Frame(myw,width=400,height=300,bg="red")
        lframe.place(x=10,y=30)
        
        l1=Label(lframe,text="Enter circumference in meter",width=25,anchor="w")
        l1.place(x=10,y=10) 
        e1=Entry(lframe,width=20)
        e1.place(x=200,y=10) 
        
        l2=Label(lframe,text="Area of circle in meter",width=25,anchor="w")
        l2.place(x=10,y=65)
        e2=Entry(lframe,width=20)
        e2.place(x=200,y=65)

        
        #right frame
        
        ltitle=Label(myw,text="Enter data in Centimeter...",bg="orange",anchor="w")
        ltitle.place(x=420,y=9)
        rframe=Frame(myw,width=350,height=300,bg="red")
        rframe.place(x=420,y=30)
        
        l3=Label(rframe,text="Enter circumference in centimeter",width=27,anchor="w")
        l3.place(x=10,y=10)
        e3=Entry(rframe,width=20)
        e3.place(x=215,y=10)
        
        l4=Label(rframe,text="Area of circle in centimeter",width=27,anchor="w")
        l4.place(x=10,y=65)
        e4=Entry(rframe,width=20)
        e4.place(x=215,y=65)
        
        def circumM():                                       #this is used to calculate area of cirle when circumference is given
            myvar=(float(e1.get())*0.15909090)               # circumference=2*pie*r,  pie=3.14 and r=radius
            e2.delete(0,END)                                 #and formula is radius = (circumference*7)/(22*2)
            e2.insert(0,float(myvar*myvar*3.14159))          # area=pie*r**2
            #messagebox.showinfo("FORMULA OF CIRCUMFERENCE","radius = "+e1.get()+ ", value of pie = 3.14")
        def circumD():                                       #this is used to calculate area of cirle when circumference is given
            myvar=float(float(float(e3.get())*0.15909090))   # circumference=2*pie*r,  pie=3.14 and r=radius
            e4.delete(0,END)                                 #and formula is radius = (circumference*7)/(22*2)
            e4.insert(0,float(myvar*myvar*3.14159))          # area=pie*r**2
            
            
        
        b1=Button(lframe,text="Area of Circle(m)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumM)
        b1.place(x=10,y=35)
        b1=Button(rframe,text="Area of Circle(cm)",relief=SUNKEN,bg="cyan",highlightcolor="orange",command=circumD)
        b1.place(x=10,y=35) 
        
    #*****************************************label and button***************************************************
    Label(myw,text='AREA & CIRCUMFERENCE OF CIRCLE',font=("Calibri",25),bg='yellow',width=43).place(relx=.27,rely=.0)
    b1=Button(myw,text="Calculate Circumference of circle with radius",font=("Calibri",18),relief=SUNKEN,width=60,bg="pink",command=radius)
    b1.place(relx=.27,rely=.1)
    b2=Button(myw,text="Calculate Circumference of circle with diameter",font=("Calibri",18),relief=SUNKEN,width=60,bg="pink",command=diameter)
    b2.place(relx=.27,rely=.2)
    b3=Button(myw,text="Calculate Area of circle with Radius",font=("Calibri",18),relief=SUNKEN,width=60,bg="pink",command=radius_area)
    b3.place(relx=.27,rely=.3)
    b4=Button(myw,text="Calculate Area of circle with Diameter",font=("Calibri",18),relief=SUNKEN,width=60,bg="pink",command=diameter_area)
    b4.place(relx=.27,rely=.4)
    b5=Button(myw,text="Calculate Area of circle with Circumference when  radius is given",font=("Calibri",18),relief=SUNKEN,width=60,bg="pink",command=circumference)
    b5.place(relx=.27,rely=.5)

#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------
#------------------------------------area of triangle--------------------------------------------------------------
def areaoftriangle():

    myw=Tk()
    myw.geometry('1600x820')
    myw.configure(bg='cyan')
    myw.title('AREA OF TRIANGLE')

    
    #this is help us to create new window 
    #create frame for simplicity
    lframe=Frame(myw,width=500,height=400,bg='red')
    lframe.place(x=30,y=30)
    #create label1
    l1=Label(lframe,text="Enter Base of triangle(m) : ",width=25,bg='yellow')
    l1.place(x=5,y=5)
    #create label2
    l2=Label(lframe,text="Enter Height of triangle(m) : ",width=25,bg='yellow')
    l2.place(x=5,y=30)
    #create label3
    l3=Label(lframe,text="Area Of Triangle (m^2)  ",width=25,bg='yellow')
    l3.place(x=5,y=100)
    #create entry1
    e1=Entry(lframe)
    e1.place(x=190,y=5)
    #create entry2
    e2=Entry(lframe)
    e2.place(x=190,y=30)
    #create entry3
    e3=Entry(lframe)
    e3.place(x=190,y=100)

    def myf():                                              #this function help us to calculate area of triangle
        
        e3.delete(0,END)
        e3.insert(0,float (1/2)*float(e1.get())*float(e2.get()))
    def showt():                                             #this function help us to show the  triangle 
            myw=Tk()
            myw.geometry('1000x1000')
            myw.configure(bg='cyan')       
            myc=Canvas(myw,width=800,height=600)
            myc.place(x=10,y=10)
            if e1.get()>e2.get():
                myc.create_polygon(float(float(e1.get())/1.3),float(float(e1.get())/1.3),float(float(e2.get())*2),float(float(e2.get())*2),float(float(e1.get())/3),float(float(e2.get()))*2)
            elif e1.get()<e2.get():
                myc.create_polygon(float(e1.get()),float(e1.get()),float(float(e2.get())*1.3),float(float(e2.get())*1.3),float(float(e1.get())*1.1),float(float(e2.get()))*1.3)
            else:
                myc.create_polygon(float(e1.get()),float(e1.get()),float(float(e2.get())*1.5),float(float(e2.get())*1.5),float(float(e1.get())*0.9),float(float(e2.get()))*1.3)    
    
    #create button for clicking purpose
    b1=Button(lframe,text="answer",width=20,bg="pink",relief=SUNKEN,command=myf)
    b1.place(x=5,y=60)
    b2=Button(lframe,text="Show triangle(at most )",width=20,command=showt,bg="black",fg="white")
    b2.place(x=5,y=200)
    
#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------
#---------------------------------area of rectangle --------------------------------------------------------

def areaofreactangle():
    myw=Tk()
    myw.geometry('1600x820')
    myw.configure(bg='cyan')
    myw.title('AREA OF RECTANGLE')

    def Area_rec():
        #this is help us to create new window 
        myw=Tk()
        myw.geometry('1000x800')
        myw.configure(bg='cyan')
        #create title
        myw.title("Rectangle")
        #creating frame
        lframe=Frame(myw,width=450,height=300,bg="red")
        lframe.place(x=10,y=10)
        
    #label1
        l1=Label(lframe,text="Enter the lenght of rectangle(m)",width=25,anchor="w")
        l1.place(x=5,y=5)
        e1=Entry(lframe,width=13)
        e1.place(x=200,y=5)
    #label2
        l2=Label(lframe,text="Enter the breadth of rectangle(m)",width=25,anchor="w")
        l2.place(x=5,y=30)
        e2=Entry(lframe,width=13)
        e2.place(x=200,y=30)
    #label3
        l3=Label(lframe,text="Area of rectangle (m^2)",width=25,anchor="w")
        l3.place(x=5,y=85)
        e3=Entry(lframe,width=13)
        e3.place(x=200,y=85)

        def cal():                                                #this function help us to calculate area of rectangle
            e3.delete(0,END)
            e3.insert(0,float(float(e1.get())*float(e2.get())))
        

        b1=Button(lframe,text="calculate ",width=20,bg="darkcyan",command=cal)
        b1.place(x=5,y=55)
    #label4
        l4=Label(lframe,text="Unifrom width inside rectangle",width=25,anchor="w")
        l4.place(x=5,y=112)
        e4=Entry(lframe,width=13)
        e4.place(x=200,y=112)
    #label5
        l5=Label(lframe,text="Area of inside rectangle",width=25,anchor="w")
        l5.place(x=5,y=168)
        e5=Entry(lframe,width=13)
        e5.place(x=200,y=168)

        def inside():                                              #this function help us to calculate area of inside rectangle
            myvar1 =(float(float(e1.get())-float(e4.get())*2))
            myvar2 =(float(float(e2.get())-float(e4.get())*2))
            e5.delete(0,END)
            e5.insert(0,float(float(myvar1)*float(myvar2)))
        

        b2=Button(lframe,text="calculate inside rectangle",width=23,bg="darkcyan",command=inside,relief=SUNKEN)
        b2.place(x=5,y=137)
    #label6
        l6=Label(lframe,text="Area of foothpath",width=25,anchor="w")
        l6.place(x=5,y=225)
        e6=Entry(lframe,width=13)
        e6.place(x=200,y=225)

        def outin():                                              #this function help us to calculate area of outside rectangle
            varcal=float(float(e3.get())-float(e5.get()))
            e6.delete(0,END)
            e6.insert(0,float(varcal))
        
        
        b3=Button(lframe,text="calculate Area Of Foothpath(m^2)",width=25,bg="darkcyan",command=outin,relief=SUNKEN)
        b3.place(x=5,y=195)

        rframe=Frame(myw,width=430,height=300,bg="yellow")
        rframe.place(x=550,y=10)
        def mytri():                                               #this function help us to calculate area of foothpath of rectangle

            myc=Canvas(rframe,width=400,height=300)
            myc.place(x=5,y=30)
            myrec=myc.create_rectangle(10,120,150,220,fill="cyan")
        
            myrec=myc.create_rectangle(20,130,140,210,fill="red")
    #create button
        b1=Button(rframe,text="Show Rectangle",width=30,bg="darkcyan",command=mytri)
        b1.place(x=5,y=5)
        
#-------------------This section is madw by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------
#----------------------------------------area of rectangle------------------------------------------------------------------ 
    def Area_rectangle():
        
        myw=Tk()
        myw.geometry('1000x800')
        myw.configure(bg='cyan')
        myw.title("Rectangle")
        lframe=Frame(myw,width=450,height=300,bg="red")
        lframe.place(x=10,y=10)
        
    #label1
        l1=Label(lframe,text="Enter the lenght of rectangle(m)",width=25,anchor="w")
        l1.place(x=5,y=5)
        e1=Entry(lframe,width=13)
        e1.place(x=200,y=5)
    #label 2 
        l2=Label(lframe,text="Enter the breadth of rectangle(m)",width=25,anchor="w")
        l2.place(x=5,y=30)
        e2=Entry(lframe,width=13)
        e2.place(x=200,y=30)
    #label 3
        l3=Label(lframe,text="Area of rectangle (m^2)",width=25,anchor="w")
        l3.place(x=5,y=85)
        e3=Entry(lframe,width=13)
        e3.place(x=200,y=85)

        def cal():                                                 #this function help us to calculate a
            e3.delete(0,END)
            e3.insert(0,float(float(e1.get())*float(e2.get()))) 
            b1=Button(lframe,text="calculate ",width=20,bg="darkcyan",command=cal)
            b1.place(x=5,y=55)

        def mytri():                                                       #this function help us to show  rectangle
            #this is creating new window for showing rectangle
            myw=Tk()
            myw.geometry('1000x1000')
            myw.configure(bg='cyan')
            myw.title(" Show Rectangle")
        
            if float(e1.get())<=155 and float(e2.get())<=155:
                myc=Canvas(myw,width=900,height=700)
                myc.place(x=5,y=30)
                myc.create_rectangle(float(float(e1.get())/3),float(float(e2.get())),float(float(e1.get())*2),float(float(e2.get())*1.7),fill="#f50")
            else:
                myc=Canvas(myw,width=900,height=700)
                myc.place(x=5,y=30)
                myc.create_rectangle(float(float(e1.get())/3),float(float(e2.get())/3),float(float(e1.get())),float(float(e2.get())),fill="#fb0")

        b1=Button(lframe,text="Show Rectangle",width=20,bg="darkcyan",command=cal)
        b1.place(x=5,y=55)
        b2=Button(lframe,text="Show Rectangle",width=30,bg="darkcyan",command=mytri)
        b2.place(x=5,y=200)
    #----------------------------------------------------------------------------------------------------------
        
    Label(myw,text='AREA OF RECTANGLE',font=('calibri',18),width=60,bg='yellow').place(x=400,y=10)
    b2=Button(myw,text="Calculate Area Of Path of Rectangle ",font=("Calibri",18),width=60,height=1,bg="darkcyan",activebackground="orange",command=Area_rec)
    b2.place(x=400,y=180)
    #create button1
    b3=Button(myw,text="Calculate Area Rectangle ",font=("Calibri",18),width=60,height=1,bg="darkcyan",activebackground="orange",command=Area_rectangle)
    b3.place(x=400,y=250)
    
#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------   
#-------------------------------------profit and loss---------------------------------------------------------
def profitloss():
    myw=Tk()
    myw.geometry("500x400")
    myw.configure(bg="cyan")
    myw.title("Profit And Loss")
    #creating frame
    lframe=Frame(myw,width=400,height=300,bg="red")
    lframe.place(x=10,y=10)
    #label is used to show data
    l2=Label(lframe,text="Enter the Selling price :",width=25,anchor="w")
    l2.place(x=10,y=10)
    #entry is used to enter data in box
    e2=Entry(lframe,width=13)
    e2.place(x=200,y=10)

    l1=Label(lframe,text="Enter the Cost Price :",width=25,anchor="w")
    l1.place(x=10,y=40)
    e1=Entry(lframe,width=13)
    e1.place(x=200,y=40)
    #this is function for calculating profit and loss of given data
    def myprofit():
        e3.delete(0,END)
        if e2.get()>e1.get():
            e3.insert(0,float(float(e2.get())-float(e1.get()))*100)
            #essagebox.showinfo("because of S.P>C.P(PROFIT)","COST PRICE = "+e1.get()+ ", SELLING PRICE = "+e2.get())
        else:
            e3.insert(0,float(float(e1.get())-float(e2.get()))*100)
            #essagebox.showinfo("because of C.P>S.P (LOSE)","COST PRICE = "+e1.get()+ ", SELLING PRICE = "+e2.get())

    #this is button for clicking pourpose
    b1=Button(lframe,text="check profit and loss",relief=SUNKEN,width=18,anchor="w",bg="yellow",command=myprofit)
    b1.place(x=10,y=70)
    l3=Label(lframe,text="IN PERCENTAGE :",width=25)
    l3.place(x=10,y=100)
    e3=Entry(lframe,width=13)
    e3.place(x=200,y=100)
    
#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------   
#-------------decimal converter------------------------------------------------------------------------

def decimalconverter():

    myw=Tk()
    myw.geometry("500x400")
    myw.configure(bg="cyan")
    myw.title(" decimal  ")
    #label is used to show text in window
    l1=Label(myw,text="Enter the numinator = ",bg='yellow',anchor="w",width=26)
    l1.place(x=5,y=5)
    #entry is used to enter the user data in box
    e1=Entry(myw, width=20)
    e1.place(x=200,y=5)
    #label 2
    l2=Label(myw,text="Enter the denominator = ",bg='yellow',anchor="w",width=26)
    l2.place(x=5,y=40)
    #entry 2
    e2=Entry(myw, width=20)
    e2.place(x=200,y=40)
    #function is used for calculating data to find decimal number 
    def myd():
        e3.delete(0,END)
        e3.insert(0,float(float(e1.get())/float(e2.get())))
        
        
    #it is used for clicking purpose 
    b1=Button(myw,text="IN DECIMAL",width=10,bg='yellow',relief=SUNKEN,command=myd)
    b1.place(x=5,y=70)
    #label 3
    l3=Label(myw,text=" Number in decimal",bg='yellow',width=26,anchor="w")
    l3.place(x=5,y=100)
    #entry 3
    e3=Entry(myw,relief=SUNKEN, width=20)
    e3.place(x=200,y=100)

#-------------------This section is made by Aditya Singh(11906040),section(K19PD),Roll no.(B39)--------------------------------   
#--------------------simple intrest---------------------------------------------------------------------

def simpleintrest():
    myw=Tk()
    myw.geometry("700x400")
    myw.configure(bg="cyan")
    #frame
    lframe=Frame(myw,width=550,height=200,bg='red')
    lframe.place(x=30,y=30)
#label and entry
    l1=Label(lframe,text="Enter the principal value: ",width=25,anchor="w")
    l1.place(x=5,y=5)
    e1=Entry(lframe,width=10)
    e1.place(x=200,y=5)
#label2
    l2=Label(lframe,text="Enter the Rate in %: ",width=25,anchor="w")
    l2.place(x=5,y=30)
    e2=Entry(lframe,width=10)
    e2.place(x=200,y=30)
#label3
    l3=Label(lframe,text="Enter the Time : ",width=25,anchor="w")
    l3.place(x=5,y=55)
    e3=Entry(lframe,width=10)
    e3.place(x=200,y=55)
#label5
    l5=Label(lframe,text="Time is Convert into year : ",width=25,anchor="w")
    l5.place(x=5,y=80)
    e5=Entry(lframe,width=10)
    e5.place(x=200,y=80)
#label4
    l4=Label(lframe,text="your answer is : ",width=25,anchor="w")
    l4.place(x=5,y=150)
    e4=Entry(lframe,width=10)
    e4.place(x=200,y=150)
    #function

    def myanswer():                                                                    #this show the final answer
        e4.delete(0,END)
        e4.insert(0,float(float(e1.get())*float(e2.get())*float(e5.get())/100))            

    def myH():                                                                           #this is for calculating value in hours
        e5.delete(0,END)
        e5.insert(0,float(e3.get()))
        
    def myM():                                                                      #this is for calculating value in minutes
        e5.delete(0,END)
        e5.insert(0,float(float(e3.get())/12))
        
    def myD():                                                                         #this is for calculating value in minutes
        e5.delete(0,END)
        e5.insert(0,float(float(e3.get())/365))
    
    def myW():                                                                        #this is for calculating value in weeks
        e5.delete(0,END)
        e5.insert(0,float(float(e3.get())/52))
    
#BUTTON is used for clicking purpose
    b1=Button(lframe,text="Click Me For S.I",width=20,relief=SUNKEN,bg="cyan",command=myanswer)
    b1.place(x=5,y=120)
    btM=Button(lframe,text="MONTH'S",width=7,relief=SUNKEN,bg="yellow",command=myM)
    btM.place(x=270,y=55)
    btD=Button(lframe,text="DAYS",width=5,relief=SUNKEN,bg="cyan",command=myD)
    btD.place(x=335,y=55)
    btW=Button(lframe,text="WEEKS",width=6,relief=SUNKEN,bg="cyan",command=myW)
    btW.place(x=385,y=55)
    btH=Button(lframe,text="HOUR'S",width=6,relief=SUNKEN,bg="cyan",command=myH)
    btH.place(x=450,y=55)

#-------------------This section is made by Ankit Kumar Singh(11910439) section (RK19PD) roll no.(58)-----------------------
#probablity----------------------------------------------------------------------------------------

def probablity():

    myw=Tk()
    myw.geometry('400x300')
    myw.configure(bg='blue')
    myw.title('Probability')
    l1=Label(myw,text='enter no of possible outcomes',width=25)
    l1.grid(row=0)
    l2=Label(myw,text='enter no of favourable outcomes',width=25)
    l2.grid(row=1)
    l3=Label(myw,text='result',width=20)
    l3.grid(row=2)
    e1=Entry(myw)
    e2=Entry(myw)
    e3=Entry(myw)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    def prob():
        e3.delete(0,END)
        e3.insert(0,float(e1.get())//float(e2.get()))
    b1=Button(myw,text='probablity',width=7,command=prob)
    b1.grid(row=3,column=0)

#-------------------This section is made by Ankit Kumar Singh(11910439) section (RK19PD) roll no.(58)------------------------
#---------------------pythogoras theoram------------------------------------------------------------

def pythogoras():
    
    myw=Tk()
    myw.geometry('600x400')
    myw.configure(bg='blue')
    myw.title('Pythagoras theorem')
    hframe=Frame(myw,height=400,width=400,bg='cyan')
    hframe.grid(row=0)
    pframe=Frame(myw,height=400,width=400,bg='cyan')
    pframe.grid(row=0,column=1)
    bframe=Frame(myw,height=400,width=400,bg='cyan')
    bframe.grid(row=1,column=0)
    #----------------------------hypotenuse-----------------------------------------
    l1=Label(hframe,text='enter perpendicular',width=20)
    l1.grid(row=0)
    l2=Label(hframe,text='enter base',width=20)
    l2.grid(row=1)
    l3=Label(hframe,text='hypotenuse',width=20)
    l3.grid(row=2)
    e1=Entry(hframe)
    e2=Entry(hframe)
    e3=Entry(hframe)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    def pyth():
        e3.delete(0,END)
        e3.insert(0,float(pow((float(e1.get())*float(e1.get()))+(float(e2.get())*float(e2.get())),1/2)))
    b=Button(hframe,text='result',width=7,command=pyth)
    b.grid(row=3,column=0)
    #---------------------------perpendicular----------------------------------------------
    lp1=Label(pframe,text='enter hypotenuse',width=20)
    lp1.grid(row=0)
    lp2=Label(pframe,text='enter base',width=20)
    lp2.grid(row=1)
    lp3=Label(pframe,text='perpendicular',width=20)
    lp3.grid(row=2)
    ep1=Entry(pframe)
    ep2=Entry(pframe)
    ep3=Entry(pframe)
    ep1.grid(row=0,column=1)
    ep2.grid(row=1,column=1)
    ep3.grid(row=2,column=1)
    def pyth():
        ep3.delete(0,END)
        ep3.insert(0,float(pow((float(e1.get())*float(e1.get()))-(float(e2.get())*float(e2.get())),1/2)))
    bp=Button(pframe,text='result',width=7,command=pyth)
    bp.grid(row=3,column=0)
    #------------------------------------------base-----------------------------
    lb1=Label(bframe,text='enter hypotenuse',width=20)
    lb1.grid(row=0)
    lb2=Label(bframe,text='enter perpendicular',width=20)
    lb2.grid(row=1)
    lb3=Label(bframe,text='base',width=20)
    lb3.grid(row=2)
    eb1=Entry(bframe)
    eb2=Entry(bframe)
    eb3=Entry(bframe)
    eb1.grid(row=0,column=1)
    eb2.grid(row=1,column=1)
    eb3.grid(row=2,column=1)
    def pyth():
        eb3.delete(0,END)
        eb3.insert(0,float(pow((float(e1.get())*float(e1.get()))-(float(e2.get())*float(e2.get())),1/2)))
    bb=Button(bframe,text='result',width=7,command=pyth)
    bb.grid(row=3,column=0)
    
#-------------------This section is made by Ankit Kumar Singh(11910439) section (RK19PD) roll no.(58)------------------------
#-------------------This section is made by Rakesh Kumar jani (11905956) section (RK19PD) roll no.(25)------------
#-------------------------------LCM-------------------------------------------------------------------

def lcm():
    myw=Tk()
    myw.geometry('400x300')
    myw.configure(bg='blue')
    myw.title('LCM')
    l1=Label(myw,text='enter first number',width=20,bg='cyan')
    l1.grid(row=0)
    l2=Label(myw,text='enter second number',width=20,bg='cyan')
    l2.grid(row=1)
    l3=Label(myw,text='LCM',width=20,bg='cyan')
    l3.grid(row=2)
    e1=Entry(myw)
    e2=Entry(myw)
    e3=Entry(myw)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    def gcd():
        e3.delete(0,END)
        a=float(e1.get())
        b=float(e2.get())
        if(a>b):
            max=a
        else:
            max=b
        while(1):
            if(max%a==0 and max%b==0):
                e3.insert(0,max)
                break
            max=max+1   
        
    b1=Button(myw,text='LCM',width=7,command=gcd)
    b1.grid(row=3,column=0)
    
#-------------------This section is made by Rakesh Kumar jani (11905956) section (RK19PD) roll no.(25)------------
#----------------------------EXPONENTS AND POWER-------------------------------------------------------
#These all button(b1,b2,b3,b4,b5)is done by Rakesh Kumar jani (11905956) section (RK19PD) roll no.(25)------------
def exponents():
    myw=Tk()
    myw.geometry('1600x820')
    myw.configure(bg='cyan')
    myw.title('EXPONENTS AND POWERS')
    Label(myw,text='EXPONENTS AND POWER',width=25,font=('Calibri',35),bg='yellow').place(x=480,y=10)

    def but1():
        myw=Tk()
        myw.geometry('400x300')
        myw.configure(bg='cyan')
        myw.title('a^m x a^n = a^(m+n)')
        Label(myw,text='enter a',font=('Calibri',13),width=10).place(x=10,y=10)
        Label(myw,text='enter m',font=('Calibri',13),width=10).place(x=10,y=40)
        Label(myw,text='enter n',font=('Calibri',13),width=10).place(x=10,y=70)
        Label(myw,text='a^(m+n)',font=('calibri',13),width=10).place(x=10,y=100)
        e1=Entry(myw,width=10)
        e2=Entry(myw,width=10)
        e3=Entry(myw,width=10)
        e4=Entry(myw,width=10)
        e1.place(x=120,y=10)
        e2.place(x=120,y=40)
        e3.place(x=120,y=70)
        e4.place(x=120,y=100)
        def p1():
            e4.delete(0,END)
            a=float(e1.get())
            m=float(e2.get())
            n=float(e3.get())

            e4.insert(0,pow(a,m+n))
        Button(myw,text='result',font=('calibri',13),width=10,bg='yellow',command=p1).place(x=10,y=130)
    #------------------------------------b2---------------------------------------------
#-------------------This section is made by Rakesh Kumar jani (11905956) section (RK19PD) roll no.(25)------------
    def but2():
        myw=Tk()
        myw.geometry('400x300')
        myw.configure(bg='cyan')
        myw.title('a^m / a^n = a^(m-n)')
        Label(myw,text='enter a',font=('Calibri',13),width=10).place(x=10,y=10)
        Label(myw,text='enter m',font=('Calibri',13),width=10).place(x=10,y=40)
        Label(myw,text='enter n',font=('Calibri',13),width=10).place(x=10,y=70)
        Label(myw,text='a^(m-n)',font=('calibri',13),width=10).place(x=10,y=100)
        e1=Entry(myw,width=10)
        e2=Entry(myw,width=10)
        e3=Entry(myw,width=10)
        e4=Entry(myw,width=10)
        e1.place(x=120,y=10)
        e2.place(x=120,y=40)
        e3.place(x=120,y=70)
        e4.place(x=120,y=100)
        def p1():
            e4.delete(0,END)
            a=float(e1.get())
            m=float(e2.get())
            n=float(e3.get())

            e4.insert(0,pow(a,m-n))
        Button(myw,text='result',font=('calibri',13),width=10,bg='yellow',command=p1).place(x=10,y=130)
    #-------------------------------b3----------------------------------------------------------------
    def but3():
        myw=Tk()
        myw.geometry('400x300')
        myw.configure(bg='cyan')
        myw.title('(a^m)^n = a^(m x n)')
        Label(myw,text='enter a',font=('Calibri',13),width=10).place(x=10,y=10)
        Label(myw,text='enter m',font=('Calibri',13),width=10).place(x=10,y=40)
        Label(myw,text='enter n',font=('Calibri',13),width=10).place(x=10,y=70)
        Label(myw,text='a^(m x n)',font=('calibri',13),width=10).place(x=10,y=100)
        e1=Entry(myw,width=10)
        e2=Entry(myw,width=10)
        e3=Entry(myw,width=10)
        e4=Entry(myw,width=10)
        e1.place(x=120,y=10)
        e2.place(x=120,y=40)
        e3.place(x=120,y=70)
        e4.place(x=120,y=100)
        def p1():
            e4.delete(0,END)
            a=float(e1.get())
            m=float(e2.get())
            n=float(e3.get())

            e4.insert(0,pow(a,m*n))
        Button(myw,text='result',font=('calibri',13),width=10,bg='yellow',command=p1).place(x=10,y=130)
    #----------------------------------------b4---------------------------------------------------------

    def but4():
        myw=Tk()
        myw.geometry('400x300')
        myw.configure(bg='cyan')
        myw.title('(axb)^n = a^n x b^n')
        Label(myw,text='enter a',font=('Calibri',13),width=10).place(x=10,y=10)
        Label(myw,text='enter b',font=('Calibri',13),width=10).place(x=10,y=40)
        Label(myw,text='enter n',font=('Calibri',13),width=10).place(x=10,y=70)
        Label(myw,text='a^n x b^n',font=('calibri',13),width=10).place(x=10,y=100)
        e1=Entry(myw,width=10)
        e2=Entry(myw,width=10)
        e3=Entry(myw,width=10)
        e4=Entry(myw,width=10)
        e1.place(x=120,y=10)
        e2.place(x=120,y=40)
        e3.place(x=120,y=70)
        e4.place(x=120,y=100)
        def p1():
            e4.delete(0,END)
            a=float(e1.get())
            b=float(e2.get())
            n=float(e3.get())

            e4.insert(0,pow(a,n)*pow(b,n))
        Button(myw,text='result',font=('calibri',13),width=10,bg='yellow',command=p1).place(x=10,y=130)
    #-------------------------------------but5--------------------------------------------------------
    def but5():
        myw=Tk()
        myw.geometry('400x300')
        myw.configure(bg='cyan')
        myw.title('(a/b)^n = a^n / b^n')
        Label(myw,text='enter a',font=('Calibri',13),width=10).place(x=10,y=10)
        Label(myw,text='enter b',font=('Calibri',13),width=10).place(x=10,y=40)
        Label(myw,text='enter n',font=('Calibri',13),width=10).place(x=10,y=70)
        Label(myw,text='a^n / b^n',font=('calibri',13),width=10).place(x=10,y=100)
        e1=Entry(myw,width=10)
        e2=Entry(myw,width=10)
        e3=Entry(myw,width=10)
        e4=Entry(myw,width=10)
        e1.place(x=120,y=10)
        e2.place(x=120,y=40)
        e3.place(x=120,y=70)
        e4.place(x=120,y=100)
        def p1():
            e4.delete(0,END)
            a=float(e1.get())
            b=float(e2.get())
            n=float(e3.get())

            e4.insert(0,pow(a,n)/pow(b,n))
        Button(myw,text='result',font=('calibri',13),width=10,bg='yellow',command=p1).place(x=10,y=130)



    b1=Button(myw,text='a^m x a^n = a^(m+n)',width=30,font=('Calibri',18),command=but1).place(x=590,y=110)
    b2=Button(myw,text='a^m / a^n = a^(m-n)',width=30,font=('Calibri',18),command=but2).place(x=590,y=190)
    b3=Button(myw,text='(a^m)^n = a^(m x n)',width=30,font=('Calibri',18),command=but3).place(x=590,y=270)
    b4=Button(myw,text='(axb)^n = a^n x b^n',width=30,font=('Calibri',18),command=but4).place(x=590,y=350)
    b5=Button(myw,text='(a/b)^n = a^n / b^n',width=30,font=('Calibri',18),command=but5).place(x=590,y=430)

#-----------------------------info button---------------------------------------------------
#-------------------This section is made by Aditya Singh (11906040) section (RK19PD) roll no.(39)---------
def mybutton():
    messagebox.showinfo("information of devloper ","1. Name = Aditya Singh(39),Registration No.=11906040  2.Name = Rakesh Kumar jani(25),Registration No.=11905956 3.Name = Ankit Kumar Singh(58),Registration No.=11910439")

#--------------------master buttons---------------------------------------------------------------------
    
b1=Button(master,text='AREA OF CIRCLE',width=30,font=("Calibri",18),command=areaofcircle).place(x=80,y=200)
b2=Button(master,text='AREA OF TRIANGLE',width=30,font=("Calibri",18),command=areaoftriangle).place(x=80,y=300)
b3=Button(master,text='SIMPLE INTREST',width=30,font=("Calibri",18),command=simpleintrest).place(x=80,y=400)
b4=Button(master,text='AREA OF RECTANGLE',width=30,font=("Calibri",18),command=areaofreactangle).place(x=80,y=500)
b5=Button(master,text='PROFIT AND LOSS',width=30,font=("Calibri",18),command=profitloss).place(x=80,y=600)
b6=Button(master,text='LCM',width=30,font=("Calibri",18),command=lcm).place(x=1070,y=200)
b7=Button(master,text='PYTHOGORAS THEORAM',width=30,font=("Calibri",18),command=pythogoras).place(x=1070,y=300)
b8=Button(master,text='PROBABLITY',width=30,font=("Calibri",18),command=probablity).place(x=1070,y=400)
b9=Button(master,text='DECIMAL CONVERTER',width=30,font=("Calibri",18),command=decimalconverter).place(x=1070,y=500)
b10=Button(master,text='EXPONENTS AND POWER',width=30,font=("Calibri",18),command=exponents).place(x=1070,y=600)
sb=Button(master,text="DEVLOPER INFO",width=15,bg='dark cyan',font=("Calibri",15),command=mybutton).place(x=700,y=720)
master.mainloop()


# In[ ]:





# In[ ]:




