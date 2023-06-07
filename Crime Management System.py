from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Criminal Mangement System")

        lbl_title = Label(self.root, text="Criminal Management System Software",font=('times new roman',40,'bold'),bg='black',fg='green')
        lbl_title.place(x=0,y=0,width=1430,height=70)

        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_address=StringVar()
        self.var_birthmark=StringVar()
        self.var_gender=StringVar()
        self.var_most_wanted=StringVar()




        #ncr logo
        img_logo = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\crime_logo.jpg")
        img_logo = img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)

        #image frame 
        img_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1430,height=150)

        # First image

        img1 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\c_photo1.jpeg")
        img1 = img1.resize((540,160),Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=476,height=150)

        # Second Image
        img2 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\c_photo2.jpeg")
        img2 = img2.resize((540,160),Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame,image=self.photo2)
        self.img_2.place(x=477,y=0,width=476,height=150)

        # Third Image

        img3 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\c_photo3.jpg")
        img3 = img3.resize((540,160),Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_2 = Label(img_frame,image=self.photo3)
        self.img_2.place(x=954,y=0,width=476,height=150)

        # main frame
        Main_frame = Frame(self.root,bd=2,relief = RIDGE,bg= 'white')
        Main_frame.place(x=0,y=220,width=1365,height=480)

        #upper frame
        upper_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal Information",font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=0,y=0,width=1350,height=240)
        
        #Labels nd Entry

        #case id
        caseid = Label(upper_frame,text="Case ID:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry = ttk.Entry(upper_frame,width=22,textvariable=self.var_case_id,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #criminal id
        lbl_criminal_no = Label(upper_frame,text="Criminal No:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_criminal_no = ttk.Entry(upper_frame,width=22,textvariable=self.var_criminal_no,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #criminal name
        lbl_Name = Label(upper_frame,text="Criminal Name:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_Name.grid(row=1,column=0,padx=2,sticky=W,pady=4)

        txt_Name = ttk.Entry(upper_frame,width=22,textvariable=self.var_name,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,sticky=W,pady=4)

        #nickname
        
        lbl_Nickname = Label(upper_frame,text="Nickname:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_Nickname.grid(row=1,column=2,padx=2,sticky=W,pady=4)

        txt_Nickname = ttk.Entry(upper_frame,width=22,textvariable=self.var_nickname,font=('arial',11,'bold'))
        txt_Nickname.grid(row=1,column=3,padx=2,sticky=W,pady=4)

        #Age
        
        lbl_age = Label(upper_frame,text="Age:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_age.grid(row=2,column=0,padx=2,sticky=W,pady=4)

        txt_age = ttk.Entry(upper_frame,width=22,textvariable=self.var_age,font=('arial',11,'bold'))
        txt_age.grid(row=2,column=1,padx=2,sticky=W,pady=4)

        #occupation
        lbl_occupation = Label(upper_frame,text="Occupation:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_occupation.grid(row=2,column=2,padx=2,sticky=W,pady=4)

        txt_occupation = ttk.Entry(upper_frame,width=22,textvariable=self.var_occupation,font=('arial',11,'bold'))
        txt_occupation.grid(row=2,column=3,padx=2,sticky=W,pady=4)

        #Arrest Date
        lbl_arrestdate = Label(upper_frame,text="Arrest Date:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_arrestdate.grid(row=3,column=0,padx=2,sticky=W,pady=4)

        txt_arrestdate = ttk.Entry(upper_frame,width=22,textvariable=self.var_arrest_date,font=('arial',11,'bold'))
        txt_arrestdate.grid(row=3,column=1,padx=2,sticky=W,pady=4)

        #Date of Crime
        lbl_dateofcrime = Label(upper_frame,text="Date of Crime:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_dateofcrime.grid(row=3,column=2,padx=2,sticky=W,pady=4)

        txt_dateofcrime = ttk.Entry(upper_frame,width=22,textvariable=self.var_date_of_crime,font=('arial',11,'bold'))
        txt_dateofcrime.grid(row=3,column=3,padx=2,sticky=W,pady=4)

        # Crime Type
        lbl_crimetype = Label(upper_frame,text="Crime Type:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_crimetype.grid(row=4,column=0,padx=2,sticky=W,pady=4)

        txt_crimetype = ttk.Entry(upper_frame,width=22,textvariable=self.var_crime_type,font=('arial',11,'bold'))
        txt_crimetype.grid(row=4,column=1,padx=2,sticky=W,pady=4)

        # Father Name
        lbl_fathername = Label(upper_frame,text="Father Name:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_fathername.grid(row=4,column=2,padx=2,sticky=W,pady=4)

        txt_fathername = ttk.Entry(upper_frame,width=22,textvariable=self.var_father_name,font=('arial',11,'bold'))
        txt_fathername.grid(row=4,column=3,padx=2,sticky=W,pady=4)

        #Address

        lbl_adress = Label(upper_frame,text="Address:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_adress.grid(row=0,column=4,padx=2,sticky=W,pady=4)

        txt_adress = ttk.Entry(upper_frame,width=22,textvariable=self.var_address,font=('arial',11,'bold'))
        txt_adress.grid(row=0,column=5,padx=2,sticky=W,pady=4)

        #BirthMark

        
        lbl_birthmark = Label(upper_frame,text="Birthmark:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_birthmark.grid(row=1,column=4,padx=2,sticky=W,pady=4)

        txt_birthmark = ttk.Entry(upper_frame,width=22,textvariable=self.var_birthmark,font=('arial',11,'bold'))
        txt_birthmark.grid(row=1,column=5,padx=2,sticky=W,pady=4)

        #gender

        
        lbl_gender = Label(upper_frame,text="Gender:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_gender.grid(row=2,column=4,padx=2,sticky=W,pady=4)

        # radio button gender

        radio_frame_gender = Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=698,y=72,width=180,height=30)

        male = Radiobutton(radio_frame_gender,text='Male', value = 'male', variable=self.var_gender,font=("arial",9,'bold'))
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        female = Radiobutton(radio_frame_gender,text='Female', value = 'male', variable=self.var_gender,font=("arial",9,'bold'))
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        # trans = Radiobutton(radio_frame_gender,text='TransGender', value = 'transgender', font=("arial",9,'bold'))
        # trans.grid(row=0,column=3,pady=2,padx=5,sticky=W)

        #most wanted

        lbl_wanted = Label(upper_frame,text="Most Wanted:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_wanted.grid(row=3,column=4,padx=2,sticky=W,pady=7)
        
        radio_frame_wanted = Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=698,y=110,width=180,height=30)

        yes = Radiobutton(radio_frame_wanted,text='Yes', value = 'yes',variable=self.var_most_wanted,font=("arial",9,'bold'))
        yes.grid(row=1,column=0,pady=2,padx=5,sticky=W)

        no = Radiobutton(radio_frame_wanted,text='No', value = 'no',variable=self.var_most_wanted,font=("arial",9,'bold'))
        no.grid(row=1,column=1,pady=2,padx=5,sticky=W)

        #buttons

        butttn_frame = Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        butttn_frame.place(x=5,y=175,width=620,height=40)

        # ADD Button

        btn_add = Button(butttn_frame,command=self.add_data,text='Record Save',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #update button
        btn_update  = Button(butttn_frame,text='Update Record',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update .grid(row=0,column=1,padx=3,pady=5)

        #Delete Button

        btn_delete = Button(butttn_frame,text='Delete Record',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #clear Button

        btn_clear = Button(butttn_frame,text='Clear Record',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=4,padx=3,pady=5)

        #right side image

        img4 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\c_photo1.jpeg")
        img4 = img4.resize((600,220),Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(img4)

        self.img_4 = Label(upper_frame,image=self.photo4)
        self.img_4.place(x=900,y=0,width=440,height=210)


        # down Frame
        down_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal Information Table",font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=0,y=241,width=1350,height=230)

        search_frame = LabelFrame(down_frame,bd=2,relief=RIDGE,text="Search Criminal Record",font=('times new roman',11,'bold'),fg='Blue',bg='white')
        search_frame.place(x=0,y=0,width=1340,height=60)

        search_by= Label(search_frame,font=('arial',11,'bold'),text='Search By',bg='red',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        combo_search= ttk.Combobox(search_frame,font=('arial',11,'bold'),width=18)
        combo_search['value']=('Select Option','Case_id','Criminal_no')
        combo_search.set(0)
        combo_search.grid(row=0,column=1,sticky=W,padx=5)

        search_txt= ttk.Entry(search_frame,width=19,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,padx=5,sticky=W)

        #Search Button

        btn_search = Button(search_frame,text='Search',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #Show ALl Button

        btn_all = Button(search_frame,text='Show All',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        table_frame= Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1350,height=150)

        crimeAgency= Label(search_frame,font=('arial',25,'bold'),text='National Crime Agency',bg='white',fg='Grey')
        crimeAgency.grid(row=0,column=5,sticky=W,padx=10,pady=0)


        #scroll Bar

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)


        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nickname')
        self.criminal_table.heading('5',text='Age')
        self.criminal_table.heading('6',text='Occupation')
        self.criminal_table.heading('7',text='Arrest Date')
        self.criminal_table.heading('8',text='Date of Crime')
        self.criminal_table.heading('9',text='Crime Type')
        self.criminal_table.heading('10',text='Father Name')
        self.criminal_table.heading('11',text='Address')
        self.criminal_table.heading('12',text='BirthMark')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Most Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)
        self.criminal_table.column("8",width=100)
        self.criminal_table.column("9",width=100)
        self.criminal_table.column("10",width=100)
        self.criminal_table.column("11",width=100)
        self.criminal_table.column("12",width=100)
        self.criminal_table.column("13",width=100)
        self.criminal_table.column("14",width=100)


        self.criminal_table.pack(fill=BOTH,expand=1)

        self.fetch_Data()
        

        #add Function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')

        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Amit@9588',database='crime_management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_case_id.get(),
                                                                                                                self.var_criminal_no.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_nickname.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_occupation.get(),
                                                                                                                self.var_arrest_date.get(),
                                                                                                                self.var_date_of_crime.get(),
                                                                                                                self.var_crime_type.get(),
                                                                                                                self.var_father_name.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_birthmark.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_most_wanted.get()))
                                                                                                                
                                                                                                                
                                                                                                                




                    
                conn.commit()
                self.fetch_Data()
                conn.close()
                messagebox.showinfo('Success','Criminial Record has been added successfully')
            except Exception as es:
                messagebox.showerror('Error',f'Error due to {str(es)}')

    def fetch_Data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Amit@9588',database='crime_management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()



        
if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
        