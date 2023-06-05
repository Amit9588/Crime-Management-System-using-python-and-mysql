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

        img_logo = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\crime_logo.jpg")
        img_logo = img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)

        


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
        