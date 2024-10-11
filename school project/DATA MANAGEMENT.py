from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import csv
##==========================================================================================================================================================##
                                           #MARKSHEET#
##==========================================================================================================================================================##
def mark():
    def calculate():
        global a
        a=ph.get()+ch.get()+ma.get()+en.get()+cs.get()
        to.set(str(a))
        per()
        grade()

    def per():
        global p1
        p1=a/5
        tt.set(str(p1))

    def grade():
        if p1>=90:
            g.set("A")
        elif p1>=80:
            g.set("B")
        elif p1>=70:
            g.set("C")
        elif p1>=60:
            g.set("D")
        elif p1<40:
            g.set("E")
        else:
            g.set("FAIL")
            
    def exit1():
        root.destroy()
        data_management()
        

    ##=====================
    def load():
         try:
              employees=open("D:\\PROJECT\\marksheet.csv","r")
              data=csv.reader(employees)
              for a in data:
                   trv.insert("",'end',values=(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13]))
         except:
              pass

    def add():
        employees=open("D:\\PROJECT\\marksheet.csv","r")
        count=0
        data=csv.reader(employees)
        for d in data:
            if d[0]==ro.get():
                count=count+1
        employees.close()
        if count==0:
            add_data()   
        else:
            messagebox.showinfo("Error"," ID already exist")
            
        
    def add_data():
        aa=n.get()
        bb=fn.get()
        cc=mob.get()
        dd=ro.get()
        ee=cl.get()
        ff=se.get()
        hh=ph.get()
        ii=ch.get()
        jj=ma.get()
        kk=en.get()
        ll=cs.get()
        mm=to.get()
        nn=tt.get()
        oo=g.get()
        i=1
        i=i+1
        trv.insert("",'end',values=(dd,aa,bb,cc,ee,ff,hh,ii,jj,kk,ll,mm,nn,oo))
        employees=open("D:\\PROJECT\\marksheet.csv","a",newline="")
        writer=csv.writer(employees)
        writer.writerow([dd,aa,bb,cc,ee,ff,hh,ii,jj,kk,ll,mm,nn,oo])
        employees.close()
        n.set("")
        fn.set("")
        mob.set("")
        ro.set("")
        cl.set("")
        se.set("")
        sea.set("")
        ph.set("0")
        ch.set("0")
        ma.set("0")
        en.set("0")
        cs.set("0")
        to.set("")
        tt.set("")
        g.set("")
             
    def clear():
        n.set("")
        fn.set("")
        mob.set("")
        ro.set("")
        cl.set("")
        se.set("")
        sea.set("")
        ph.set("0")
        ch.set("0")
        ma.set("0")
        en.set("0")
        cs.set("0")
        to.set("")
        tt.set("")
        g.set("")

    def update():
        employees=open("D:\\PROJECT\\marksheet.csv","r")
        count=0
        data=csv.reader(employees)
        for d in data:
            if d[0]==ro.get():
                count=count+1
        employees.close()
        if count==1:
            edit()        
        else:
            messagebox.showinfo("Error"," ID already exist")
    
    def edit():
       # Get selected item to Edit
       selected_item=trv.selection()
       item = trv.item(selected_item)
       values=item['values']
       if len(values)>0:
            selected_item = trv.selection()[0]
            aa=n.get()
            bb=fn.get()
            cc=mob.get()
            dd=ro.get()
            ee=cl.get()
            ff=se.get()
            hh=ph.get()
            ii=ch.get()
            jj=ma.get()
            kk=en.get()
            ll=cs.get()
            mm=to.get()
            nn=tt.get()
            oo=g.get() 
            trv.item(selected_item, text="blub", values=(dd,aa,bb,cc,ee,ff,hh,ii,jj,kk,ll,mm,nn,oo))
            emp=open("D:\\PROJECT\\marksheet.csv","w",newline="")
            writer=csv.writer(emp)
            listOfEntriesInTreeView=trv.get_children()
            for each in listOfEntriesInTreeView:
                 writer.writerow(trv.item(each)['values'])
            emp.close()
       else:
            messagebox.showinfo("Warning","No data to update")   
    def getedit(event):
         selected_item=trv.selection()
         item = trv.item(selected_item)
         values=item['values']
         if len(values)>0:
             ro.set(values[0])
             n.set(values[1])
             fn.set(values[2])
             mob.set(values[3])
             cl.set(values[4])
             se.set(values[5])
             ph.set(values[6])
             ch.set(values[7])
             ma.set(values[8])
             en.set(values[9])
             cs.set(values[10])
             to.set(values[11])
             tt.set(values[12])
             g.set(values[13])
              
         else:
              pass

    def clear_all():
        for item in trv.get_children():
            trv.delete(item)

    def show_all():
        clear_all()
        load()

        
    def show():
        employees=open("D:\\PROJECT\\marksheet.csv","r")
        data=csv.reader(employees)
        for a in data:
            if sea.get()!="":
                if sea.get() in a:
                    clear_all()
                    trv.insert("",'end',values=(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13]))
                    sea.set("")
        employees.close()

    def del_item():
         selected_item=trv.selection()
         item = trv.item(selected_item)
         values=item['values']
         if len(values)>0:
              selected_item = trv.selection()[0]
              trv.delete(selected_item)
              clear()
              emp=open("D:\\PROJECT\\marksheet.csv","w",newline="")
              writer=csv.writer(emp)
              listOfEntriesInTreeView=trv.get_children()
              for each in listOfEntriesInTreeView:
                   writer.writerow(trv.item(each)['values'])   
         else:
            messagebox.showinfo("Warning","No data to delete")
    ##========================
    root=Tk()
    root.title("MARKSHEET")
    ##root.geometry("1600x900+0+0")
    root.configure(bg="white")
    root.attributes('-fullscreen',True)
    font=("time new roman",8,"bold")
    bg="white"

    n=StringVar()
    fn=StringVar()
    mob=StringVar()
    ro=StringVar()
    cl=StringVar()
    se=StringVar()
    sea=StringVar()
    ph=IntVar()
    ch=IntVar()
    ma=IntVar()
    en=IntVar()
    cs=IntVar()
    to=IntVar()
    tt=IntVar()
    g=StringVar()

    title=Label(root,text="MARKSHEET",font=("time new roman",20,"bold"),bg=bg,fg="red")
    title.place(x=550,y=0)

    p_frame=Frame(root,width=1240,height=160,bd=10,relief=GROOVE,bg=bg)
    p_frame.place(x=20,y=60)

    name=Label(p_frame,text="NAME",font=font,bg=bg,fg="red")
    name.place(x=40,y=20)
    name_entry=Entry(p_frame,font=font,textvariable=n,bd=5,relief=GROOVE)
    name_entry.place(x=220,y=20)

    f_name=Label(p_frame,text="FATHER NAME",font=font,bg=bg,fg="red")
    f_name.place(x=40,y=60)
    f_name_entry=Entry(p_frame,font=font,textvariable=fn,bd=5,relief=GROOVE)
    f_name_entry.place(x=220,y=60)

    mo=Label(p_frame,text="MOBILE NO.",font=font,bg=bg,fg="red")
    mo.place(x=40,y=100)
    mo_entry=Entry(p_frame,font=font,textvariable=mob,bd=5,relief=GROOVE)
    mo_entry.place(x=220,y=100)

    r=Label(p_frame,text="ROLL NO.",font=font,bg=bg,fg="red")
    r.place(x=800,y=20)
    r_entry=Entry(p_frame,font=font,textvariable=ro,bd=5,relief=GROOVE)
    r_entry.place(x=940,y=20)

    c=Label(p_frame,text="CLASS",font=font,bg=bg,fg="red")
    c.place(x=800,y=60)
    c_entry=Entry(p_frame,font=font,textvariable=cl,bd=5,relief=GROOVE)
    c_entry.place(x=940,y=60)

    s=Label(p_frame,text="SEC",font=font,bg=bg,fg="red")
    s.place(x=800,y=100)
    s_entry=Entry(p_frame,font=font,textvariable=se,bd=5,relief=GROOVE)
    s_entry.place(x=940,y=100)

    m_frame=Frame(root,width=1240,height=530,relief=GROOVE,bg=bg,bd=5)
    m_frame.place(x=20,y=225)

    s_frame=LabelFrame(m_frame,text="SUBJECT",width=200,height=300,bg=bg,fg="red",font=font)
    s_frame.place(x=2,y=2)

    p=Label(s_frame,text="PHYSICS",font=font,bg=bg,fg="red")
    p.place(x=10,y=10)
    p_entry=Entry(s_frame,font=font,textvariable=ph,bd=5,relief=GROOVE,width=5)
    p_entry.place(x=120,y=10)

    c=Label(s_frame,text="CHEMISTRY",font=font,bg=bg,fg="red")
    c.place(x=10,y=60)
    c_entry=Entry(s_frame,font=font,textvariable=ch,bd=5,relief=GROOVE,width=5)
    c_entry.place(x=120,y=60)

    m=Label(s_frame,text="MATH",font=font,bg=bg,fg="red")
    m.place(x=10,y=110)
    m_entry=Entry(s_frame,font=font,textvariable=ma,bd=5,relief=GROOVE,width=5)
    m_entry.place(x=120,y=110)

    e=Label(s_frame,text="ENGLISH",font=font,bg=bg,fg="red")
    e.place(x=10,y=160)
    e_entry=Entry(s_frame,font=font,textvariable=en,bd=5,relief=GROOVE,width=5)
    e_entry.place(x=120,y=160)

    cb=Label(s_frame,text="CS/BIO",font=font,bg=bg,fg="red")
    cb.place(x=10,y=210)
    cb_entry=Entry(s_frame,font=font,textvariable=cs,bd=5,relief=GROOVE,width=5)
    cb_entry.place(x=120,y=210)

    b_frame=LabelFrame(m_frame,text="BUTTON",width=330,height=80,bg=bg,fg="red",font=font)
    b_frame.place(x=530,y=420)
    t_b=Button(b_frame,text="TOTAL",bg=bg,font=("time new roman",5,"bold"),command=calculate).place(x=10,y=5)
    a_b=Button(b_frame,text="ADD",bg=bg,font=("time new roman",5,"bold"),command=add).place(x=90,y=5)
    u_b=Button(b_frame,text="UPDATE",bg=bg,font=("time new roman",5,"bold"),command=update).place(x=160,y=5)
    e_b=Button(b_frame,text="EXIT",bg=bg,font=("time new roman",5,"bold"),command=exit1).place(x=250,y=5)

    c_frame=LabelFrame(m_frame,text="CALCULATE",width=520,height=80,bg=bg,fg="red",font=font)
    c_frame.place(x=2,y=420)
    t=Label(c_frame,text="TOTAL",font=font,bg=bg,fg="red")
    t.place(x=10,y=5)
    t_entry=Entry(c_frame,textvariable=to,bd=5,relief=GROOVE,width=5,font=font)
    t_entry.place(x=80,y=5)
    p=Label(c_frame,text="PERCENTAGE",font=font,bg=bg,fg="red")
    p.place(x=160,y=5)
    p_entry=Entry(c_frame,textvariable=tt,bd=5,relief=GROOVE,width=5,font=font)
    p_entry.place(x=280,y=5)
    p=Label(c_frame,text="GRADE",font=font,bg=bg,fg="red")
    p.place(x=360,y=5)
    p_entry=Entry(c_frame,textvariable=g,bd=5,relief=GROOVE,width=5,font=font)
    p_entry.place(x=430,y=5)


    s_frame=LabelFrame(m_frame,text="SEARCH",width=340,height=80,bg=bg,fg="red",font=font)
    s_frame.place(x=880,y=420)
    t_entry=Entry(s_frame,textvariable=sea,bd=5,relief=GROOVE,width=8,font=font)
    t_entry.place(x=10,y=5)
    t_b=Button(s_frame,text="SEARCH",bg=bg,font=("time new roman",5,"bold"),command=show).place(x=120,y=5)
    t_b=Button(s_frame,text="SEARCH ALL",bg=bg,font=("time new roman",5,"bold"),command=show_all).place(x=220,y=5)

    f4=LabelFrame(m_frame,relief=GROOVE,bd=5,bg=bg,font=font)
    f4.place(x=210,y=10,width=1010,height=400)
    trv=ttk.Treeview(f4,selectmode='browse',height=12)
    trv.grid(row=0,column=0)
    trv["columns"]=("1","2","3","4","5","6","7","8","9","10","11","12","13","14")
    trv['show']='headings'
    trv.column("1",width=80,anchor='c')
    trv.column("2",width=100,anchor='c')
    trv.column("3",width=120,anchor='c')
    trv.column("4",width=120,anchor='c')
    trv.column("5",width=60,anchor='c')
    trv.column("6",width=50,anchor='c')
    trv.column("7",width=60,anchor='c')
    trv.column("8",width=60,anchor='c')
    trv.column("9",width=60,anchor='c')
    trv.column("10",width=60,anchor='c')
    trv.column("11",width=70,anchor='c')
    trv.column("12",width=70,anchor='c')
    trv.column("13",width=60,anchor='c')
    trv.column("14",width=30,anchor='c')
    trv.heading("1",text="ROLL NO")
    trv.heading("2",text="Name")
    trv.heading("3",text="FATHER NAME")
    trv.heading("4",text="MOB.NO")
    trv.heading("5",text="CLASS")
    trv.heading("6",text="SEC")
    trv.heading("7",text="PHY")
    trv.heading("8",text="CHE")
    trv.heading("9",text="MATH")
    trv.heading("10",text="ENG")
    trv.heading("11",text="CS/BIO")
    trv.heading("12",text="TOTAL")
    trv.heading("13",text="PER")
    trv.heading("14",text="GR")
    load()
    trv.bind('<<TreeviewSelect>>', getedit)

    d_button=Button(m_frame,text="DELETE",bg=bg,font=("time new roman",5,"bold"),command=del_item).place(x=20,y=340)
    dc_button=Button(m_frame,text="CLEAR",bg=bg,font=("time new roman",5,"bold"),command=clear).place(x=120,y=340)

    exit_img=PhotoImage(file="D:\\PROJECT\\exit icon.png",master=root)
    destroy_b=Button(root,text="destroy",command=exit1,image=exit_img).place(x=1230,y=6)
    root.mainloop()

