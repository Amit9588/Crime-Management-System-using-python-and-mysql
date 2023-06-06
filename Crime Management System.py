from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Criminal:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Criminal Mangement System")

        lbl_title = Label(self.root, text="Criminal Management System Software",font=('times new roman',40,'bold'),bg='black',fg='green')
        lbl_title.place(x=0,y=0,width=1430,height=70)
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

        caseentry = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #criminal id
        lbl_criminal_no = Label(upper_frame,text="Criminal No:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_criminal_no = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #criminal name
        lbl_Name = Label(upper_frame,text="Criminal Name:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_Name.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        txt_Name = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,sticky=W,pady=7)

        #nickname
        
        lbl_Nickname = Label(upper_frame,text="Nickname:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_Nickname.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        txt_Nickname = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_Nickname.grid(row=1,column=3,padx=2,sticky=W,pady=7)

        #Age
        
        lbl_age = Label(upper_frame,text="Age:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_age.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        txt_age = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=2,column=1,padx=2,sticky=W,pady=7)

        #occupation
        lbl_occupation = Label(upper_frame,text="Occupation:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_occupation.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        txt_occupation = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=2,column=3,padx=2,sticky=W,pady=7)

        #Arrest Date
        lbl_arrestdate = Label(upper_frame,text="Arrest Date:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_arrestdate.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        txt_arrestdate = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_arrestdate.grid(row=3,column=1,padx=2,sticky=W,pady=7)

        #Date of Crime
        lbl_dateofcrime = Label(upper_frame,text="Date of Crime:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_dateofcrime.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        txt_dateofcrime = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_dateofcrime.grid(row=3,column=3,padx=2,sticky=W,pady=7)

        # Crime Type
        lbl_crimetype = Label(upper_frame,text="Crime Type:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_crimetype.grid(row=4,column=0,padx=2,sticky=W,pady=7)

        txt_crimetype = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_crimetype.grid(row=4,column=1,padx=2,sticky=W,pady=7)

        # Father Name
        lbl_fathername = Label(upper_frame,text="Father Name:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_fathername.grid(row=4,column=2,padx=2,sticky=W,pady=7)

        txt_fathername = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_fathername.grid(row=4,column=3,padx=2,sticky=W,pady=7)

        #Address

        lbl_adress = Label(upper_frame,text="Address:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_adress.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        txt_adress = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_adress.grid(row=0,column=5,padx=2,sticky=W,pady=7)

        #BirthMark

        
        lbl_birthmark = Label(upper_frame,text="Birthmark:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_birthmark.grid(row=1,column=4,padx=2,sticky=W,pady=7)

        txt_birthmark = ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_birthmark.grid(row=1,column=5,padx=2,sticky=W,pady=7)

        #gender

        
        lbl_gender = Label(upper_frame,text="Gender:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_gender.grid(row=2,column=4,padx=2,sticky=W,pady=7)

        # radio button gender

        radio_frame_gender = Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=90,width=190,height=30)

        male = Radiobutton(radio_frame_gender,text='Male', value = 'male', font=("arial",9,'bold'))
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        lbl_wanted = Label(upper_frame,text="Most Wanted:",font=('times new roman',11,'bold'),fg='Blue',bg='white' )
        lbl_wanted.grid(row=3,column=4,padx=2,sticky=W,pady=7)






        # down Frame
        down_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal Information Table",font=('times new roman',11,'bold'),fg='Blue',bg='white')
        down_frame.place(x=0,y=241,width=1350,height=230)

        search_frame = LabelFrame(down_frame,bd=2,relief=RIDGE,text="Search Criminal Record",font=('times new roman',11,'bold'),fg='Blue',bg='white')
        search_frame.place(x=0,y=241,width=1350,height=230)

        
if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
        