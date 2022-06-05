from tkinter import *
from tkvideo import tkvideo
from location import locshow
from articles import articles
from contact import helpline_numbers

root=Tk()
root.geometry("360x640")
root.title("SCRAPATROL")
imglbl=Label(root)
imglbl.place(x=0, y=0, relwidth=1, relheight=1)
player = tkvideo("C:/Users/DELL/Documents/VS/HACKATHONS/SCRAPATROL/backvid1.mp4", imglbl,loop = 1, size = (360,640))
player.play()

frame0=Frame(root,relief=RAISED,bg='#7be3ab',highlightbackground="#32a885", highlightthickness=7)
frame0.place(x=180,y=180,anchor='center')

sd=Label(frame0,text="DAILY WASTE\nMANAGEMENT\nSCHEDULE",bg='#7be3ab',font=('Century',14,'bold'))
sd.grid(row=0,column=0,columnspan=2,ipadx=50,ipady=10)

lb1=Label(frame0,text="Degradable\nWaste (kg)",bg='#7be3ab',font=('Consolas',9,'bold'))
lb1.grid(row=1,column=0)
lb2=Label(frame0,text="Non-Degradable\nWaste (kg)",bg='#7be3ab',font=('Consolas',9,'bold'))
lb2.grid(row=2,column=0)
lb3=Label(frame0,text="Liquid\nWaste(kg)",bg='#7be3ab',font=('Consolas',9,'bold'))
lb3.grid(row=3,column=0)
sl1=Scale(frame0,from_=0,to=5,orient=HORIZONTAL,bg='#7be3ab')
sl1.grid(row=1,column=1,pady=2)
sl2=Scale(frame0,from_=0,to=5,orient=HORIZONTAL,bg='#7be3ab')
sl2.grid(row=2,column=1,pady=2)
sl3=Scale(frame0,from_=0,to=5,orient=HORIZONTAL,bg='#7be3ab')
sl3.grid(row=3,column=1,pady=(2,10))

disposal=IntVar()
label_s = Label(frame0,text="0/15",font=("Century", 25,'bold'), bg="#32a885") 
label_s.grid(row=4, column=0,columnspan=2,sticky=W+E,ipadx=8)

def update():
    disposal.set(disposal.get()+int(sl1.get())+int(sl2.get())+int(sl3.get()))
    label_s.config(text=str(disposal.get())+"/15")
    if disposal.get()>=15:
        label_s.config(text="15/15")
        labeln = Label(frame0,text="GREAT JOB !",font=("HelvLight", 11), bg="#32a885", fg="#3d3842")
        labeln.place(x=135,y=296,anchor='center')

upd=Button(frame0,text="UPDATE DISPOSAL", bg="#32a885",command=update)
upd.grid(row=5,column=0,columnspan=2,ipadx=10,pady=(20,7))

frame1=Frame(root, relief=RAISED)
frame1.place(x=180,y=410,anchor='center')
artbtn=Button(frame1,bg='#8ccfab',text="Waste\nManagement\nArticles",font=('Candara',10,'bold'),command=articles)
artbtn.grid(row=0,column=0,columnspan=2,ipadx=50,ipady=20)

frame2=Frame(root, relief=RAISED)
frame2.place(x=180,y=510,anchor='center')
showbtn=Button(frame2,bg='#8ccfab',text="Waste\nCollector\nLocations",font=('Candara',10,'bold'),command=locshow)
showbtn.grid(row=0,column=0,columnspan=2,ipady=10,ipadx=61)

frame4=Frame(root, relief=RAISED)
frame4.place(x=180,y=595,anchor='center')
sendbtn=Button(frame4,bg='#8ccfab',text="CONTACT",font=('Candara',10,'bold'),command=helpline_numbers)
sendbtn.grid(row=0,column=0,columnspan=2,ipady=20,ipadx=60)

root.mainloop()
