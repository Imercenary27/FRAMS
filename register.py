from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #text VAriables
        self.var_fname=StringVar()
        self.var_Lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


        img=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\hackers2.jpg")
        img=img.resize((1517,765),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=5,y=10,width=1517,height=765)

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hp\Desktop\face_recognition_system\college_images\clock.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        get_str=Label(frame,text="REGISTER HERE",font=("Arial Black",20,"bold"),fg="darkgreen",bg="white")
        get_str.place(x=20,y=20)

        fname=Label(frame,text="First Name:",font=("Arial Black",15,"bold"),bg="White")
        fname.place(x=50,y=100)

        self.txtfname=ttk.Entry(frame,textvariable=self.var_fname,font=("Arial Black",15,"bold"))
        self.txtfname.place(x=50,y=130,width=300)

        Lname=Label(frame,text="Last Name:",font=("Arial Black",15,"bold"),bg="White")
        Lname.place(x=450,y=100)

        self.txtLname=ttk.Entry(frame,textvariable=self.var_Lname,font=("Arial Black",15,"bold"))
        self.txtLname.place(x=450,y=130,width=300)

        contact=Label(frame,text="Contact No.:",font=("Arial Black",15,"bold"),bg="White")
        contact.place(x=50,y=180)

        self.txtcontact=ttk.Entry(frame,textvariable=self.var_contact,font=("Arial Black",15,"bold"))
        self.txtcontact.place(x=50,y=210,width=300)

        email=Label(frame,text="Email:",font=("Arial Black",15,"bold"),bg="White")
        email.place(x=450,y=180)

        self.txtemail=ttk.Entry(frame,textvariable=self.var_email,font=("Arial Black",15,"bold"))
        self.txtemail.place(x=450,y=210,width=300)

        SQ=Label(frame,text="Select Security Question:",font=("Arial Black",15,"bold"),bg="White")
        SQ.place(x=50,y=260)

        depSQ_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Arial Black",15,"bold"),state="readonly",width=21)
        depSQ_combo["values"]=("Select","Birth Place","Favourite City","Pet Name","Favourite Car","Favourite Actor","Favourite Actress")
        depSQ_combo.current(0)
        depSQ_combo.place(x=50,y=290)

        SQA=Label(frame,text="Security Answer:",font=("Arial Black",15,"bold"),bg="White")
        SQA.place(x=450,y=260)

        self.txtSQA=ttk.Entry(frame,textvariable=self.var_securityA,font=("Arial Black",15,"bold"))
        self.txtSQA.place(x=450,y=290,width=300)

        Password=Label(frame,text="Confirm Password:",font=("Arial Black",15,"bold"),bg="White")
        Password.place(x=50,y=340)

        self.txtPassword=ttk.Entry(frame,textvariable=self.var_pass,font=("Arial Black",15,"bold"))
        self.txtPassword.place(x=50,y=370,width=300)

        Cpass=Label(frame,text="Confirm Password:",font=("Arial Black",15,"bold"),bg="White")
        Cpass.place(x=450,y=340)

        self.txtCpass=ttk.Entry(frame,textvariable=self.var_confpass,font=("Arial Black",15,"bold"))
        self.txtCpass.place(x=450,y=370,width=300)

        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("Arial Black",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=410)

        #buttons'
        img5=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\register-now-button1.jpg")
        img5=img5.resize((200,55),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        save_btn=Button(frame,image=self.photoimg5,command=self.register_data,borderwidth=0,cursor="hand2")
        save_btn.place(x=50,y=440,width=200)

        img6=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\loginpng.png")
        img6=img6.resize((200,45),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        save_btn=Button(frame,image=self.photoimg6,borderwidth=0,cursor="hand2")
        save_btn.place(x=525,y=450,width=200)

    
    #Function Declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif len(self.var_pass.get())<5:
            messagebox.showerror("Error","Password should be of Mininum 6 characters")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please click on agree terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",passwd="Krunal@2002",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #if row!=None:
                #messagebox.showerror("Error","User already exist")
            if row==None:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                       ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success","Registered Successfully")    
    






if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()