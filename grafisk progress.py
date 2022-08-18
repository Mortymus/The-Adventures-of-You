from tkinter import *

root=Tk()
root.geometry('300x450')
root.configure(bg='beige')

#Frames

topframe=Frame(root,)
topframe.pack()
middleframe=Frame(root, width=800,height=1400, bg='beige')
middleframe.propagate(0)
middleframe.pack()
spaceframe1=Frame(root, height=100)
spaceframe1.pack()
bottomframe=Frame(root, bg='beige')
bottomframe.pack()
spaceframe2=Frame(root, height=100)
spaceframe2.pack()
quitframe=Frame(root, bg='beige')
quitframe.pack()

headline=Label(topframe, text='''
---The Amazing Adventures of You---
''', bg='beige')
headline.pack()

frames=[topframe,middleframe,spaceframe1,bottomframe,spaceframe2,quitframe,headline,root]

intro='''
Du våkne i et brennande hus.

A Du håppe ud vinduet.
B Du springe gjønå flammene.
'''
Label(middleframe, text=intro, bg='beige').pack()

# Functions

countq=0
def quitting():
		global countq
		countq+=1
		if countq==1:
			for content in middleframe.winfo_children():
				content.destroy()
			buttona.destroy()
			buttonb.destroy()
			buttonq.destroy()
			for f in frames:
				f.configure(bg='beige')
			Label(middleframe, text="""
(: Thank you for playing :)
		
...please don't have nightmares...
""", bg='beige').pack(side=BOTTOM)
			root.after(5000, root.destroy)

# Buttons

buttona=Button(bottomframe,text='    A    ',bg='lightgreen', activebackground='green')
buttona.pack(side=LEFT)
buttonb=Button(bottomframe, text='    B    ', bg='lightgreen', activebackground='green')
buttonb.pack()
buttonq=Button(quitframe,text='           Quit           ',command=quitting, bg='orange', activebackground='red')
buttonq.pack()

# Story

a='''
D e 5 meter ner te betongen, du skamslår
deg å svime av.

Du våkne av at håret ditt brenne...

A Skrig.
B Grin.
'''


root.mainloop()