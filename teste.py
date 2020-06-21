

from tkinter import *
from tkinter import messagebox  # importar caixa de messangens(mensagens usuário)
from tkinter import ttk
import database   #importando o arquivo database para fazer a conexao com banco de dados 
from datetime import date #Bliblioteca para lidar com datas e horarios
import tkinter
from tkinter import simpledialog
from clientes import *
from operadores import *
from tkinter import ttk 
import tkinter as tk 
  
# Creating tkinter jan3 
jan3 = Tk() 
jan3.geometry('1180x1000')

  
# Using treeview widget 
treev = ttk.Treeview(jan3, selectmode ='browse') 



  
# Calling pack method w.r.to treeview 
treev.place(x=500, y=430)

  
# Constructing vertical scrollbar 
# with treeview 
verscrlbar = Scrollbar(jan3,  
                           orient ="vertical",  
                           command = treev.yview) 
  
# Calling pack method w.r.to verical  
# scrollbar 
verscrlbar.place(x=800, y=489) 
  
# Configuring treeview 
treev.configure(xscrollcommand = verscrlbar.set) 
  
# Defining number of columns 
treev["columns"] = ("1", "2", "3") 
  
# Defining heading 
treev['show'] = 'headings'
  
# Assigning the width and anchor to  the 
# respective columns 
treev.column("1", width = 90, anchor ='c') 
treev.column("2", width = 90, anchor ='se') 
treev.column("3", width = 90, anchor ='se') 
  
# Assigning the heading names to the  
# respective columns 
treev.heading("1", text ="Id") 
treev.heading("2", text ="Produto") 
treev.heading("3", text ="Quantidade") 
  



def AdicionarPro():
      treev.insert("", 'end', text ="", 
            values =("aaa", "22", "00")) 
  
AdicionarButton = ttk.Button(jan3, text="Adicionar",command=AdicionarPro, width=15)
AdicionarButton.place(x=15,y=100)

# Calling mainloop 
jan3.mainloop() 