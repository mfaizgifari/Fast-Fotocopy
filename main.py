from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Set-up awal GUI 
root = Tk()
root.title("Fast Fotocopy")
root.geometry("1600x600")
root.resizable(False,False)


# Function button
def reset():
    entryA0.delete(0,END)
    entryA1.delete(0,END)
    entryA2.delete(0,END)
    entryA3.delete(0,END)
    entryA4.delete(0,END)  
    entryF4.delete(0,END)
    entrycA0.delete(0,END)  
    entrycA1.delete(0,END)  
    entrycA2.delete(0,END)  
    entrycA3.delete(0,END)  
    entrycA4.delete(0,END)  
    entrycF4.delete(0,END) 
         
def total():
    try: a0 = int(bwA0.get())   
    except: a0 = 0   
    try: a1 = int(bwA1.get())   
    except: a1 = 0  
    try: a2 = int(bwA2.get())   
    except: a2 = 0  
    try: a3 = int(bwA3.get())   
    except: a3 = 0  
    try: a4 = int(bwA4.get())   
    except: a4 = 0  
    try: f4 = int(bwF4.get())   
    except: f4 = 0  
    
    try: ca0 = int(cA0.get())   
    except: ca0 = 0  
    try: ca1 = int(cA1.get())   
    except: ca1 = 0  
    try: ca2 = int(cA2.get())   
    except: ca2 = 0  
    try: ca3 = int(cA3.get())   
    except: ca3 = 0  
    try: ca4 = int(cA4.get())   
    except: ca4 = 0  
    try: cf4 = int(cF4.get())   
    except: cf4 = 0  
    
    # Penjumlahan Harga
    totalharga = StringVar()
    
    Ta0 = 12000 * a0
    Ta1 = 8000 * a1
    Ta2 = 4000 * a2
    Ta3 = 800 * a3
    Ta4 = 200 * a4
    Tf4 = 250 * f4
    
    Tca0 = 24000 * ca0
    Tca1 = 16000 * ca1
    Tca2 =  8000 * ca2
    Tca3 =  1600 * ca3
    Tca4 =   400 * ca4
    Tcf4 =   500 * cf4
    
    entrytotal = Entry(root,font=("Monserrat",20,'bold'),textvariable=totalharga,bd=8,width=35)
    entrytotal.place(x=960,y=200)
    
    if  checkMem.get() == 1:
        totaldiskon = (Ta0 + Ta1 + Ta2 + Ta3 + Ta4 + Tf4 + Tca0 + Tca1 + Tca2 + Tca3 + Tca4 + Tcf4) * 0.9
        string_total="Rp." + str('%.2f' %totaldiskon)
    else:
        totalsemua = Ta0 + Ta1 + Ta2 + Ta3 + Ta4 + Tf4 + Tca0 + Tca1 + Tca2 + Tca3 + Tca4 + Tcf4
        string_total="Rp." + str('%.2f' %totalsemua)
        
    totalharga.set(string_total) 
          
  
# Bagian Menu
class background:
    photo = PhotoImage(file="bg.png")
    canvas = Canvas(root)
    canvas.create_image(0,0,image=photo,anchor=NW)
    labelphoto = Label(root, image = photo)
    labelphoto.place(x=0,y=0)
    
class labelatas:
    Label(text="FAST FOTOCOPY",fg="black",font=("Paladins Laser",40),width="100",height="1").pack()
    Label(text="By: Muhamad Faiz Gifari",fg="black",font=("Monserrat",10),width="200",height="2").pack()

class boxhitamputih:
    f = Frame(root,bg="white",highlightbackground="black",highlightthickness=1,width=400,height=410)
    f.place(x=20,y=120)

    Label(f, font=("Monserrat",20,'bold'),bg="white",text="HITAM PUTIH",fg="black").place(x=110,y=15)
    Label(f, font=("Monserrat",12,'bold'),bg="white",text="UKURAN",fg="black").place(x=15,y=60)
    Label(f, font=("Monserrat",12,'bold'),bg="white",text="HARGA",fg="black").place(x=270,y=60)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.12000",fg="black").place(x=220,y=90)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp. 8000",fg="black").place(x=220,y=140)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp. 4000",fg="black").place(x=220,y=185)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.  800",fg="black").place(x=220,y=235)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.  200",fg="black").place(x=220,y=280)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.  250",fg="black").place(x=220,y=330)
    
class boxwarna:
    f = Frame(root,bg="white",highlightbackground="black",highlightthickness=1,width=400,height=410)
    f.place(x=445,y=120)

    Label(f, font=("Monserrat",20,'bold'),bg="white",text="WARNA",fg="black").place(x=150,y=15)
    Label(f, font=("Monserrat",12,'bold'),bg="white",text="UKURAN",fg="black").place(x=15,y=60)
    Label(f, font=("Monserrat",12,'bold'),bg="white",text="HARGA",fg="black").place(x=270,y=60)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.24000",fg="black").place(x=220,y=90)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.16000",fg="black").place(x=220,y=140)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp. 8000",fg="black").place(x=220,y=185)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp. 1600",fg="black").place(x=220,y=235)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.  400",fg="black").place(x=220,y=280)
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="Rp.  500",fg="black").place(x=220,y=330)
    
class boxtotal:
    f = Frame(root,bg="white",highlightbackground="black",highlightthickness=1,width=660,height=260)
    f.place(x=900,y=120)    
    Label(f, font=("Monserrat",20,'bold'),bg="white",text="TOTAL HARGA",fg="black").place(x=230,y=15)

    
