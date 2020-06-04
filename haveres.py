#importando as Blibiotecas
from tkinter import *
from tkinter import messagebox  # importar caixa de messangens(mensagens usuário)
from tkinter import ttk
import database   #importando o arquivo database para fazer a conexao com banco de dados 
from datetime import date #Bliblioteca para lidar com datas e horarios
import tkinter
from clientes import *
from operadores import *

def haver():
   #Criando jan3ela Login 
   jan3=Tk()  #atribuindo uma variável á uma jan3ela
   jan3.title('Acess Panel - Operadores') # Dando titulo a jan3ela
   #jan3.geometry('1000x600') # Tamanho da jan3ela
   #jan3.configure (background ="#05A134") #Cor da jan3ela
   jan3.resizable(width=False, height=False) #tamanho fixo da jan3ela, nao podendo altera altura e largura e nem maximizala
   jan3.attributes("-alpha",0.92) #deixa a jan3ela com transparência


   #centralizando a tela 
   window_height = 700
   window_width = 1000
   screen_width = jan3.winfo_screenwidth()
   screen_height = jan3.winfo_screenheight()
   x_cordinate = int((screen_width/2) - (window_width/2))
   y_cordinate = int((screen_height/2) - (window_height/2))
   jan3.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

   #Separando a  jan3ela em 4 partes
   TopFrameCli= Frame(jan3, width=1000, height=63, bg="black", relief="raise")
   TopFrameCli.pack(side=TOP)

   MenuFrameCli= Frame(jan3, width=1000, height=27, bg="#282828", relief="raise")
   MenuFrameCli.pack(side=TOP)

   DrowFrameCli= Frame(jan3, width=1000, height=50, bg="#05A134", relief="raise")
   DrowFrameCli.pack(side=TOP)

   ClienteFramrCli= Frame(jan3, width=1000, height=527, bg="white", relief="raise")
   ClienteFramrCli.pack(side=TOP)





   #Configurando o TopFrameCli
      # Colocando o icon Home

   logohCli=PhotoImage(file="img/home.png") 
   LogohomeCli = Label(TopFrameCli,image=logohCli,bg="black") 
   LogohomeCli.place(x=5, y=2)  #posicionando a iamgem


   data_atual = date.today()
   data_em_texto = "{}/{}".format(data_atual.day, data_atual.month)
   hj=date.today()
   dias =('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

   #supermecadoLabel = Label(TopFrameCli, text="Supermecado Alves",font=("Century Gothic",16),bg="black",fg="White")
   #supermecadoLabel.place(x=100, y=10)
   supLabelCli = Label(TopFrameCli, text="Supermecado Alves",font=("Century Gothic",12),bg="black",fg="White")
   supLabelCli.place(x=70, y=26)
   DataLabelCli = Label(TopFrameCli, text=data_em_texto,font=("Century Gothic",16),bg="black",fg="White")
   DataLabelCli.place(x=500, y=10)
   DiaLabelCli = Label(TopFrameCli, text=dias[hj.weekday()] ,font=("Century Gothic",10),bg="black",fg="White")
   DiaLabelCli.place(x=500, y=35)
   VindoLabelCli = Label(TopFrameCli, text="Bem Vindo",font=("Century Gothic",12),bg="black",fg="White")
   VindoLabelCli.place(x=580, y=12)




   #Configurando o DrowFrameCli
   nomeLabelCli = Label(DrowFrameCli, text="HAVERES",font=("Century Gothic",16),bg="#05A134",fg="White")
   nomeLabelCli.place(x=5, y=10)

  
   def oper():
         JanOperadores()
    
     
   def cli():
        client()

  # def cliente():


   #Configurando o MenuFrameCli
   botao1Cli=Button(MenuFrameCli,text="Operadores",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1,command=oper)
   botao1Cli.place(x=200,y=5)
   botao2Cli=Button(MenuFrameCli,text="Cliente",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1,command=cli)
   botao2Cli.place(x=380,y=5)
   botao3Cli=Button(MenuFrameCli,text="Haveres",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1)
   botao3Cli.place(x=580,y=5)


   jan3.mainloop()