##==========================================================================================================================================================##
                                           #STUDENT RECORD#
##==========================================================================================================================================================##
def student():
    def fn():
         r_e.focus()
    def load():
         try:
              employees=open("D:\\PROJECT\\student detail.csv","r")
              data=csv.reader(employees)
              for a in data:
                   trv.insert("",'end',values=(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
         except:
              pass

    def add():
        employees=open("D:\\PROJECT\\student detail.csv","r")
        count=0
        data=csv.reader(employees)
        for d in data:
            if d[0]==roll_no.get():
                count=count+1
        employees.close()
        if count==0:
            add_data()   
        else:
            messagebox.showinfo("Error"," ID already exist")
            
    def add_data():
         roll=roll_no.get() 
         name1=name.get()    
         f=f_name.get()
         g=gender.get()
         y=ye.get()
         c=co_n.get()
         a=a_d.get()
         o=options.get()
         i=1
         i=i+1
         if roll!="":
             trv.insert("",'end',values=(roll,name1,f,g,o,y,c,a))
             employees=open("D:\\PROJECT\\student detail.csv","a",newline="")
             writer=csv.writer(employees)
             writer.writerow([roll,name1,f,g,o,y,c,a])
             employees.close()
             roll_no.set("") 
             name.set("")    
             f_name.set("")
             gender.set("")
             ye.set("")
             co_n.set("")
             a_d.set("")
             options.set("")
    def clear():
         roll_no.set("") 
         name.set("")    
         f_name.set("")
         gender.set("")
         ye.set("")
         co_n.set("")
         a_d.set("")
         options.set("")
         fn()

    def update():
        employees=open("D:\\PROJECT\\student detail.csv","r")
        count=0
        data=csv.reader(employees)
        for d in data:
            if d[0]==roll_no.get():
                count=count+1
        employees.close()
        if count==1:
            edit()        
        else:
            messagebox.showinfo("Error"," ID already exist")
    def edit():
       # Get selected item to Edit
       selected_item=trv.selection()
       item = trv.item(selected_item)
       values=item['values']
       if len(values)>0:
            selected_item = trv.selection()[0]
            roll=roll_no.get()
            name1=name.get()
            f=f_name.get()
            g=gender.get()
            y=ye.get()
            c=co_n.get()
            a=a_d.get()
            o=options.get()
            trv.item(selected_item, text="blub", values=(roll,name1,f,g,o,y,c,a))
            emp=open("D:\\PROJECT\\student detail.csv","w",newline="")
            writer=csv.writer(emp)
            listOfEntriesInTreeView=trv.get_children()
            for each in listOfEntriesInTreeView:
                 writer.writerow(trv.item(each)['values'])
            emp.close()
       else:
            messagebox.showinfo("Warning","No data to update")   
    def getedit(event):
         selected_item=trv.selection()
         item = trv.item(selected_item)
         values=item['values']
         if len(values)>0:
              roll_no.set(values[0])
              name.set(values[1])
              f_name.set(values[2])
              gender.set(values[3])
              options.set(values[4])
              ye.set(values[5])
              co_n.set(values[6])
              a_d.set(values[7])
              
         else:
              pass
    def destroy1():
         root.destroy()
         data_management()

    def clear_all():
        for item in trv.get_children():
            trv.delete(item)

    def show_all():
        clear_all()
        load()

        
    def show():
        employees=open("D:\\PROJECT\\student detail.csv","r")
        data=csv.reader(employees)
        for a in data:
            if sh.get()!="":
                if sh.get()in a:
                    clear_all()
                    trv.insert("",'end',values=(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
                    sh.set("")

    def del_item():
         selected_item=trv.selection()
         item = trv.item(selected_item)
         values=item['values']
         if len(values)>0:
              selected_item = trv.selection()[0]
              trv.delete(selected_item)
              clear()
              emp=open("D:\\PROJECT\\student detail.csv","w",newline="")
              writer=csv.writer(emp)
              listOfEntriesInTreeView=trv.get_children()
              for each in listOfEntriesInTreeView:
                   writer.writerow(trv.item(each)['values'])   
         else:
            messagebox.showinfo("Warning","No data to delete")   
    root=Tk()
    root.title("STUDENT DATA MANAGEMENT")
   
    root.attributes('-fullscreen',True)
   
    root.configure(bg="white")
    
    bg="white"
    font=("time new roman",8,"bold")

    roll_no=StringVar()
    name=StringVar()
    f_name=StringVar()
    gender=StringVar()
    ye=StringVar()
    co_n=StringVar()
    a_d=StringVar()
    options = StringVar()
    sh=StringVar()


    #title=Label(root,text="Student Management System",font=("Forte",10,"bold"),bg=bg,fg="red")
    #title.place(x=580,y=10)

    f=LabelFrame(root,text="Registration Form",bg=bg,fg="red",bd=5,relief=GROOVE,font=font)
    f.place(x=20,y=200,width=400,height=550)

    r=Label(f,text="Roll no.",bg=bg,font=font).grid(row=0,column=0,ipadx=10,ipady=10)
    r_e=Entry(f,textvariable=roll_no,font=font,relief=GROOVE,bd=4,width=15)
    r_e.grid(row=0,column=1,padx=40)
    r_e.focus()
    n=Label(f,text="Name",bg=bg,font=font).grid(row=1,column=0,ipadx=10,ipady=10)
    n_e=Entry(f,textvariable=name,font=font,relief=GROOVE,bd=4,width=15).grid(row=1,column=1,padx=40)

    p=Label(f,text="Father's name",bg=bg,font=font).grid(row=2,column=0,ipadx=10,ipady=10)
    p_e=Entry(f,textvariable=f_name,font=font,relief=GROOVE,bd=4,width=15).grid(row=2,column=1,padx=40)

    g=Label(f,text="Gender",bg=bg,font=font).grid(row=3,column=0,ipadx=10,ipady=10)
    
    gender.set('Male')
    r1 = Radiobutton(f, text='Male', variable=gender, value='Male',font=font,bg=bg)
    r1.place(x=185,y=150)
    r2 = Radiobutton(f, text='Female', variable=gender, value='Female',font=font,bg=bg)
    r2.place(x=280,y=150)

    op=Label(f,text="grade",font=font,bg=bg)
    op.grid(row=4,column=0)
    options.set("") 
    opt = OptionMenu(f,options,"One","Two","Three", "Four", "Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve")
    opt.grid(row=4,column=1)

    y=Label(f,text="year",bg=bg,font=font).grid(row=5,column=0,ipadx=10,ipady=10)

    y=ttk.Combobox(f,width=18,textvariable=ye,font=("time new roman",6,"bold"))
    y["values"]=(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,2100,)
    y.grid(row=5,column=1,padx=40)

    co=Label(f,text="Contact no.",bg=bg,font=font).grid(row=6,column=0,ipadx=10,ipady=10)
    co_e=Entry(f,textvariable=co_n,font=font,relief=GROOVE,bd=4,width=15).grid(row=6,column=1,padx=40)

    a=Label(f,text="Address",bg=bg,font=font).grid(row=7,column=0)
    a_e=Entry(f,textvariable=a_d,font=font,relief=GROOVE,bd=4,width=15).grid(row=7,column=1)

    f2=Label(f,bd=7,relief=GROOVE,bg=bg,font=font)
    f2.place(x=40,y=380,width=300,height=120)

    b1=Button(f2,text="Add",bg=bg,font=font,bd=5,command=add).grid(row=0,column=0,ipadx=18,padx=10,pady=2)
    b2=Button(f2,text="Update",bg=bg,font=font,bd=5,command=update).grid(row=0,column=1,padx=10,pady=2)
    b3=Button(f2,text="Delete",bg=bg,font=font,bd=5,command=del_item).grid(row=1,column=0,padx=10,pady=2)
    b4=Button(f2,text="Clear",bg=bg,font=font,bd=5,command=clear).grid(row=1,column=1,ipadx=16,padx=10,pady=2)

    f3=LabelFrame(root,bd=5,text="Main",bg=bg,fg="red",relief=GROOVE,font=font)
    f3.place(x=430,y=200,height=550,width=840)

    s_e=Entry(f3,textvariable=sh,font=font,relief=GROOVE,bd=4,width=15).grid(row=0,column=0,padx=20)

    s_b=Button(f3,text="SEARCH",bg=bg,font=font,command=show).grid(row=0,column=1,padx=10)
    sl_b=Button(f3,text="SEARCH ALL",bg=bg,font=font,command=show_all).grid(row=0,column=2,padx=10)


    f4=LabelFrame(f3,relief=GROOVE,bd=5,bg=bg,font=font)
    f4.place(x=10,y=80,width=800,height=430)


    trv=ttk.Treeview(f4,selectmode='browse',height=13)
    trv.grid(row=0,column=0)
    trv["columns"]=("1","2","3","4","5","6","7","8")
    trv['show']='headings'
    trv.column("1",width=80,anchor='c')
    trv.column("2",width=120,anchor='c')
    trv.column("3",width=130,anchor='c')
    trv.column("4",width=80,anchor='c')
    trv.column("5",width=80,anchor='c')
    trv.column("6",width=80,anchor='c')
    trv.column("7",width=120,anchor='c')
    trv.column("8",width=100,anchor='c')
    trv.heading("1",text="ROLL NO")
    trv.heading("2",text="Name")
    trv.heading("3",text="FATHER NAME")
    trv.heading("4",text="GENDER")
    trv.heading("5",text="GRADE")
    trv.heading("6",text="YEAR")
    trv.heading("7",text="CONTACT NO.")
    trv.heading("8",text="ADDRESS")
    load()
    trv.bind('<<TreeviewSelect>>', getedit)
    r_e.focus_set=()


    exit_img=PhotoImage(file="D:\\PROJECT\\exit icon.png",master=root)
    destroy_b=Button(root,text="destroy",command=destroy1,image=exit_img).place(x=1230,y=6)

    img=PhotoImage(file='D:\\PROJECT\\student icon.png',master=root)
    img_label=Label(root,image=img,bg=bg)
    img_label.place(x=550,y=0)

    simg=PhotoImage(file='D:\\PROJECT\\school icon.png',master=root)
    simg_label=Label(root,image=simg,bg=bg)
    simg_label.place(x=80,y=0)

    root.mainloop()    

##==========================================================================================================================================================##
                                           #MENU#
##==========================================================================================================================================================##
def data_management():
    def menu1():
        menu.destroy()
        student()
    def menu2():
        pass
        menu.destroy()
        mark()
        
    def exit1():
        menu.destroy()
    menu=Tk()
    menu.title("MENU")
    menu.attributes('-fullscreen',True)
    menu.configure(bg="white")
    
    title=Label(menu,text="STUDENT DATA BASE MANAGEMENT",font=("Forte",30,"bold"),bg="white",fg="red")
    title.place(x=100,y=100)
    st_img=PhotoImage(file="D:\\PROJECT\\marksheet icon.png",master=menu)
    st_button=Button(menu,image=st_img,bg="white",height=180,width=180,command=menu2)
    st_button.place(x=690,y=360)
    st_label=Label(menu,text="student record",bg="white",fg="gold",font=("time new roman",13,"bold")).place(x=690,y=550)
    m_img=PhotoImage(file="D:\\PROJECT\\info icon.png",master=menu)
    m_button=Button(menu,image=m_img,bg="white",command=menu1)
    m_button.place(x=420,y=360)
    m_label=Label(menu,text="student marksheet",bg="white",fg="gold",font=("time new roman",13,"bold")).place(x=400,y=550)
    exit_img=PhotoImage(file="D:\\PROJECT\\exit icon.png",master=menu)
    destroy_b=Button(menu,text="destroy",command=exit1,image=exit_img,bg="white").place(x=1230,y=6)
    menu.mainloop()
##==========================================================================================================================================================##
                                           #CREATE ACCOUNT#
##==========================================================================================================================================================##
def create_account():
    def create_id():
    
        file=open("D:\\PROJECT\\account info.csv","a",newline="")
        data=csv.writer(file)
        if c.get()!="" and cp.get()!="" and cpd.get()!="":
            data.writerow([f.get(),l.get(),c.get(),cp.get(),cpd.get(),b.get(),g.get(),m.get()])
            file.close()
            f.set("")
            l.set("")
            c.set("")
            cp.set("")
            cpd.set("")
            b.set("")
            g.set("")
            m.set("")
            create.destroy()
            login_account()
        elif c.get()=="" and cp.get()=="" and cpd.get()=="":
##            pass
            msg_label=Label(frame,text="please fill the information",fg="red",bg=bg)
            msg_label.place(x=400,y=450)
            

    def go_back():
        create.destroy()
        login_account()
        
        
    create=Tk()
##    create.geometry("1600x900+0+0")
    create.attributes('-fullscreen',True)
    create.configure(bg="white")
    bd=1
    bg="white"

    f=StringVar()
    l=StringVar()
    c=StringVar()
    cp=StringVar()
    cpd=StringVar()
    b=StringVar()
    g=StringVar()
    m=StringVar()

    frame=Frame(create,width=860,height=600,bd=1,relief=SOLID,bg="white")
    frame.place(x=260,y=140)

    title=Label(create,text="CREATE YOUR ACCOUNT",font="forte 25 bold",bg=bg,fg="red")
    title.place(x=360,y=60)

    f_label=Label(frame,text="FIRST NAME",bg=bg)
    f_label.place(x=100,y=50)
    f_entry=Entry(frame,textvariable=f,bd=1)
    f_entry.place(x=400,y=50)

    l_label=Label(frame,text="LAST NAME",bg=bg)
    l_label.place(x=100,y=100)
    l_entry=Entry(frame,textvariable=l)
    l_entry.place(x=400,y=100)

    c_label=Label(frame,text=" CHOOSE YOUR USERNAME",bg=bg)
    c_label.place(x=100,y=150)
    c_entry=Entry(frame,textvariable=c)
    c_entry.place(x=400,y=150)

    cp_label=Label(frame,text="CREATE A PASSWORD",bg=bg)
    cp_label.place(x=100,y=200)
    cp_entry=Entry(frame,textvariable=cp,show="*")
    cp_entry.place(x=400,y=200)

    cpd_label=Label(frame,text="CONFIRM YOUR PASSWORD",bg=bg)
    cpd_label.place(x=100,y=250)
    cpd_entry=Entry(frame,textvariable=cpd,show="*")
    cpd_entry.place(x=400,y=250)

    b_label=Label(frame,text="BIRTHDAY",bg=bg)
    b_label.place(x=100,y=300)
    b_entry=Entry(frame,textvariable=b)
    b_entry.place(x=400,y=300)

    g_label=Label(frame,text="GENDER",bg=bg)
    g_label.place(x=100,y=350)
    g_entry=Entry(frame,textvariable=g)
    g_entry.place(x=400,y=350)


    m_label=Label(frame,text="MOBILE NO.",bg=bg)
    m_label.place(x=100,y=400)
    m_entry=Entry(frame,textvariable=m)
    m_entry.place(x=400,y=400)


    l_button=Button(frame,text="GO BACK",bd=bd,bg=bg,command=go_back)
    l_button.place(x=100,y=500)

    c_button=Button(frame,text="CREATE",bd=bd,bg=bg,command=create_id)
    c_button.place(x=500,y=500)

    img=PhotoImage(file='D:\\PROJECT\\user icon.png',master=frame)
    img_label=Label(frame,image=img,bg=bg)
    img_label.place(x=620,y=80)

    create.mainloop()

##==========================================================================================================================================================##
                                           #LOGIN ACCOUNT#
##==========================================================================================================================================================##
def login_account():
    def login_id():
        
        file=open("D:\\PROJECT\\account info.csv","r")
        count=0
        data=csv.reader(file)
        for d in data:
            if d[2]==u.get()and d[3]==p.get():
                count=count+1
        file.close()
        if count==0:
            messagebox.showinfo("Error","User ID is wrong")
        else:
            login.destroy()
            data_management()

    def create_id():
        login.destroy()
        create_account()
    def exit2():
        login.destroy()
        
    login=Tk()
    login.attributes('-fullscreen',True)
    login.configure(bg="white")
    
    font=("time new roman",10,"bold")
    
    u=StringVar()
    p=StringVar()
    bd=1
    bg="white"

    
    title=Label(login,text="STUDENT DATA MANAGEMENT",font=("time new roman",20,"bold"),bg=bg,fg="red")
    title.place(x=360,y=80)
    

    img=PhotoImage(file='D:\\PROJECT\\info icon.png',master=login)
    img_label=Label(login,image=img,bg=bg)
    img_label.place(x=1000,y=20)
    
    img1=PhotoImage(file='D:\\PROJECT\\school icon.png',master=login)
    img1_label=Label(login,image=img1,bg=bg)
    img1_label.place(x=80,y=20)

    
    frame=Frame(login,bd=1,relief=SOLID,width=600,height=400,bg=bg)
    frame.place(x=360,y=250)
    ftitle=Label(frame,text="LOGIN YOUR ACCOUNT",font=("time new roman",20,"bold"),bg=bg,fg="red")
    ftitle.place(x=80,y=40)
    u_label=Label(frame,text="USERNAME",bg=bg,font=font)
    u_label.place(x=100,y=120)
    u_entry=Entry(frame,textvariable=u)
    u_entry.place(x=300,y=120)
    
    p_label=Label(frame,text="PASSWORD",bg=bg,font=font)
    p_label.place(x=100,y=180)
    p_entry=Entry(frame,textvariable=p,show="*")
    p_entry.place(x=300,y=180)
    
    l_button=Button(frame,text="LOGIN",bg=bg,command=login_id,font=font)
    l_button.place(x=400,y=280)

    
    c_button=Button(frame,text="CREATE",bg=bg,command=create_id,font=font)
    c_button.place(x=100,y=280)

    exit_img=PhotoImage(file="D:\\PROJECT\\exit icon.png",master=login)

    q_button=Button(login,image=exit_img,bg=bg,borderwidth=0,command=exit2)
    q_button.place(x=1230,y=6)
    
    
    login.mainloop()

login_account()
    
##data_management()
