


##########################################################--------------ADD-STUDENT-------------------------------------------------#######################################
def AddStudent():

    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%Y")
        try:
            strr='insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addedtime,addeddate))
            con.commit()
            res=messagebox.askyesnocancel('Notification','ID {} Name {} Added sucessfully.... and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                 idval.set('')
                 nameval.set('')
                 addressval.set('')
                 emailval.set('')
                 genderval.set('')
                 dobval.set('')
        except:
            messagebox.showerror('Notification','ID already exist try another id.......',parent=addroot)
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,value=vv)
            
            
    
     
        
    ##########################################
    
    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.title("Student Managment System")
    addroot.geometry('470x470+220+220')
    addroot.config(bg='blue')
    addroot.resizable(False,False)
    
    #######################ADD STUDENTS LABEL

    idlabel=Label(addroot,text='Enter Id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    idlabel.place(x=10,y=10)

    Namelabel=Label(addroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Namelabel.place(x=10,y=70)

    Mobilelabel=Label(addroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Mobilelabel.place(x=10,y=130)

    Emaillabel=Label(addroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Emaillabel.place(x=10,y=190)

    Addresslabel=Label(addroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Addresslabel.place(x=10,y=260)

    Genderlabel=Label(addroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Genderlabel.place(x=10,y=320)

    DOBlabel=Label(addroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    DOBlabel.place(x=10,y=380)

#################################################### ADD STUDENTS ENTRY

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    addressval=StringVar()
    emailval=StringVar()
    genderval=StringVar()
    dobval=StringVar()

    

    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    addressentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=190)

    emailentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=260)

    genderentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=320)

    dobentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=380)

    ################################## add button

    submitbtn=Button(addroot,text='Submit',font=('roman',15,'bold'),width=18,bd=5,activebackground='blue',activeforeground='white'
                     ,bg='red',command=submitadd)
    submitbtn.place(x=210,y=425)

    #########################################
    
    addroot.mainloop()
    
#############################################################################-----Search Student-------------------------##############################################s
    
def SearchStudent():

    def searchdata():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addeddate=time.strftime("%d/%m/%Y")
        if(id!=''):
            strr='select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,value=vv)
        elif(name!=''):
            strr='select *from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,value=vv)
        elif(mobile!=''):
            strr='select *from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,value=vv)
        elif(email!=''):
            strr='select *from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,value=vv)

        elif(address!=''):
            strr='select *from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,value=vv)

        elif(gender!=''):
            strr='select *from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,value=vv)

        elif(dob!=''):
            strr='select *from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,value=vv)

        elif(addeddate!=''):
            strr='select *from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        
        
        

    ##########################################
    
    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.title("Student Managment System")
    searchroot.geometry('470x550+220+220')
    searchroot.config(bg='skyblue')
    searchroot.resizable(False,False)
    
    #######################ADD STUDENTS LABEL

    idlabel=Label(searchroot,text='Enter Id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    idlabel.place(x=10,y=10)

    Namelabel=Label(searchroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Namelabel.place(x=10,y=70)

    Mobilelabel=Label(searchroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Mobilelabel.place(x=10,y=130)

    Emaillabel=Label(searchroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Emaillabel.place(x=10,y=190)

    Addresslabel=Label(searchroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Addresslabel.place(x=10,y=260)

    Genderlabel=Label(searchroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Genderlabel.place(x=10,y=320)

    DOBlabel=Label(searchroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    DOBlabel.place(x=10,y=380)

    Datelabel=Label(searchroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Datelabel.place(x=10,y=440)

    

#################################################### ADD STUDENTS ENTRY

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    addressval=StringVar()
    emailval=StringVar()
    genderval=StringVar()
    dobval=StringVar()

    

    identry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    addressentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=190)

    emailentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=260)

    genderentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=320)

    dobentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=380)

    dobentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=440)

    

    ################################## add button

    submitbtn=Button(searchroot,text='Search',font=('roman',15,'bold'),width=18,bd=5,activebackground='blue',activeforeground='white'
                     ,bg='red',command=searchdata)
    submitbtn.place(x=210,y=490)

    #########################################
    
    searchroot.mainloop()
    
##################################################----------------Delete Student---------------################################################################################

def DeleteStudent():
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values'][0]
    strr='delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','data corrosponding to id : {} is deleted'.format(pp))
    strr='select *from studentdata1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)
    
    

#############################################----------------------Update Student-------------------####################################################################

def UpdateStudent():
    
    
    def updatedata():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        date=dateval.get()
        time=timeval.get()

        strr='update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notification','id {} modified sucessfully'.format(id),parent=updateroot)
        strr='select *from studentdata1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,value=vv)
            
        
        
        
    ##########################################
    
    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.title("Student Managment System")
    updateroot.geometry('470x605+220+160')
    updateroot.config(bg='grey')
    updateroot.resizable(False,False)
    
    #######################ADD STUDENTS LABEL

    idlabel=Label(updateroot,text='Update Id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    idlabel.place(x=10,y=10)

    Namelabel=Label(updateroot,text='Update Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Namelabel.place(x=10,y=70)

    Mobilelabel=Label(updateroot,text='Update Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Mobilelabel.place(x=10,y=130)

    Emaillabel=Label(updateroot,text='Update Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Emaillabel.place(x=10,y=190)

    Addresslabel=Label(updateroot,text='Update Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Addresslabel.place(x=10,y=260)

    Genderlabel=Label(updateroot,text='Update Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Genderlabel.place(x=10,y=320)

    DOBlabel=Label(updateroot,text='Update D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    DOBlabel.place(x=10,y=380)

    Datelabel=Label(updateroot,text='Update Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Datelabel.place(x=10,y=440)

    Timelabel=Label(updateroot,text='Update Time:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w',width=12)
    Timelabel.place(x=10,y=500)

    
#################################################### ADD STUDENTS ENTRY

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    addressval=StringVar()
    emailval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()

    

    identry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    addressentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=190)

    emailentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=260)

    genderentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=320)

    dobentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=380)

    dateentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=440)

    timeentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=500)
    

    ################################## add button

    updatebtn=Button(updateroot,text='Update',font=('roman',15,'bold'),width=18,bd=5,activebackground='blue',activeforeground='white'
                     ,bg='red',command=updatedata)
    updatebtn.place(x=210,y=550)

    #########################################

    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        addressval.set(pp[3])
        emailval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
        
    
    updateroot.mainloop()

#################################################---------------Show Student-----------------------------------##############################################################
    


def ShowStudent():
    strr='select *from studentdata1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,value=vv)

##################################################################---------Export Student----------------------#########################################################
    
    


def ExportStudent():
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenttable.item(i)
        pp=content['value']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),
        addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['ID','Name','Mobile','Email','Address','Gender','DOB','Added date','Added time']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','Student data is saved {}'.format(paths))


def ExitStudent():
    res=messagebox.askyesnocancel('Notification','Do you want to exit')
    if(res==True):
        root.destroy()
    
    


    


#################################-----------------------connect to database----------------------------------------------###############################################

def connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passval.get()
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notification','Data is insufficiant ,please try again')
            return
        try:
            strr='create database schoolmanagmentsystem1'
            mycursor.execute(strr)
            strr='use schoolmanagmentsystem1'
            mycursor.execute(strr)
            strr='create table studentdata1(id int, name varchar(20), mobile varchar(12), email varchar(30),address varchar(50),gender varchar(5), dob varchar(50), time varchar(50),date varchar(50))'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification','Database created and now you are connected to database',parent=rootdb)
            
        except:
            strr='use schoolmanagmentsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('notification','Now you are connected to database',parent=rootdb)

        rootdb.destroy()
            
              
    rootdb=Toplevel()
    rootdb.grab_set()
    rootdb.geometry('450x250+800+230')
    rootdb.iconbitmap(r'C:/Users/Dell/Desktop/141-1417907_school-management-system-icon.ico')
    rootdb.resizable(False,False)
    rootdb.config(bg='blue')

    ##################################### connect db label
    hostlabel=Label(rootdb,text='Enter Host',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    hostlabel.place(x=10,y=10)
    
    userlabel=Label(rootdb,text='Enter User',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    userlabel.place(x=10,y=70)

    passlabel=Label(rootdb,text='Enter Password',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    passlabel.place(x=10,y=130)

    #########################creating entry fields

    hostval=StringVar()
    userval=StringVar()
    passval=StringVar()

    hostval=Entry(rootdb,font=('roman',15,'bold'),border=5,textvariable=hostval,width=15)
    hostval.place(x=250,y=10)

    userval=Entry(rootdb,font=('roman',15,'bold'),border=5,textvariable=hostval,width=15)
    userval.place(x=250,y=70)


    passval=Entry(rootdb,font=('roman',15,'bold'),border=5,textvariable=passval,width=15)
    passval.place(x=250,y=130)

    ######################################Submit button

    submitbtn=Button(rootdb,text='Submit',bd=5,font=('roman',15,'bold'),width=20,activebackground='blue',
                     activeforeground='white',command=submitdb)
    submitbtn.place(x=200,y=190)
    


    
    rootdb.mainloop()
    
    
    


################################Welcome
def IntroLabelTick():
    global text,count
    if(count>=len(ss)):
        count=-1
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
    count=count+1
    SliderLabel.after(200,IntroLabelTick)

################################Time 

def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    ClockLabel.config(text='Time:'+time_string+'\n'+'Date:'+date_string)
    ClockLabel.after(200,tick)
    
    
###############################------------------------------------Header Files-------------------------------------------##########################################################

from tkinter import *

#######################pop up window

from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
#####################

import time


###########################

import pandas   ###############for export operation

############################################################################-----------------Main Window------------------------------#############################################
root=Tk()
root.title("School Managment System")
root.config(bg='gold2')
root.geometry('1100x700+100+50')
root.iconbitmap(r'C:/Users/Dell/Desktop/141-1417907_school-management-system-icon.ico')
root.resizable(False,False)

################################################################## Frames

DataEntryFrame=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

##########=================================================Data entry frame

frontlabel=Label(DataEntryFrame,text="----------------WELCOME-----------------",font=('arial',20,'italic bold'),bg='gold2',relief=GROOVE,borderwidth=5)
frontlabel.pack(side=TOP,expand=True)



###########-------------------------------------------------------------creating Buttons

Addbtn=Button(DataEntryFrame,text="1. Add Student",font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue',activebackground='blue',relief='ridge',
              activeforeground='white',anchor='n',command=AddStudent)
Addbtn.pack(side=TOP,expand=True)

Searchbtn=Button(DataEntryFrame,text="2. Search Student",font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue',activebackground='blue',relief='ridge',
              activeforeground='white',anchor='n',command=SearchStudent)
Searchbtn.pack(side=TOP,expand=True)

Deletebtn=Button(DataEntryFrame,text="3. Delete Student",font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue',activebackground='blue',relief='ridge',
              activeforeground='white',anchor='n',command=DeleteStudent)
Deletebtn.pack(side=TOP,expand=True)

Updatebtn=Button(DataEntryFrame,text="4. Update Student",font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue',activebackground='blue',relief='ridge',
              activeforeground='white',anchor='n',command=UpdateStudent)
Updatebtn.pack(side=TOP,expand=True)

Showbtn=Button(DataEntryFrame,text="5. Show All",font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue',activebackground='blue',relief='ridge',
              activeforeground='white',anchor='n',command=ShowStudent)
Showbtn.pack(side=TOP,expand=True)

Exportbtn=Button(DataEntryFrame,text="6. Export Data",font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue',activebackground='blue',relief='ridge',
              activeforeground='white',anchor='n',command=ExportStudent)
Exportbtn.pack(side=TOP,expand=True)


Exitbtn=Button(DataEntryFrame,text="7. Exit",font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue',activebackground='blue',relief='ridge',
              activeforeground='white',anchor='n',command=ExitStudent)
Exitbtn.pack(side=TOP,expand=True)



ShowdataFrame=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
ShowdataFrame.place(x=550,y=80,width=500,height=600)

###################################################################################################################################### table show data
style=ttk.Style()
style.configure('Treeview.heading',font=('chillar',20,'bold'),foreground='blue',activebackground='grey')
style.configure('Treeview',font=('chillar',15,'bold'),foreground='black',background='cyan')

scroll_x=Scrollbar(ShowdataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowdataFrame,orient=VERTICAL)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

studenttable=Treeview(ShowdataFrame,columns=('ID','Name','Mobile No.','Email', 'Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
studenttable.pack(fill=BOTH,expand=1)

scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text="ID")
studenttable.heading('Name',text="Name")
studenttable.heading('Mobile No.',text="Mobile No.")
studenttable.heading('Email',text="Email")
studenttable.heading('Address',text="Address")
studenttable.heading('Gender',text="Gender")
studenttable.heading('D.O.B',text="D.O.B")
studenttable.heading('Added Date',text="Added Date")
studenttable.heading('Added Time',text="Added Time")

studenttable['show']='headings' ############will remove one extra added columns

studenttable.column('ID',width=100)
studenttable.column('Name',width=150)
studenttable.column('Mobile No.',width=200)
studenttable.column('Email',width=200)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=50)
studenttable.column('D.O.B',width=100)
studenttable.column('Added Date',width=100)
studenttable.column('Added Time',width=100)



###########################################################################slider

ss="WELCOME TO SCHOOL MANAGMENT SYSTEM "
count=0
text=''
#######################################

SliderLabel=Label(root,text=ss,font=('chiller',20,'italic bold'),relief=RIDGE,borderwidth=4,width=42,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()

######################################## clock

ClockLabel=Label(root,font=('chiller',20,'italic bold'),relief=RIDGE,borderwidth=4,width=20,bg='cyan')
ClockLabel.place(x=0,y=0)
tick()

######################################## Connect to database Button

databaseButton=Button(root,text='Connect to database',font=('chiller',20,'italic bold'),relief=RIDGE,
                      borderwidth=4,width=20,bg='cyan',activebackground='blue',activeforeground='white',command=connectdb)
databaseButton.place(x=800,y=0)



root.mainloop()
