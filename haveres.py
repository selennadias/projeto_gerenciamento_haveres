#importando as Blibiotecas
from tkinter import *
from tkinter import messagebox  # importar caixa de messangens(mensagens usuário)
from tkinter import ttk
import database   #importando o arquivo database para fazer a conexao com banco de dados 
from datetime import date #Bliblioteca para lidar com datas e horarios
import tkinter
from tkinter import simpledialog
from clientes import *
from operadores import *

def haver():
   #Criando jan3ela Login 
   jan3=Tk()  #atribuindo uma variável á uma jan3ela
   jan3.title('Acess Panel - Haveres') # Dando titulo a jan3ela
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
   TopFrameHav= Frame(jan3, width=1000, height=63, bg="black", relief="raise")
   TopFrameHav.pack(side=TOP)

   MenuFrameHav= Frame(jan3, width=1000, height=27, bg="#282828", relief="raise")
   MenuFrameHav.pack(side=TOP)

   FrameHav= Frame(jan3, width=1000, height=50, bg="#05A134", relief="raise")
   FrameHav.pack(side=TOP)

   HavFramHav= Frame(jan3, width=1000, height=527, bg="white", relief="raise")
   HavFramHav.pack(side=TOP)





   #Configurando o TopFrameHav
      # Colocando o icon Home

   logohCli=PhotoImage(file="img/home.png") 
   LogohomeCli = Label(TopFrameHav,image=logohCli,bg="black") 
   LogohomeCli.place(x=5, y=2)  #posicionando a iamgem


   data_atual = date.today()
   data_em_texto = "{}/{}".format(data_atual.day, data_atual.month)
   hj=date.today()
   dias =('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

   #supermecadoLabel = Label(TopFrameHav, text="Supermecado Alves",font=("Century Gothic",16),bg="black",fg="White")
   #supermecadoLabel.place(x=100, y=10)
   supLabelCli = Label(TopFrameHav, text="Supermecado Alves",font=("Century Gothic",12),bg="black",fg="White")
   supLabelCli.place(x=70, y=26)
   DataLabelCli = Label(TopFrameHav, text=data_em_texto,font=("Century Gothic",16),bg="black",fg="White")
   DataLabelCli.place(x=500, y=10)
   DiaLabelCli = Label(TopFrameHav, text=dias[hj.weekday()] ,font=("Century Gothic",10),bg="black",fg="White")
   DiaLabelCli.place(x=500, y=35)
   VindoLabelCli = Label(TopFrameHav, text="Bem Vindo",font=("Century Gothic",12),bg="black",fg="White")
   VindoLabelCli.place(x=580, y=12)

 

  
   def oper():
         JanOperadores()
    
     
   def cli():
        client()

  # def cliente():


   #Configurando o MenuFrameHav
   botao1Cli=Button(MenuFrameHav,text="Operadores",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1,command=oper)
   botao1Cli.place(x=200,y=5)
   botao2Cli=Button(MenuFrameHav,text="Cliente",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1,command=cli)
   botao2Cli.place(x=380,y=5)
   botao3Cli=Button(MenuFrameHav,text="Haveres",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1)
   botao3Cli.place(x=580,y=5)

   HavLabel=Label(FrameHav, text="HAVERES",font=("Century Gothic",16),bg="#05A134",fg="White")
   HavLabel.place(x=5, y=10)
 
   GerLabel = Label(HavFramHav, text="Gerenciamento Haveres",font=("Century Gothic",14),bg="white",fg="black")
   GerLabel.place(x=100, y=60)

   logo=PhotoImage(file="img/linha.png") 
   LogoLabel = Label(HavFramHav,image=logo,bg="white")  #carregando o logo através de um label.
   LogoLabel.place(x=100, y=82)  #posicionando a iamgem

   logon1=PhotoImage(file="img/haveres.png") 
   Logo1 = Label(HavFramHav,image=logon1,bg="white")  #carregando o logo através de um label.
   Logo1.place(x=25, y=60)  #posicionando a iamgem

   clien = StringVar()
   dinh = StringVar()

   def selecionar():
         root=Toplevel()
         root.title('Selection Clientes') # Dando titulo a jan3ela
         #jan3.geometry('1000x600') # Tamanho da jan3ela
         #jan3.configure (background ="#05A134") #Cor da jan3ela
         root.resizable(width=False, height=False) #tamanho fixo da jan3ela, nao podendo altera altura e largura e nem maximizala
         #root.attributes("-alpha",0.92) #deixa a jan3ela com transparência

         #centralizando a tela 
         window_height = 700
         window_width = 1000
         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()
         x_cordinate = int((screen_width/2) - (window_width/2))
         y_cordinate = int((screen_height/2) - (window_height/2))
         root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

         def zerar():
                lista .delete(0,"end")

         def buscar():

                consul=str(NomeCliEntry.get())
                database.cursor.execute('''
                SELECT idCli,nome FROM cliente WHERE nome LIKE %s
                ''',("%" + consul + "%",))
                rows = database.cursor.fetchall()
                if not rows:
                       messagebox.showinfo(title="Selection Info",message="Cliente Não Encontrado!!",parent=root)

                else:
                  zerar()
                  for results in rows:
                        insertData = str(results[0])+ '          '+ str(results[1])
                        lista.insert("end", insertData)
                     

         def sel():
                    result = lista.get(ACTIVE) 
                    id=result[0]
                    database.cursor.execute(''' 
                    select nome from cliente where idCli = %s
                    ''',(id))
                    rows = database.cursor.fetchall()
                    clien.set(rows[0][0])
                    root.destroy()
                    
                    
         
        
         
         seleCli = ttk.Button(root,  text="Selecionar", command=sel,width=15)
         seleCli.place(x=550,y=305)
               

         NomeCliLabel = Label(root, text="Nome :",font=("Century Gothic",12),fg="black")
         NomeCliLabel.place(x=7, y=35)
         NomeCliEntry= ttk.Entry(root,width=60) 
         NomeCliEntry.place(x=77, y=37)
         getCliButton = ttk.Button(root,  text="Buscar", command=buscar,width=15)
         getCliButton.place(x=450,y=35)
         

         scroll=Scrollbar(root)  
         scroll.place(x=920,y=190)
         lista=Listbox(root,width=150)
         lista.place(x=15, y=100)
         lista.config(yscrollcommand=scroll.set)  

         
         

         #clien.set("Maria Cristina")

   def somar():
      
        if not clien.get():
             messagebox.showinfo(title="Selection Info",message="Cliente não selecionado!!",parent=jan3)

        else:

             Adicionar = simpledialog.askstring(title = "Adicionando",
                                    prompt = "Entre com valor para Adionar:",parent=jan3)

             if Adicionar:
                  if not dinh.get():
                        dinh.set(Adicionar)
                  else:
                        hav=float(dinh.get())
                        maiss=float(Adicionar)
                        valor=hav + maiss
                        dinh.set(valor)
                        
      

   def Diminuir():
        if not dinh.get():
                 messagebox.showinfo(title="Selection Info",message="Não é possivel realizar a operação!!",parent=jan3)

        else:
               Diminuir= simpledialog.askstring(title = "Adicionando",
                        prompt = "Entre com valor para Subtrair:",parent=jan3)
            
               hav=float(dinh.get())
      
               if Diminuir:
                  menoss=float(Diminuir)
                  
                  if (hav >= menoss ):
                        valor=hav -menoss
                        dinh.set(valor)
                  
                  else:
                        messagebox.showinfo(title="Selection Info",message="Não é possivel realizar a operação!! Saldo Insuficiente",parent=jan3)
            
              


                    
        
            

   CLabel = Label(HavFramHav, text="Cliente",font=("Century Gothic",12),bg="white",fg="black")
   CLabel.place(x=100, y=135)
   getButton = ttk.Button(HavFramHav,  text="Selecionar", command=selecionar,width=15)
   getButton.place(x=180,y=135)
   CSLabel = ttk.Label(HavFramHav, textvariable=clien,background="White",font=("Century Gothic",12),relief="groove",width=45,padding=2)
   CSLabel.place(x=100, y=185)

   DinheiroLabel = Label(HavFramHav, text="Dinheiro",font=("Century Gothic",12),bg="white",fg="black")
   DinheiroLabel.place(x=100, y=250)
   CSLabel = ttk.Label(HavFramHav, textvariable=dinh,background="White",font=("Century Gothic",12),relief="groove",width=10,padding=2)
   CSLabel.place(x=190, y=250)
  
   mais=PhotoImage(file="img/ma.png") 
   MaisButton = Button(HavFramHav,image=mais,command=somar)  #carregando o logo através de um label.
   MaisButton.place(x=320, y=250)  

   Menos=PhotoImage(file="img/meno.png") 
   MenosButton = Button(HavFramHav,image=Menos,command=Diminuir)  #carregando o logo através de um label.
   MenosButton.place(x=360, y=250)  

   DinheiroLabel = Label(HavFramHav, text="Produtos",font=("Century Gothic",12),bg="white",fg="black")
   DinheiroLabel.place(x=100, y=310)

   #imagMais = PhotoImage(file="img/mai.png")





   jan3.mainloop()