from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.font import Font

root = Tk()
root.title("PASSWORD MANAGER")
root.configure(background = "#a7d9c5")

root.geometry("600x500")

password = StringVar()
regNo = StringVar()
# image list
my_img1 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-cut.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-wave.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-graffiti.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-mass.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-collage.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-spiderweb2.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-collage.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-sunrays.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-wavycolorletters.jpg"))



image_list = [my_img1 , my_img2, my_img3, my_img4, my_img5, my_img6 , my_img7 ,my_img8, my_img9]
imglabel = Label(image = my_img1)



# fonts
mssglabfont = Font(family ='Bodoni MT' ,size =25 )
cappyfont = Font(family = 'Rockwell' ,size = 12)
entryfont = Font(family = "Arial" ,size = 10 )
buttonfont = Font(family = "Rockwell", size = 12)



def clear():
    regNo.set("")
    password.set("")
    capClear.set("")


def fun():
    messagebox.showinfo("saved","Sign In Sucessfully")

# logic for forward
def forward(image_number):
    global imglabel
    global refreshb

    imglabel.grid_forget()
    imglabel = Label(image = image_list[image_number - 1])
    refreshb = Button(root,text = "Refresh",image= photo ,border = 4 ,height = 15,width =15,command = lambda: forward(image_number+1),bg='#e0e5ef')

    imglabel.place(x=280, y=220)
    refreshb.place(x = 550, y=220)



img = ImageTk.PhotoImage(Image.open("imagess/botdetect3-captcha-cut.jpg"))
regNo = StringVar()
password = StringVar()
capClear = StringVar()


imglabel.place(x=280, y=220)
photo = PhotoImage(file="refresh-page-option.png")

# imglabel.place(x=280, y=220)


nreg = Label(root , text = "Reg No. ",bg="#a7d9c5" ,font = cappyfont).place(x =170, y =100)
npwd = Label(root ,text = "Password ",bg="#a7d9c5",font = cappyfont).place(x = 170 ,y = 150)
txx = Label(root ,text = "Type the code you see above *",font = "none 10 bold italic ",bg="#a7d9c5",fg = '#e03267').place(x = 280 ,y = 280)
cappy = Label(root ,text = "Captcha ",bg="#a7d9c5",font = cappyfont).place(x = 170 ,y = 220)
mssg = Label(root ,text = "Welcome to Python Class ",bg="#a7d9c5",font = mssglabfont, fg = '#162e61' ).place(x = 150,y = 10)


regEne1 = Entry(root,textvariable= regNo ,font = entryfont).place(x = 280 , y = 100,width = 200 ,height = 25)
captchaEnte2 = Entry(root,textvariable= capClear,font = entryfont).place(x = 280 , y = 320,width = 200 ,height = 25)
passwode3 = Entry(root ,width = 25,textvariable= password, show='*',font = entryfont).place(x = 280 ,y = 150,width = 200 ,height = 25)



sbmitbtn = Button(root, text = "Sign In", command = fun ,bg='#b6aed9' ,width = 7 ,height =1,font = buttonfont,border = 3).place(x = 280, y = 380)
refreshb = Button(root ,image= photo ,border = 2 ,height = 15,width =15 ,command = lambda :forward(2) ,bg='#e0e5ef').place(x = 550, y =220)
clrbutton = Button(root ,text = "clear",command = clear,width = 7 ,height = 1,font =buttonfont,border = 4 ,bg='#b6aed9').place(x = 380, y =378)




root.mainloop()



