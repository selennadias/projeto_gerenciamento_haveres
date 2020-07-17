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
import operator
try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk

def haver():
   #Criando jan3ela Login 
   jan3=Tk()  #atribuindo uma variável á uma jan3ela
   jan3.title('Acess Panel - Haveres') # Dando titulo a jan3ela
   #jan3.geometry('1000x600') # Tamanho da jan3ela
   #jan3.configure (background ="#05A134") #Cor da jan3ela
   jan3.resizable(width=False, height=False) #tamanho fixo da jan3ela, nao podendo altera altura e largura e nem maximizala
   jan3.attributes("-alpha",0.92) #deixa a jan3ela com transparência


   #centralizando a tela 
   window_height = 710
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

 
  
   def Prodd():
        
        jan4=Toplevel() #atribuindo uma variável á uma jan4ela
        jan4.title('Acess Panel - Produto') # Dando titulo a jan4ela
        jan4.resizable(width=False, height=False) #tamanho fixo da jan4ela, nao podendo altera altura e largura e nem maximizala
        jan4.attributes("-alpha",0.92) #deixa a jan4ela com transparência
        jan4.transient()#
        jan4.focus_force()#
        jan4.grab_set()#
        


        #centralizando a tela    
        window_height = 680   
        window_width = 900
        screen_width = jan4.winfo_screenwidth()
        screen_height = jan4.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        jan4.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

            #Separando a  jan4ela em 4 partes
        TopFrame2= Frame(jan4, width=900, height=100, bg="black", relief="raise")
        TopFrame2.pack(side=TOP)

        DrowFrame2= Frame(jan4, width=900, height=50, bg="#05A134", relief="raise")
        DrowFrame2.pack(side=TOP)

        ProdutoFrame1= Frame(jan4, width=900, height=527, bg="white", relief="raise")
        ProdutoFrame1.pack(side=TOP)





            #Configurando o TopFrame2
            # Colocando o icon Home

        logoh=PhotoImage(file="img/home.png") 
        Logohome = Label(TopFrame2,image=logoh,bg="black") 
        Logohome.place(x=5, y=2)  #posicionando a iamgem


        data_atual = date.today()
        data_em_texto = "{}/{}".format(data_atual.day, data_atual.month)
        hj=date.today()
        dias =('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

            #supermecadoLabel = Label(TopFrame2, text="Supermecado Alves",font=("Century Gothic",16),bg="black",fg="White")
            #supermecadoLabel.place(x=100, y=10)
        supLabel = Label(TopFrame2, text="Supermecado Alves",font=("Century Gothic",12),bg="black",fg="White")
        supLabel.place(x=70, y=26)
        DataLabel = Label(TopFrame2, text=data_em_texto,font=("Century Gothic",16),bg="black",fg="White")
        DataLabel.place(x=500, y=10)
        DiaLabel = Label(TopFrame2, text=dias[hj.weekday()] ,font=("Century Gothic",10),bg="black",fg="White")
        DiaLabel.place(x=500, y=35)
        VindoLabel = Label(TopFrame2, text="Bem Vindo",font=("Century Gothic",12),bg="black",fg="White")
        VindoLabel.place(x=580, y=12)




            #Configurando o DrowFrame2
        nomeLabel = Label(DrowFrame2, text="PRODUTO",font=("Century Gothic",16),bg="#05A134",fg="White")
        nomeLabel.place(x=5, y=10)

        


            #Configurando o ProdutoFrame1

        cliLabel = Label(ProdutoFrame1, text="Ficha Cadastral Produto",font=("Century Gothic",14),bg="white",fg="black")
        cliLabel.place(x=100, y=60)

        logo=PhotoImage(file="img/linha.png") 
        LogoLabel = Label(ProdutoFrame1,image=logo,bg="white")  #carregando o logo através de um label.
        LogoLabel.place(x=100, y=82)  #posicionando a iamgem

        logon1=PhotoImage(file="img/n3.png") 
        Logo1 = Label(ProdutoFrame1,image=logon1,bg="white")  #carregando o logo através de um label.
        Logo1.place(x=25, y=60)  #posicionando a iamgem




                #Criando os campos
                #Criando Label Nome
        idPro=Label(ProdutoFrame1, text='Enter ID:',font=("Century Gothic",12),bg="white",fg="black")
        idPro.place(x=10,y=120)
        idProEntry= ttk.Entry(ProdutoFrame1,width=60) 
        idProEntry.place(x=95, y=124)
        DescLabel = Label(ProdutoFrame1, text="Produto :",font=("Century Gothic",12),bg="white",fg="black")
        DescLabel.place(x=10, y=160)
        NomeProEntry= ttk.Entry(ProdutoFrame1,width=60) 
        NomeProEntry.place(x=95, y=164)
        TelefoneCliLabel = Label(ProdutoFrame1, text=
        "Descrição:",font=("Century Gothic",12),bg="white",fg="black")
        TelefoneCliLabel.place(x=10, y=200)
        CategoriaEntry=ttk.Entry(ProdutoFrame1,width=60) 
        CategoriaEntry.place(x=95, y=204)


    
        
        

        

    
        def salvar():
        

                try:
                    
                    

                    id=idProEntry.get()
                    descri=NomeProEntry.get()
                    categ=CategoriaEntry.get()
                

                    if(not descri):
                        messagebox.showinfo("Insert status", "Erro!!  Campos Vazios",parent=jan4)
                    else:

                        database.cursor.execute('''
                        insert into produtos(IDprod,descricao,categoria) 
                        values(%s,%s,%s)
                        ''',(id,descri,categ))
                        database.db.commit()

                    
                        messagebox.showinfo(title="Register Info",message="Salvo com Sucesso!!",parent=jan4)
                        idProEntry.delete(0, 'end')
                        NomeProEntry.delete(0, 'end')#limpa o label Nome
                        CategoriaEntry.delete(0, 'end')#limpa o label telefone
                        treev4.delete(*treev4.get_children())
                        database.cursor.execute('''
                        SELECT * FROM produtos''')
                        rows = database.cursor.fetchall()
                    
                        for results in rows:
                            treev4.insert("", 'end', text ="", 
                                        values =(results[0], results[1]))

                        treev1.delete(*treev1.get_children())
                        for results in rows:
                            treev1.insert("", 'end', text ="", 
                                        values =(results[0], results[1]))

                    
                
                except:
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan4)

        def excluir():
                try: 
                    id=idProEntry.get()
                    if(idProEntry.get() == ""):
                            messagebox.showinfo("Delete Status", "ID não informado",parent=jan4)
                    else:
                        
                        database.cursor.execute('''
                        delete from produtos where IDprod= %s
                        ''',(id))
                        database.db.commit()
                        messagebox.showinfo(title="Register Info",message="Deletado com sucesso!!",parent=jan4)
                        idProEntry.delete(0, 'end')
                        NomeProEntry.delete(0, 'end')
                        CategoriaEntry.delete(0, 'end')
                        
                        treev4.delete(*treev4.get_children())
                        database.cursor.execute('''
                        SELECT * FROM produtos''')
                        rows = database.cursor.fetchall()
                    
                        for results in rows:
                            treev4.insert("", 'end', text ="", 
                                        values =(results[0], results[1]))
                        
                
                except:
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan4)

        def limpar():
                    
                    

                    idProEntry.delete(0, 'end')
                    NomeProEntry.delete(0, 'end')
                    CategoriaEntry.delete(0, 'end')
                
        def selecionar():
                try: 
                    
                        result =treev4.item(treev4.selection()) ["values"]
                        id=int(result[0])
                    
                        database.cursor.execute('''
                        SELECT * FROM produtos WHERE IDprod=%s;
                        ''',[id])
                        rows = database.cursor.fetchall()
                    
                        idProEntry.delete(0,'end')
                        NomeProEntry.delete(0, 'end')#limpa o label Nome
                        CategoriaEntry.delete(0, 'end')#limpa o label telefone
                    


                    
                        for row in rows:
                            idProEntry.insert(0,row[0])
                            NomeProEntry.insert(0,row[1])
                            if row[2]:
                             CategoriaEntry.insert(0,row[2])
                    
                        
                        
                except:
                        
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan4)
                
        def alterar():
                try: 
                    id=idProEntry.get()
                    nome=NomeProEntry.get()
                    categoria=CategoriaEntry.get()
            
                    if(id=="" or nome==""):
                        messagebox.showinfo("Insert status", "Erro!!  Campos Vazios",parent=jan4)
                    else:
                        
                        database.cursor.execute('''
                        update produtos set descricao=%s,categoria=%s  where IDprod=%s
                        ''',(nome,categoria,id))
                        database.db.commit()
                        messagebox.showinfo(title="Register Info",message="Atualizado com Sucesso!!",parent=jan4)
                        idProEntry.delete(0, 'end')
                        NomeProEntry.delete(0, 'end')#limpa o label Nome
                        CategoriaEntry.delete(0, 'end')#limpa o label telefone
                        treev4.delete(*treev4.get_children())
                        database.cursor.execute('''
                        SELECT * FROM produtos''')
                        rows = database.cursor.fetchall()
                    
                        for results in rows:
                            treev4.insert("", 'end', text ="", 
                                        values =(results[0], results[1]))

                except:
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan4)
                        
        
        def showPro():
            
            database.cursor.execute('''
            SELECT * FROM produtos''')
            rows = database.cursor.fetchall()
                    
            for results in rows:
                    treev4.insert("", 'end', text ="", 
                                        values =(results[0], results[1]))



        def zerar():
            treev4.delete(*treev4.get_children())


        imag = PhotoImage(file="img/lim.png")
        limparButton = Button(ProdutoFrame1,bd=0,default=DISABLED,image=imag,command=limpar)
        limparButton.place(x=375,y=320)

    #  photo01 = PhotoImage(file="img/iconsalvar.png")
        salvarButton = ttk.Button(ProdutoFrame1, text="Salvar",command=salvar, width=15)
        salvarButton.place(x=140,y=410)

    #  photo02 = PhotoImage(file="img/iconExcluir.png")
        deleteButton = ttk.Button(ProdutoFrame1,  text="Excluir", command=excluir,width=15)
        deleteButton.place(x=260,y=410)

        photo03 = PhotoImage(file="img/selectIcon.png")
        updateButton = ttk.Button(ProdutoFrame1, image=photo03, command=selecionar)
        updateButton.place(x=550,y=305)

        #photo04 = PhotoImage(file="img/alterarIcon.png")
        getButton = ttk.Button(ProdutoFrame1,  text="Alterar", command=alterar,width=15)
        getButton.place(x=380,y=410)
        '''
        scroll=Scrollbar(ProdutoFrame1)  
        scroll.place(x=750,y=160)
        lista=Listbox(ProdutoFrame1,width=40)
        lista.place(x=500, y=122)
        lista.config(yscrollcommand=scroll.set)
        show()
        '''
        treev4 = ttk.Treeview(ProdutoFrame1, selectmode ='browse',height="7") 
        treev4.place(x=500, y=122)
        verscrlbar1 = Scrollbar(ProdutoFrame1,  
                            orient ="vertical",  
                            command = treev4.yview) 
        verscrlbar1.place(x=750,y=200)
        treev4.configure(xscrollcommand = verscrlbar1.set) 
        treev4["columns"] = ("1", "2") 
        treev4['show'] = 'headings'
        treev4.column("1", width = 60, anchor ='c') 
        treev4.column("2", width = 180, anchor ='nw') 
        treev4.heading("1", text ="Id") 
        treev4.heading("2", text ="Produto") 
        showPro()
        
        jan4.mainloop()
  
   def oper():
         JanOperadores()
    
     
   def cli():
        client()
      
   def produtos():
      Prodd()

  # def cliente():


   #Configurando o MenuFrameHav
   botao1Cli=Button(MenuFrameHav,text="Operadores",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1,command=oper)
   botao1Cli.place(x=200,y=5)
   botao2Cli=Button(MenuFrameHav,text="Cliente",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1,command=cli)
   botao2Cli.place(x=380,y=5)
   botao3Cli=Button(MenuFrameHav,text="Produtos",activeforeground="red",default=DISABLED, highlightbackground="gray",highlightcolor="white",width=15,bg='#282828',highlightthickness=0,fg='white',bd=0.1,command=produtos)
   botao3Cli.place(x=580,y=5)

   HavLabel=Label(FrameHav, text="HAVERES",font=("Century Gothic",16),bg="#05A134",fg="White")
   HavLabel.place(x=5, y=10)
 
   GerLabel = Label(HavFramHav, text="Gerenciamento Haveres",font=("Century Gothic",14),bg="white",fg="black")
   GerLabel.place(x=100, y=30)

   logo=PhotoImage(file="img/linha.png") 
   LogoLabel = Label(HavFramHav,image=logo,bg="white")  #carregando o logo através de um label.
   LogoLabel.place(x=100, y=52)  #posicionando a iamgem

   logon1=PhotoImage(file="img/haveres.png") 
   Logo1 = Label(HavFramHav,image=logon1,bg="white")  #carregando o logo através de um label.
   Logo1.place(x=25, y=30)  #posicionando a iamgem

   clien = StringVar()
   dinh = StringVar()
   codi = StringVar()
   idp= StringVar()
   nomeP= StringVar()

   def selecionar():
         root=Toplevel()
         root.title('Selection Clientes') # Dando titulo a jan3ela
         #jan3.geometry('1000x600') # Tamanho da jan3ela
         #jan3.configure (background ="#05A134") #Cor da jan3ela
         root.resizable(width=False, height=False) #tamanho fixo da jan3ela, nao podendo altera altura e largura e nem maximizala
         root.configure (background ="white")
         root.attributes("-alpha",0.98) #deixa a jan3ela com transparência

         #centralizando a tela 
         window_height = 545
         window_width = 600
         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()
         x_cordinate = int((screen_width/2) - (window_width/2))
         y_cordinate = int((screen_height/2) - (window_height/2))
         root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

         frameClie= Frame(root, width=600, height=100, bg="#18A844", relief="raise")
         frameClie.pack(side=TOP)


         def zerar():
               tree.delete(*tree.get_children())


         def buscar():

           
                        consul=str(NomeCliEntry.get())
                        database.cursor.execute('''
                        SELECT idCli,nome,cpf,telefone FROM cliente WHERE nome LIKE %s
                        ''',("%" + consul + "%",))
                        rows = database.cursor.fetchall()
                        if not rows:
                              messagebox.showinfo(title="Selection Info",message="Cliente Não Encontrado!!",parent=root)

                        else:
                              zerar()
                              for results in rows:
                                    tree.insert("", 'end', text ="", 
                                                values =(results[0], results[1], results[2]))
                        

         def sel():
                  
                treev.delete(*treev.get_children())
                dados =tree.item(tree.selection()) ["values"]
                
              
                if not dados:
                        messagebox.showinfo(title="Aviso",message="Cliente não selecionado",parent=root)
                else:
                    
                    clien.set(dados[1])
                    codi.set(dados[0])
                    
                   
                    iCli=str(dados[0])
                    print(iCli)
                    

                    database.cursor.execute('''
                    SELECT * FROM haveres where IDclientes=%s
                    ''',iCli)
                    rows = database.cursor.fetchall()
                    

                    if not rows:
                                dinh.set("0")
                        
                    else:
                        dinne=float(rows[0][3])
                        if(not  dinne):
                            dinh.set("0")
                        else:
                              dinh.set(dinne)  


                   
                    database.cursor.execute('''
                    SELECT id,nome,qtde FROM haveres_produto WHERE doc =%s
                    ''',([iCli]))
                    dad = database.cursor.fetchall()
                    print(dad)
                    index = iid = 0
                    for results in dad:
    
                              treev.insert("", index, iid, values=results)
                              index = iid = index + 1

                    root.destroy()
                 
                  
      

                    


                    
                  
                  
         
          
         bLabel = Label(frameClie, text="Selecionar Cliente",font=("Century Gothic",16),bg="#18A844",fg="white")
         bLabel.place(x=200, y=35)
         imapro=PhotoImage(file="img/fot03.png")     
         log2 = Label(frameClie, image=imapro,bg="#18A844")
         log2.photo = imapro  # Para colocar imagem no ToopLevel
         log2.place(x=50, y=5)  #posicionando a iamgem
    

         seleCli = ttk.Button(root,  text="Selecionar", command=sel,width=15)
         seleCli.place(x=445,y=450)
         
               

         NomeCliLabel = Label(root, text="Nome :",font=("Century Gothic",12),fg="black",bg="white")
         NomeCliLabel.place(x=20, y=130)
         NomeCliEntry= ttk.Entry(root,width=50) 
         NomeCliEntry.place(x=90, y=132)
         getCliButton = ttk.Button(root,  text="Buscar", command=buscar,width=15)
         getCliButton.place(x=290,y=166)
  

         tree = ttk.Treeview(root, selectmode ='browse') 
         tree.place(x=60, y=215)
         verscrlba = Scrollbar(root,  
                              orient ="vertical",  
                              command = tree.yview)  
         verscrlba.place(x=548, y=300) 
         tree.configure(xscrollcommand = verscrlba.set) 
         tree["columns"] = ("1", "2","3") 
         tree['show'] = 'headings'
         tree.column("1", width = 80, anchor ='c') 
         treev.column("2", width = 100, anchor ='se') 
         treev.column("3", width = 100, anchor ='se') 
     
         tree.heading("1", text ="Id") 
         tree.heading("2", text ="Cliente") 
         tree.heading("3", text ="CPF") 
      
      
      
  


         '''
         tree=ttk.Treeview(root,height=10,column=2)
         tree.place(x=15, y=100)
         # tree.place(,column=0,columnspan=2)
         tree.heading('#0',text="Código",anchor=CENTER)
         tree.heading('#1',text="Cliente",anchor=CENTER)
         '''
        
         
         '''
         scroll=Scrollbar(root)  
         scroll.place(x=920,y=190)
         lista=Listbox(root,width=150)
         lista.place(x=15, y=100)
         lista.config(yscrollcommand=scroll.set)  
         '''

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
   CLabel.place(x=100, y=105)
   getButton = ttk.Button(HavFramHav,  text="Selecionar", command=selecionar,width=15)
   getButton.place(x=180,y=105)

   ConsHav = ttk.Button(HavFramHav,  text="Conultar Haveres", command=selecionar,width=15)
   ConsHav.place(x=670,y=180)
   consulta1=PhotoImage(file="img/haverescad.png") 
   imgcons = Label(HavFramHav,image=consulta1,bg="white")  #carregando o logo através de um label.
   imgcons.place(x=670, y=90)

   CSLabel = ttk.Label(HavFramHav, textvariable=clien,background="White",font=("Century Gothic",12),relief="groove",width=45,padding=2)
   CSLabel.place(x=145, y=150)
   CooLabel = ttk.Label(HavFramHav, textvariable=codi,background="White",font=("Century Gothic",12),relief="groove",width=4,padding=2)
   CooLabel.place(x=100, y=150)

   DinheiroLabel = Label(HavFramHav, text="Dinheiro",font=("Century Gothic",12),bg="white",fg="black")
   DinheiroLabel.place(x=100, y=200)
   CSLabel = ttk.Label(HavFramHav, textvariable=dinh,background="White",font=("Century Gothic",12),relief="groove",width=10,padding=2)
   CSLabel.place(x=190, y=200)
  
   mais=PhotoImage(file="img/ma.png") 
   MaisButton = Button(HavFramHav,image=mais,command=somar)  #carregando o logo através de um label.
   MaisButton.place(x=320, y=200)  

   Menos=PhotoImage(file="img/meno.png") 
   MenosButton = Button(HavFramHav,image=Menos,command=Diminuir)  #carregando o logo através de um label.
   MenosButton.place(x=360, y=200)  

   DinheiroLabel = Label(HavFramHav, text="Produtos á Selecionar",font=("Century Gothic",12),bg="white",fg="black")
   DinheiroLabel.place(x=100, y=250)

   DinheiroLabel = Label(HavFramHav, text="Produtos em Haver",font=("Century Gothic",12),bg="white",fg="black")
   DinheiroLabel.place(x=500, y=250)

   #imagMais = PhotoImage(file="img/mai.png")

 
   def salvarBD():
                
               
                if not clien.get():
                        messagebox.showinfo(title="Selection Info",message="Cliente não selecionado!!",parent=jan3)

                else:

                 # curItem = treev.focus()
                 #print (treev.item(curItem))

                  id=codi.get()
                  din=dinh.get()
                  doc=codi.get()
                  try:
                        if not dinh.get():
                              din=0
                        print(din)
                        
                        doc=codi.get()
                        database.cursor.execute('''
                        insert into haveres(IDclientes,dinheiro,documento) 
                        values(%s, %s, %s)
                        ''',(id,din,doc))
                        database.db.commit()
                        codi.set("")
                        clien.set("")
                        dinh.set("")

                        messagebox.showinfo(title="Selection Info",message="Salvo com sucesso!!",parent=jan3)
                  except:
                        messagebox.showinfo(title="Selection Info",message="Erro!!",parent=jan3)
                        

                        
                     
  
  
      
   def alterarBD():
         print("Alterou")

   def showPro():
         
          database.cursor.execute('''
          SELECT * FROM produtos''')
          rows = database.cursor.fetchall()
                
          for results in rows:
                treev1.insert("", 'end', text ="", 
                                    values =(results[0], results[1]))

   
 
                  
   def showtreev(dooc):
          
          
          database.cursor.execute('''
          SELECT * FROM haveres_produto where doc=%s
          ''',(dooc))
          rows = database.cursor.fetchall()
                
          for results in rows:
                treev.insert("", 'end', text ="", 
                                    values =(results[0], results[1], results[2]))
                     
                     
                

   def AdicionarPro():
          
                  if (not clien.get()) or (not QuantidadeCliEntry.get()):
                        messagebox.showinfo(title="Selection Info",message="Campos Vazios!!!ke",parent=jan3)


                  else:     
                              
                              dados = treev1.item(treev1.selection()) ["values"]
                              idp=dados[0]
                              nomeP=dados[1]
                              #print(idp)
                              #print(nomeP)
                              '''
                              children = treev.get_children("")
                              for child in children:
                                     values = treev.item(child, "values")
                              if idp==values[0] 
                                 messagebox.showinfo(title="Aviso",message="Nao é possivel adionar, apenas Alterar!!!")
                              
                              else:
                              '''
                              treev.insert("", 'end', text ="", 
                              values =(dados[0],dados[1], QuantidadeCliEntry.get()))
                              doce=codi.get()
                              database.cursor.execute('''
                              insert into haveres_produto(doc,id,nome,qtde) 
                              values(%s, %s, %s,%s)
                              ''',(doce,dados[0],dados[1],QuantidadeCliEntry.get()))
                              database.db.commit()
                              QuantidadeCliEntry.delete(0, 'end')

                        
                              
                              

            
   QuantidadeLabel = Label(jan3, text="Qtde:",font=("Century Gothic",12),bg="white",fg="black")
   QuantidadeLabel.place(x=100, y=600)
   QuantidadeCliEntry=ttk.Entry(jan3,width=7) 
   QuantidadeCliEntry.place(x=155, y=603)
   AdicionarButton = ttk.Button(jan3, text="Adicionar",command=AdicionarPro, width=15)
   AdicionarButton.place(x=214,y=600)

   salvarButtonHav = ttk.Button(jan3, text="Salvar",command=salvarBD, width=15)
   salvarButtonHav.place(x=250,y=660)



   '''
   scrollpro=Scrollbar(jan3)  
   scrollpro.place(x=382,y=480)
   listapro=Listbox(jan3,width=45,height=10)
   listapro.place(x=100, y=430)
   listapro.config(yscrollcommand=scrollpro.set)
   '''
   treev1 = ttk.Treeview(jan3, selectmode ='browse',height="7") 
   treev1.place(x=100, y=430)
   verscrlbar1 = Scrollbar(jan3,  
                           orient ="vertical",  
                           command = treev1.yview) 
   verscrlbar1.place(x=382,y=480)
   treev1.configure(xscrollcommand = verscrlbar1.set) 
   treev1["columns"] = ("1", "2") 
   treev1['show'] = 'headings'
   treev1.column("1", width = 60, anchor ='c') 
   treev1.column("2", width = 180, anchor ='nw') 
   treev1.heading("1", text ="Id") 
   treev1.heading("2", text ="Produto") 
   showPro()


   treev = ttk.Treeview(jan3, selectmode ='browse',height="7") 
   treev.place(x=500, y=430)
   verscrlbar = Scrollbar(jan3,  
                           orient ="vertical",  
                           command = treev.yview) 
   verscrlbar.place(x=855, y=489) 
   treev.configure(xscrollcommand = verscrlbar.set) 
   treev["columns"] = ("1", "2", "3") 
   treev['show'] = 'headings'
   treev.column("1", width = 100, anchor ='c') 
   treev.column("2", width = 100, anchor ='se') 
   treev.column("3", width = 100, anchor ='c') 
   treev.heading("1", text ="Id") 
   treev.heading("2", text ="Produto") 
   treev.heading("3", text ="Qtde") 

   
   def ExcluirPro():

         dados = treev.item(treev.selection()) ["values"]
         if not dados:
                 messagebox.showinfo(title="Selection Info",message="Produto Não Selecionado!!")
         else:

            dados = treev.item(treev.selection()) ["values"]
            doc=codi.get()
            id=dados[0]
            qtd=dados[2]
            database.cursor.execute('''
            DELETE FROM haveres_produto WHERE( (doc = %s) and (id = %s) and (qtde = %s))
            ''',(doc,id,qtd))
            database.db.commit()
            treev.delete(*treev.get_children())
            showtreev(doc)
         
                        
     


   def  AlterarPro():
         dados = treev.item(treev.selection()) ["values"]
         if not dados:
                 messagebox.showinfo(title="Selection Info",message="Produto Não Selecionado!!")
         
         else:
            root1=Toplevel()
            root1.title('Alterar Produtos') # Dando titulo a jan3ela
            #jan3.geometry('1000x600') # Tamanho da jan3ela
            #jan3.configure (background ="#05A134") #Cor da jan3ela
            root1.resizable(width=False, height=False) #tamanho fixo da jan3ela, nao podendo altera altura e largura e nem maximizala
            #root.attributes("-alpha",0.92) #deixa a jan3ela com transparência
            root1.configure (background ="white")
            root1.attributes("-alpha",0.95) #deixa a jan3ela com transparência

            #centralizando a tela 
            window_height = 400
            window_width =  400
            screen_width = root1.winfo_screenwidth()
            screen_height = root1.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            root1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            

            dados = treev.item(treev.selection()) ["values"]
            
            
            
            
            ALabel = Label(root1, text="Alterar Quantidade",font=("Century Gothic",12),bg="white",fg="black")
            ALabel.place(x=170, y=45)

            imaprod=PhotoImage(file="img/prod.png")  
            log1 = Label(root1, image=imaprod)
            log1.photo = imaprod  # Para colocar imagem no ToopLevel
            log1.place(x=15, y=30)  #posicionando a iamgem

            CLabel = Label(root1, text="Código: ",font=("Century Gothic",12),bg="white")
            CLabel.place(x=15, y=150)
            iLabel = ttk.Label(root1, textvariable=idp,background="White",font=("Century Gothic",12),relief="groove",width=6,padding=2)
            iLabel.place(x=140, y=150)
            CLabel = Label(root1, text="Produto: ",font=("Century Gothic",12),bg="white")
            CLabel.place(x=15, y=180)
            pLabel = ttk.Label(root1, textvariable=nomeP,background="White",font=("Century Gothic",12),relief="groove",width=26,padding=2)
            pLabel.place(x=140, y=180)
            qLabel = Label(root1, text="Quantidade",font=("Century Gothic",12),bg="white",fg="black")
            qLabel.place(x=15, y=210)
            qtdPEntry= ttk.Entry(root1,width=7) 
            qtdPEntry.place(x=140, y=210)
 
            idp.set(dados[0])
            nomeP.set(dados[1])
            qtdPEntry.insert(0,dados[2])

            def SalPro():
                   AlterarQua = qtdPEntry.get()

                   database.cursor.execute('''
                   select idHavPro from  haveres_produto where (doc = %s) and (id = %s)
                   ''',(codi.get(),dados[0]))
                   rows = database.cursor.fetchall()
                   idH= rows[0]
                   

                   database.cursor.execute('''
                   update haveres_produto set qtde=%s where idHavPro=%s
                   ''',(AlterarQua,idH))
                   database.db.commit()
                   root1.destroy()
                    
                  

            SalvProdButton = ttk.Button(root1, text="Alterar",command=SalPro, width=15)
            SalvProdButton.place(x=150,y=300)

          
            
           
            



   ExcluirProdButton = ttk.Button(jan3, text="Excluir Produto",command=ExcluirPro, width=15)
   ExcluirProdButton.place(x=520,y=600)
 
   AlterarProdButton = ttk.Button(jan3, text="Alterar Produto",command=AlterarPro, width=15)
   AlterarProdButton.place(x=637,y=600)
  




   jan3.mainloop()
