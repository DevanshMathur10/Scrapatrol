from tkinter import *

def helpline_numbers():
    root2=Toplevel()
    root2.geometry("360x640")
    root2.title("EMERGENCY CONTACTS")
    bg=PhotoImage(file="C:/Users/DELL/Documents/VS/HACKATHONS/SCRAPATROL/backimg2.png")
    imglbl=Label(root2,image=bg)
    imglbl.place(x=0, y=0, relwidth=1, relheight=1)

    frame_3=Frame(root2,bg='#2E0063', relief=RAISED)
    frame_3.place(x=180,y=290,anchor='center')

    info3='''               CONTACT    ⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃
  Swachhata Pakhwada - 011-24360102
   Saahas Zero Waste - 18002586676

   Central Polution Control Board - 
         43102+(204/208/209)
    '''

    contact_display=Text(frame_3,height=8,width=37,wrap=WORD,font=("Consolas",12,'bold'),bg='#599e21',fg='#2a2f30')
    contact_display.insert(INSERT,info3)
    contact_display.grid(row=3,column=0)
    contact_display.configure(state='disabled')
    frame_3.mainloop()

#helpline_numbers()