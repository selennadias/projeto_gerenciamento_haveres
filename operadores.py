#importando as Blibiotecas
from tkinter import *
from tkinter import messagebox  # importar caixa de messangens(mensagens usuário)
from tkinter import ttk
import database   #importando o arquivo database para fazer a conexao com banco de dados 
from datetime import date #Bliblioteca para lidar com datas e horarios
import tkinter
#from clientes import *
#from haveres import *



def JanOperadores():

    
    jan1=Toplevel() #atribuindo uma variável á uma jan1ela
    jan1.title('Acess Panel - Operadores') # Dando titulo a jan1ela
    jan1.resizable(width=False, height=False) #tamanho fixo da jan1ela, nao podendo altera altura e largura e nem maximizala
    jan1.attributes("-alpha",0.95) #deixa a jan1ela com transparência
    jan1.transient()#
    jan1.focus_force()#
    jan1.grab_set()#
        #centralizando a tela    
    window_height = 680   
    window_width = 900
    screen_width = jan1.winfo_screenwidth()
    screen_height = jan1.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    jan1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

            #Separando a  jan1ela em 4 partes
    TopFrame= Frame(jan1, width=900, height=100, bg="black", relief="raise")
    TopFrame.pack(side=TOP)

    DrowFrame= Frame(jan1, width=900, height=50, bg="#05A134", relief="raise")
    DrowFrame.pack(side=TOP)

    OperadorFrame= Frame(jan1, width=900, height=527, bg="white", relief="raise")
    OperadorFrame.pack(side=TOP)





            #Configurando o TopFrame
            # Colocando o icon Home

    logoh=PhotoImage(file="img/home.png") 
    Logohome = Label(TopFrame,image=logoh,bg="black") 
    Logohome.place(x=5, y=2)  #posicionando a iamgem


    data_atual = date.today()
    data_em_texto = "{}/{}".format(data_atual.day, data_atual.month)
    hj=date.today()
    dias =('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

            #supermecadoLabel = Label(TopFrame, text="Supermecado Alves",font=("Century Gothic",16),bg="black",fg="White")
            #supermecadoLabel.place(x=100, y=10)
    supLabel = Label(TopFrame, text="Supermecado Alves",font=("Century Gothic",12),bg="black",fg="White")
    supLabel.place(x=70, y=26)
    DataLabel = Label(TopFrame, text=data_em_texto,font=("Century Gothic",16),bg="black",fg="White")
    DataLabel.place(x=500, y=10)
    DiaLabel = Label(TopFrame, text=dias[hj.weekday()] ,font=("Century Gothic",10),bg="black",fg="White")
    DiaLabel.place(x=500, y=35)
    VindoLabel = Label(TopFrame, text="Bem Vindo",font=("Century Gothic",12),bg="black",fg="White")
    VindoLabel.place(x=580, y=12)




            #Configurando o DrowFrame
    nomeLabel = Label(DrowFrame, text="OPERADORES",font=("Century Gothic",16),bg="#05A134",fg="White")
    nomeLabel.place(x=5, y=10)

        


            #Configurando o OperadorFrame

    opLabel = Label(OperadorFrame, text="Ficha Cadastral Operadores",font=("Century Gothic",14),bg="white",fg="black")
    opLabel.place(x=100, y=60)

    logo=PhotoImage(file="img/linha.png") 
    LogoLabel = Label(OperadorFrame,image=logo,bg="white")  #carregando o logo através de um label.
    LogoLabel.place(x=100, y=82)  #posicionando a iamgem

    logon1=PhotoImage(file="img/n1.png") 
    Logo1 = Label(OperadorFrame,image=logon1,bg="white")  #carregando o logo através de um label.
    Logo1.place(x=25, y=60)  #posicionando a iamgem


    global NomeOpEntrys

                #Criando os campos
                #Criando Label Nome
    idOp=Label(OperadorFrame, text='Enter ID:',font=("Century Gothic",12),bg="white",fg="black")
    idOp.place(x=10,y=120)
    idOpOpEntry= ttk.Entry(OperadorFrame,width=60) 
    idOpOpEntry.place(x=90, y=124)
    
    NomeOpLabel = Label(OperadorFrame, text="Nome :",font=("Century Gothic",12),bg="white",fg="black")
    NomeOpLabel.place(x=10, y=160)
    NomeOpEntry= ttk.Entry(OperadorFrame,width=60) 
    NomeOpEntry.place(x=90, y=164)
    UsuarioOpLabel = Label(OperadorFrame, text="Usuário :",font=("Century Gothic",12),bg="white",fg="black")
    UsuarioOpLabel.place(x=10, y=200)
    UsuarioOpEntry=ttk.Entry(OperadorFrame,width=60) 
    UsuarioOpEntry.place(x=90, y=204)
    SenhaOpLabel = Label(OperadorFrame, text="Senha :",font=("Century Gothic",12),bg="white",fg="black")
    SenhaOpLabel.place(x=10, y=240)
    SenhaOpEntry=ttk.Entry(OperadorFrame,width=30,show="●●●●●●●") #Deixando a senha oculta
    SenhaOpEntry.place(x=90, y=244)

  

    def salvar():
                

                try: 
                    
                    id=idOpOpEntry.get()
                    nome=NomeOpEntry.get()
                    usuario=UsuarioOpEntry.get()
                    senha=SenhaOpEntry.get()
                    '''
                    if i.get() == 1:
                            admim="Sim"
                    else:
                           admim="Não"
                    '''
                    if(nome=="" or usuario=="" or senha==""):
                        messagebox.showinfo("Insert status", "Erro!!  Campos Vazios",parent=jan1)
                    else:
                        database.cursor.execute('''
                        insert into operadores(id,nome,usuario,senha) 
                        values(%s, %s, %s, %s)
                        ''',(id,nome,usuario,senha))
                        database.db.commit()
                        messagebox.showinfo(title="Register Info",message="Salvo com Sucesso!!",parent=jan1)
                        idOpOpEntry.delete(0, 'end')
                        NomeOpEntry.delete(0, 'end')#limpa o label Nome
                        UsuarioOpEntry.delete(0, 'end')#limpa o label usuario
                        SenhaOpEntry.delete(0, 'end')#limpa o label senha
                        #i.set(0)
                        treev2.delete(*treev2.get_children())
                        database.cursor.execute('''
                        SELECT * FROM operadores''')
                        rows = database.cursor.fetchall()
                                
                        for results in rows:
                                treev2.insert("", 'end', text ="", 
                                                values =(results[0], results[2]))
                
                except:
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan1)

    def excluir():
                try: 
                    id=idOpOpEntry.get()
                    if(idOpOpEntry.get() == ""):
                            messagebox.showinfo("Delete Status", "ID não informado",parent=jan1)
                    else:
                        
                        database.cursor.execute('''
                        delete from operadores where id= %s
                        ''',(id))
                        database.db.commit()
                        messagebox.showinfo(title="Register Info",message="Deletado com sucesso!!",parent=jan1)
                        idOpOpEntry.delete(0, 'end')
                        NomeOpEntry.delete(0, 'end')#limpa o label Nome
                        UsuarioOpEntry.delete(0, 'end')#limpa o label usuario
                        SenhaOpEntry.delete(0, 'end')#limpa o label senha
                        #i.set(0)
                        treev2.delete(*treev2.get_children())
                        database.cursor.execute('''
                        SELECT * FROM operadores''')
                        rows = database.cursor.fetchall()
                
                        for results in rows:
                          treev2.insert("", 'end', text ="", 
                                    values =(results[0], results[2]))
                
                
                except:
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan1)

    def limpar():
                    idOpOpEntry.delete(0, 'end')
                    NomeOpEntry.delete(0, 'end')#limpa o label Nome
                    UsuarioOpEntry.delete(0, 'end')#limpa o label usuario
                    SenhaOpEntry.delete(0, 'end')#limpa o label senha
    def selecionar():
                try: 
                    
                        result =treev2.item(treev2.selection()) ["values"]
                        id=str(result[0])
                        database.cursor.execute(''' 
                        select * from operadores where id=%s
                        ''',[id])
                        rows = database.cursor.fetchall()
                        '''if rows[0][4] == "Sim":
                                ad=1
                        else:
                                ad=2
                        '''
                        
                        
                        idOpOpEntry.delete(0,'end')
                        NomeOpEntry.delete(0, 'end')#limpa o label Nome
                        UsuarioOpEntry.delete(0, 'end')#limpa o label usuario
                        SenhaOpEntry.delete(0, 'end')#limpa o label senha
                       
                        
                        for row in rows:
                            idOpOpEntry.insert(0,row[0])
                            NomeOpEntry.insert(0,row[1])
                            UsuarioOpEntry.insert(0,row[2])
                            SenhaOpEntry.insert(0,row[3])
                            #i.set(ad)
                           
                           
                        
                except:
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan1)
                
    def alterar():
                try: 
                    id=idOpOpEntry.get()
                    nome=NomeOpEntry.get()
                    usuario=UsuarioOpEntry.get()
                    senha=SenhaOpEntry.get()
                    '''if i.get() == 1:
                            admim="Sim"
                    else:
                           admim="Não"
                    '''
                    if(id=="" or nome=="" or usuario=="" or senha==""):
                        messagebox.showinfo("Insert status", "Erro!!  Campos Vazios",parent=jan1)
                    else:
                        database.cursor.execute('''
                        update operadores set nome=%s,usuario=%s,senha=%s where id=%s
                        ''',(nome,usuario,senha,id))
                        database.db.commit()
                        messagebox.showinfo(title="Register Info",message="Atualizado com Sucesso!!",parent=jan1)
                        idOpOpEntry.delete(0, 'end')
                        NomeOpEntry.delete(0, 'end')#limpa o label Nome
                        UsuarioOpEntry.delete(0, 'end')#limpa o label usuario
                        SenhaOpEntry.delete(0, 'end')#limpa o label senha
                        #i.set(0)

                        treev2.delete(*treev2.get_children())
                        database.cursor.execute('''
                        SELECT * FROM operadores''')
                        rows = database.cursor.fetchall()
                
                        for results in rows:
                          treev2.insert("", 'end', text ="", 
                                    values =(results[0], results[2]))
                
                except:
                        messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan1)
                        
    def show():

          database.cursor.execute('''
          SELECT * FROM operadores''')
          rows = database.cursor.fetchall()
                
          for results in rows:
                treev2.insert("", 'end', text ="", 
                                    values =(results[0], results[2]))




    imag = PhotoImage(file="img/lim.png")
    limparButton = Button(OperadorFrame,bd=0,default=DISABLED,image=imag,command=limpar)
    limparButton.place(x=375,y=260)

    #photo01 = PhotoImage(file="img/iconsalvar.png")
    salvarButton = ttk.Button(OperadorFrame, text="Salvar",command=salvar, width=15)
    salvarButton.place(x=140,y=410)

    #photo02 = PhotoImage(file="img/iconExcluir.png")
    deleteButton = ttk.Button(OperadorFrame,  text="Excluir", command=excluir,width=15)
    deleteButton.place(x=260,y=410)

    photo03 = PhotoImage(file="img/selectIcon.png")
    updateButton = ttk.Button(OperadorFrame, image=photo03, command=selecionar)
    updateButton.place(x=550,y=305)

    #photo04 = PhotoImage(file="img/alterarIcon.png")
    getButton = ttk.Button(OperadorFrame,  text="Alterar", command=alterar,width=15)
    getButton.place(x=380,y=410)



    treev2 = ttk.Treeview(OperadorFrame, selectmode ='browse',height="7") 
    treev2.place(x=500, y=122)
    verscrlbar1 = Scrollbar(OperadorFrame,  
                           orient ="vertical",  
                           command = treev2.yview) 
    verscrlbar1.place(x=750,y=200)
    treev2.configure(xscrollcommand = verscrlbar1.set) 
    treev2["columns"] = ("1", "2") 
    treev2['show'] = 'headings'
    treev2.column("1", width = 60, anchor ='c') 
    treev2.column("2", width = 180, anchor ='nw') 
    treev2.heading("1", text ="Id") 
    treev2.heading("2", text ="Operadores") 
    show()



    jan1.mainloop()