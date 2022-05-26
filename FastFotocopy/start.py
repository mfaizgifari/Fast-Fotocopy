from tkinter import *

# Set-up awal GUI 
root = Tk()
root.title("Fast Fotocopy")
root.geometry("800x600")
root.resizable(False,False)
canvas = Canvas(root)

class start:
    def __init__(self,root1):
        self.root = root1
               
        canvas = Canvas(self.root)
        canvas.create_text(400,200,text="Fast",fill="black",font=("Paladins Laser",60))
        canvas.create_text(400,270,text="Fotocopy",fill="black",font=("Paladins Laser",60))
        canvas.create_text(400,310,text="By: Muhamad Faiz Gifari",fill="black",font=("Montserrat",12))
        canvas.pack(fill="both",expand=True)  
   
def btnmasuk():
    root.destroy()
    import menu

startbutton = PhotoImage(file="start.png")
button_start = Button(root,bd=0,fg="black",image=startbutton, command=btnmasuk)
button_start.pack(pady=50,padx=20,side=BOTTOM)

    
obj = start(root)


root.mainloop()