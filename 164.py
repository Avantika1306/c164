from tkinter import *

root=Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="Orchid1")
labelplanet=Label(root,text="Planet:",bg="Orchid2")
labelplanet.place(relx=0.2,rely=0.1,anchor=CENTER)
labelplanetname=Label(root,font=("courier",18,"bold"),bg="Orchid3")
labelplanetname.place(relx=0.5,rely=0.25,anchor=CENTER)
labelplanetimage=Label(root,bg="gold",highlightthickness=5,borderwidth=2,relief=SOLID)
labelplanetimage.place(relx=0.5,rely=0.5,anchor=CENTER)
labelgravityradius=Label(root,font=("Casttellar",18,"bold"))
labelgravityradius.place(relx=0.5,rely=0.8,anchor=CENTER)
labelinfo=Label(root,bg="Orchid4",wraplength="500")
labelinfo.place(relx=0.5,rely=0.9,anchor=CENTER) 
def showPlanetinfo():
    print("hi")
button1=Button(root,text="Show Planet Info",command=showPlanetinfo)
button1.place(relx=0.5,rely=0.18,anchor=CENTER)

root.mainloop()