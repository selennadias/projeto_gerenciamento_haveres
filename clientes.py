#importando as Blibiotecas
from tkinter import *
from tkinter import messagebox  # importar caixa de messangens(mensagens usuário)
from tkinter import ttk
import database   #importando o arquivo database para fazer a conexao com banco de dados 
from datetime import date #Bliblioteca para lidar com datas e horarios
import tkinter
def client():
  
          
    jan2=Toplevel() #atribuindo uma variável á uma jan2ela
    jan2.title('Acess Panel - Cliente') # Dando titulo a jan2ela
    jan2.resizable(width=False, height=False) #tamanho fixo da jan2ela, nao podendo altera altura e largura e nem maximizala
    jan2.attributes("-alpha",0.92) #deixa a jan2ela com transparência
    jan2.transient()#
    jan2.focus_force()#
    jan2.grab_set()#
    


    #centralizando a tela    
    window_height = 680   
    window_width = 900
    screen_width = jan2.winfo_screenwidth()
    screen_height = jan2.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    jan2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #Separando a  jan2ela em 4 partes
    TopFrame1= Frame(jan2, width=900, height=100, bg="black", relief="raise")
    TopFrame1.pack(side=TOP)

    DrowFrame1= Frame(jan2, width=900, height=50, bg="#05A134", relief="raise")
    DrowFrame1.pack(side=TOP)

    ClienteFrame1= Frame(jan2, width=900, height=527, bg="white", relief="raise")
    ClienteFrame1.pack(side=TOP)





        #Configurando o TopFrame1
        # Colocando o icon Home

    logoh=PhotoImage(file="img/home.png") 
    Logohome = Label(TopFrame1,image=logoh,bg="black") 
    Logohome.place(x=5, y=2)  #posicionando a iamgem


    data_atual = date.today()
    data_em_texto = "{}/{}".format(data_atual.day, data_atual.month)
    hj=date.today()
    dias =('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

        #supermecadoLabel = Label(TopFrame1, text="Supermecado Alves",font=("Century Gothic",16),bg="black",fg="White")
        #supermecadoLabel.place(x=100, y=10)
    supLabel = Label(TopFrame1, text="Supermecado Alves",font=("Century Gothic",12),bg="black",fg="White")
    supLabel.place(x=70, y=26)
    DataLabel = Label(TopFrame1, text=data_em_texto,font=("Century Gothic",16),bg="black",fg="White")
    DataLabel.place(x=500, y=10)
    DiaLabel = Label(TopFrame1, text=dias[hj.weekday()] ,font=("Century Gothic",10),bg="black",fg="White")
    DiaLabel.place(x=500, y=35)
    VindoLabel = Label(TopFrame1, text="Bem Vindo",font=("Century Gothic",12),bg="black",fg="White")
    VindoLabel.place(x=580, y=12)




        #Configurando o DrowFrame1
    nomeLabel = Label(DrowFrame1, text="CLIENTE",font=("Century Gothic",16),bg="#05A134",fg="White")
    nomeLabel.place(x=5, y=10)

    


        #Configurando o ClienteFrame1

    cliLabel = Label(ClienteFrame1, text="Ficha Cadastral Cliente",font=("Century Gothic",14),bg="white",fg="black")
    cliLabel.place(x=100, y=60)

    logo=PhotoImage(file="img/linha.png") 
    LogoLabel = Label(ClienteFrame1,image=logo,bg="white")  #carregando o logo através de um label.
    LogoLabel.place(x=100, y=82)  #posicionando a iamgem

    logon1=PhotoImage(file="img/n2.png") 
    Logo1 = Label(ClienteFrame1,image=logon1,bg="white")  #carregando o logo através de um label.
    Logo1.place(x=25, y=60)  #posicionando a iamgem




            #Criando os campos
            #Criando Label Nome
    idCli=Label(ClienteFrame1, text='Enter ID:',font=("Century Gothic",12),bg="white",fg="black")
    idCli.place(x=10,y=120)
    idCliOpEntry= ttk.Entry(ClienteFrame1,width=40) 
    idCliOpEntry.place(x=95, y=124)
    NomeCliLabel = Label(ClienteFrame1, text="Nome :",font=("Century Gothic",12),bg="white",fg="black")
    NomeCliLabel.place(x=10, y=160)
    NomeCliEntry= ttk.Entry(ClienteFrame1,width=40) 
    NomeCliEntry.place(x=95, y=164)
    TelefoneCliLabel = Label(ClienteFrame1, text="Telefone:",font=("Century Gothic",12),bg="white",fg="black")
    TelefoneCliLabel.place(x=10, y=200)
    TelefoneCliEntry=ttk.Entry(ClienteFrame1,width=40) 
    TelefoneCliEntry.place(x=95, y=204)
    EnderecoCliLabel =  Label(ClienteFrame1, text="Endereço:",font=("Century Gothic",12),bg="white",fg="black")
    EnderecoCliLabel.place(x=10, y=240)
    EnderecoCliEntry=ttk.Entry(ClienteFrame1,width=40) 
    EnderecoCliEntry.place(x=95, y=244)
    CpfLabel =  Label(ClienteFrame1, text="CPF:",font=("Century Gothic",12),bg="white",fg="black")
    CpfLabel.place(x=10, y=280)
    CpfLabelEntry=ttk.Entry(ClienteFrame1,width=40) 
    CpfLabelEntry.place(x=95, y=284)
    


  
    
    

    def salvar():
          

            try:
                
                database.cursor.execute('''
                select * from cliente
                ''')
                rows = database.cursor.fetchall()
                cout =len ( rows ) + 1

                id=idCliOpEntry.get()
                nome=NomeCliEntry.get()
                telefone=TelefoneCliEntry.get()
                endereco=EnderecoCliEntry.get()
                cpf=CpfLabelEntry.get()
                if(nome=="" or telefone=="" or endereco==""):
                    messagebox.showinfo("Insert status", "Erro!!  Campos Vazios",parent=jan2)
                else:
                    database.cursor.execute('''
                    insert into cliente(idCli,nome,telefone,endereco,cpf) 
                    values(%s,%s,%s,%s,%s)
                    ''',(id,nome,telefone,endereco,cpf))
                    database.db.commit()
                    messagebox.showinfo(title="Register Info",message="Salvo com Sucesso!!",parent=jan2)
                    idCliOpEntry.delete(0, 'end')
                    NomeCliEntry.delete(0, 'end')#limpa o label Nome
                    TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                    EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
                    CpfLabelEntry.delete(0, 'end')

                    treev4.delete(*treev4.get_children())
                    database.cursor.execute('''
                    SELECT idCli,nome,telefone FROM cliente''')
                    rows = database.cursor.fetchall()
                
                    for results in rows:
                          treev4.insert("", 'end', text ="", 
                                    values =(results[0], results[1], results[2]))

            
            except:
                    messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan2)


    def excluir():
            try: 
                id=idCliOpEntry.get()
                if(idCliOpEntry.get() == ""):
                        messagebox.showinfo("Delete Status", "ID não informado",parent=jan2)
                else:
                    
                    database.cursor.execute('''
                    delete from cliente where idCli= %s
                    ''',(id))
                    database.db.commit()
                    messagebox.showinfo(title="Register Info",message="Deletado com sucesso!!",parent=jan2)
                    idCliOpEntry.delete(0, 'end')
                    NomeCliEntry.delete(0, 'end')#limpa o label Nome
                    TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                    EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
                    CpfLabelEntry.delete(0, 'end')
                    
                    treev4.delete(*treev4.get_children())
                    database.cursor.execute('''
                    SELECT idCli,nome,telefone FROM cliente''')
                    rows = database.cursor.fetchall()
                
                    for results in rows:
                          treev4.insert("", 'end', text ="", 
                                    values =(results[0], results[1], results[2]))
                    
            
            except:
                    messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan2)

    def limpar():
                
                

                idCliOpEntry.delete(0, 'end')
                NomeCliEntry.delete(0, 'end')#limpa o label Nome
                TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
                CpfLabelEntry.delete(0, 'end')
    def selecionar():
          
                   
                    result =treev4.item(treev4.selection()) ["values"]
                    id=str(result[0])
                    print(result[0])
                    print(id)
                    database.cursor.execute(''' 
                    select * from cliente where idCli = %s
                    ''',[id])
                    rows = database.cursor.fetchall()
                    idCliOpEntry.delete(0,'end')
                    NomeCliEntry.delete(0, 'end')#limpa o label Nome
                    TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                    EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
                    CpfLabelEntry.delete(0, 'end')
                    for row in rows:
                        idCliOpEntry.insert(0,row[0])
                        NomeCliEntry.insert(0,row[1])
                        if row[2]:
                         TelefoneCliEntry.insert(0,row[2])
                        if row[3]:
                         EnderecoCliEntry.insert(0,row[3])
                        if row[4]:
                         CpfLabelEntry.insert(0,row[4])
        
            
    def alterar():
            try: 
                id=idCliOpEntry.get()
                nome=NomeCliEntry.get()
                telefone=TelefoneCliEntry.get()
                endereco=EnderecoCliEntry.get()
                cpf=CpfLabelEntry.get()
                if(id=="" or nome=="" or telefone=="" or endereco==""):
                    messagebox.showinfo("Insert status", "Erro!!  Campos Vazios",parent=jan2)
                else:
                    database.cursor.execute('''
                    update cliente set nome=%s,telefone=%s,endereco=%s,cpf=%s  where idCli=%s
                    ''',(nome,telefone,endereco,cpf,id))
                    database.db.commit()
                    messagebox.showinfo(title="Register Info",message="Atualizado com Sucesso!!",parent=jan2)
                    idCliOpEntry.delete(0, 'end')
                    NomeCliEntry.delete(0, 'end')#limpa o label Nome
                    TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                    EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
                    CpfLabelEntry.delete(0, 'end')#limpa o label endereco
                    
                    treev4.delete(*treev4.get_children())
                    database.cursor.execute('''
                    SELECT idCli,nome,telefone FROM cliente''')
                    rows = database.cursor.fetchall()
                
                    for results in rows:
                          treev4.insert("", 'end', text ="", 
                                    values =(results[0], results[1], results[2]))
            except:
                    messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan2)
                    
    def show():
            database.cursor.execute('''
            SELECT idCli,nome,telefone FROM cliente''')
            rows = database.cursor.fetchall()
            # print(rows)

            for results in rows:
                treev4.insert("", 'end', text ="", 
                                    values =(results[0], results[1], results[2]))



 

    imag = PhotoImage(file="img/lim.png")
    limparButton = Button(ClienteFrame1,bd=0,default=DISABLED,image=imag,command=limpar)
    limparButton.place(x=295,y=320)

  #  photo01 = PhotoImage(file="img/iconsalvar.png")
    salvarButton = ttk.Button(ClienteFrame1, text="Salvar",command=salvar, width=15)
    salvarButton.place(x=140,y=410)

  #  photo02 = PhotoImage(file="img/iconExcluir.png")
    deleteButton = ttk.Button(ClienteFrame1,  text="Excluir", command=excluir,width=15)
    deleteButton.place(x=260,y=410)

    photo03 = PhotoImage(file="img/selectIcon.png")
    updateButton = ttk.Button(ClienteFrame1, image=photo03, command=selecionar)
    updateButton.place(x=580,y=305)

    #photo04 = PhotoImage(file="img/alterarIcon.png")
    getButton = ttk.Button(ClienteFrame1,  text="Alterar", command=alterar,width=15)
    getButton.place(x=380,y=410)

    treev4 = ttk.Treeview(ClienteFrame1, selectmode ='browse',height="7") 
    treev4.place(x=430, y=122)
    verscrlbar1 = Scrollbar(ClienteFrame1,  
                           orient ="vertical",  
                           command = treev4.yview) 
    verscrlbar1.place(x=825,y=200)
    treev4.configure(xscrollcommand = verscrlbar1.set) 
    treev4["columns"] = ("1", "2","3") 
    treev4['show'] = 'headings'
    treev4.column("1", width = 60, anchor ='c') 
    treev4.column("2", width = 230, anchor ='nw') 
    treev4.column("3", width = 100, anchor ='nw') 
    treev4.heading("1", text ="Id") 
    treev4.heading("2", text ="Cliente")
    treev4.heading("3", text ="Telefone")
    show()
    jan2.mainloop()
