from tkinter import *
import tkinter
root = Tk()
root.geometry("500x500")

scroll=Scrollbar(root)  
scroll.place(x=300,y=90)
listbox = Listbox(root,exportselection=0)
listbox.insert(END, "Selecione")
listbox.config(yscrollcommand=scroll.set)
listbox.place(x=50,y=70)

for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]:
  listbox.insert(END, item)

scroll2=Scrollbar(root)  
scroll2.place(x=330,y=90)
listbox2 = Listbox(root,exportselection=0)
listbox2.pack()
listbox2.insert(END, "Selecione")
listbox2.config(yscrollcommand=scroll2.set)
listbox2.place(x=175,y=70)

for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]:
  listbox2.insert(END, item)

# Criei uma função:
listbox2.config(state=tkinter.DISABLED)

def chamada(event):
  global listbox2

 # print(event.x)
 # print(event.y)
  index = int(listbox.curselection()[0])
 # print(index)
  listbox2.select_set(index)

# E atribui a função ao evento do clique do mouse na
# primeira listbox:

listbox.bind("<Button-1>",chamada)


root.mainloop()