# FRAME HITAM PUTIH
f0 = Frame(root,bd=8,height=700,width=700,relief=RAISED)
f0.pack(side=LEFT,padx=35,pady=50)

bwA0=StringVar()
bwA1=StringVar()
bwA2=StringVar()
bwA3=StringVar()
bwA4=StringVar()
bwF4=StringVar()

lblbwA0 = Label(f0, font=("Monserrat",20,'bold'),text="A0",fg="black")
lblbwA1 = Label(f0, font=("Monserrat",20,'bold'),text="A1",fg="black")
lblbwA2 = Label(f0, font=("Monserrat",20,'bold'),text="A2",fg="black")
lblbwA3 = Label(f0, font=("Monserrat",20,'bold'),text="A3",fg="black")
lblbwA4 = Label(f0, font=("Monserrat",20,'bold'),text="A4",fg="black")
lblbwF4 = Label(f0, font=("Monserrat",20,'bold'),text="F4",fg="black")
lblbwA0.grid(row=1,column=0)
lblbwA1.grid(row=2,column=0)
lblbwA2.grid(row=3,column=0)
lblbwA3.grid(row=4,column=0)
lblbwA4.grid(row=5,column=0)
lblbwF4.grid(row=6,column=0)

# Entry HITAM PUTIH
entryA0 = Entry(f0,font=("Monserrat",20,'bold'),textvariable=bwA0,bd=6,width=8,bg="white")
entryA1 = Entry(f0,font=("Monserrat",20,'bold'),textvariable=bwA1,bd=6,width=8,bg="white")
entryA2 = Entry(f0,font=("Monserrat",20,'bold'),textvariable=bwA2,bd=6,width=8,bg="white")
entryA3 = Entry(f0,font=("Monserrat",20,'bold'),textvariable=bwA3,bd=6,width=8,bg="white")
entryA4 = Entry(f0,font=("Monserrat",20,'bold'),textvariable=bwA4,bd=6,width=8,bg="white")
entryF4 = Entry(f0,font=("Monserrat",20,'bold'),textvariable=bwF4,bd=6,width=8,bg="white")
entryA0.grid(row=1,column=1)
entryA1.grid(row=2,column=1)
entryA2.grid(row=3,column=1)
entryA3.grid(row=4,column=1)
entryA4.grid(row=5,column=1)
entryF4.grid(row=6,column=1)

# FRAME WARNA
f1 = Frame(root,bd=8,height=500,width=700,relief=RAISED)
f1.pack(side=LEFT,padx=200,pady=50)

cA0=StringVar()
cA1=StringVar()
cA2=StringVar()
cA3=StringVar()
cA4=StringVar()
cF4=StringVar()

lblcA0 = Label(f1, font=("Monserrat",20,'bold'),text="A0",fg="black")
lblcA1 = Label(f1, font=("Monserrat",20,'bold'),text="A1",fg="black")
lblcA2 = Label(f1, font=("Monserrat",20,'bold'),text="A2",fg="black")
lblcA3 = Label(f1, font=("Monserrat",20,'bold'),text="A3",fg="black")
lblcA4 = Label(f1, font=("Monserrat",20,'bold'),text="A4",fg="black")
lblcF4 = Label(f1, font=("Monserrat",20,'bold'),text="F4",fg="black")
lblcA0.grid(row=1,column=0)
lblcA1.grid(row=2,column=0)
lblcA2.grid(row=3,column=0)
lblcA3.grid(row=4,column=0)
lblcA4.grid(row=5,column=0)
lblcF4.grid(row=6,column=0)

# ENTRY WARNA
entrycA0 = Entry(f1,font=("Monserrat",20,'bold'),textvariable=cA0,bd=6,width=8,bg="white")
entrycA1 = Entry(f1,font=("Monserrat",20,'bold'),textvariable=cA1,bd=6,width=8,bg="white")
entrycA2 = Entry(f1,font=("Monserrat",20,'bold'),textvariable=cA2,bd=6,width=8,bg="white")
entrycA3 = Entry(f1,font=("Monserrat",20,'bold'),textvariable=cA3,bd=6,width=8,bg="white")
entrycA4 = Entry(f1,font=("Monserrat",20,'bold'),textvariable=cA4,bd=6,width=8,bg="white")
entrycF4 = Entry(f1,font=("Monserrat",20,'bold'),textvariable=cF4,bd=6,width=8,bg="white")
entrycA0.grid(row=1,column=1)
entrycA1.grid(row=2,column=1)
entrycA2.grid(row=3,column=1)
entrycA3.grid(row=4,column=1)
entrycA4.grid(row=5,column=1)
entrycF4.grid(row=6,column=1)

# Checkbox
checkMem = IntVar()
c = Checkbutton(root,font=("Monserrat",16,'bold'), text="Member", variable = checkMem, width=15,onvalue=1, offvalue=0,command=total)
c.deselect()
c.place(x=1125,y=270)

# Button 
buttonreset = Button(root,bd=5,fg="black",font=("Monserrat",16,'bold'),width=8,text="Reset",command=reset)
buttontotal = Button(root,bd=5,fg="black",font=("Monserrat",16,'bold'),width=8,text="Total",command=total)
buttontotal.place(x=1100,y=320)
buttonreset.place(x=1250,y=320)

root.mainloop() 
