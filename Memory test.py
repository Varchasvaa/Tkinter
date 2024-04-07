from tkinter import * 
from random import *

win=Tk()
win.geometry('600x600')
win.title("Memory")

label=Label(win,text="Testing",font=("timesnewroman",20))
label.place(x=250,y=250)
lives=Label(win,text="lives:",font=("timesnewroman",15))
lives.place(x=0,y=10)
value=Label(win,text="3",font=("timesnewroman",15))
value.place(x=52,y=10)
points=Label(win,text="0",font=("timesnewroman",20))
points.place(x=550,y=10)

dt=dict()
word=['Testing','deserve','wing', 'shock', 'letter', 'left', 'hose', 'fireman', 'deeply', 'empty', 'sneaky', 'stew']
d=dt.fromkeys(word,0)

def end():
    label.place(x=10,y=300)
    new.place(x=-100,y=0)
    seen.place(x=-100,y=0)
    label.configure(text="Ended",font=("timesnewroman",120))
    points.configure(text='points:'+str(int(points.cget("text"))+1),font=("timesnewroman",50))
    points.place(x=240,y=450)

def newb():
    words=choice(word)
    if d[label.cget('text')]==0:
        d[label.cget('text')]=int(d[label.cget('text')])+1
        points.configure(text=str(int(points.cget("text"))+1))
        label.configure(text=words)
    else:
        value.configure(text=str(int(value.cget('text'))-1))
        label.configure(text=words)
    print(d)
    if int(value.cget('text'))==0:
        new.after(100,lambda:end())

def seenb():
    words=choice(word)
    if d[label.cget('text')]>0:
        label.configure(text=words)
        points.configure(text=str(int(points.cget("text"))+1))
    else:
        value.configure(text=str(int(value.cget('text'))-1))
        label.configure(text=words)
    print(d)
    if int(value.cget('text'))==0:
        new.after(100,lambda:end())



new=Button(win,text="New",bd=10,font=("timesnewroman",10),fg='purple',bg="cyan",command=newb)
new.place(x=220,y=300)
seen=Button(win,text="Seen",font=("timesnewroman",10),bd=10,fg='purple',bg='cyan',command=seenb)
seen.place(x=320,y=300)


win.mainloop()