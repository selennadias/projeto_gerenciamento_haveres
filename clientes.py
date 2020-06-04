#importando as Blibiotecas
from tkinter import *
from tkinter import messagebox  # importar caixa de messangens(mensagens usuário)
from tkinter import ttk
import database   #importando o arquivo database para fazer a conexao com banco de dados 
from datetime import date #Bliblioteca para lidar com datas e horarios
import tkinter

def client():
  
    jan2=Toplevel() #atribuindo uma variável á uma jan2ela
    jan2.title('Acess Panel - Operadores') # Dando titulo a jan2ela
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

    logon1=PhotoImage(file="img/n1.png") 
    Logo1 = Label(ClienteFrame1,image=logon1,bg="white")  #carregando o logo através de um label.
    Logo1.place(x=25, y=60)  #posicionando a iamgem




            #Criando os campos
            #Criando Label Nome
    idCli=Label(ClienteFrame1, text='Enter ID:',font=("Century Gothic",12),bg="white",fg="black")
    idCli.place(x=10,y=120)
    idCliOpEntry= ttk.Entry(ClienteFrame1,width=60) 
    idCliOpEntry.place(x=90, y=124)
    NomeCliLabel = Label(ClienteFrame1, text="Nome :",font=("Century Gothic",12),bg="white",fg="black")
    NomeCliLabel.place(x=10, y=160)
    NomeCliEntry= ttk.Entry(ClienteFrame1,width=60) 
    NomeCliEntry.place(x=90, y=164)
    TelefoneCliLabel = Label(ClienteFrame1, text="Telefone :",font=("Century Gothic",12),bg="white",fg="black")
    TelefoneCliLabel.place(x=10, y=200)
    TelefoneCliEntry=ttk.Entry(ClienteFrame1,width=60) 
    TelefoneCliEntry.place(x=90, y=204)
    EnderecoCliLabel =  Label(ClienteFrame1, text="Endereço :",font=("Century Gothic",12),bg="white",fg="black")
    EnderecoCliLabel.place(x=10, y=240)
    EnderecoCliEntry=ttk.Entry(ClienteFrame1,width=60) 
    EnderecoCliEntry.place(x=90, y=244)
    CpfLabel =  Label(ClienteFrame1, text="cpf :",font=("Century Gothic",12),bg="white",fg="black")
    CpfLabel.place(x=10, y=280)
    CpfLabelEntry=ttk.Entry(ClienteFrame1,width=60) 
    CpfLabelEntry.place(x=90, y=284)
    


  
    
    

    

   
    def salvar():
      

            try:  
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
                    values(%s, %s, %s, %s, %s)
                    ''',(id,nome,telefone,endereco,cpf))
                    database.db.commit()
                    messagebox.showinfo(title="Register Info",message="Salvo com Sucesso!!",parent=jan2)
                    idCliOpEntry.delete(0, 'end')
                    NomeCliEntry.delete(0, 'end')#limpa o label Nome
                    TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                    EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
                    zerar()
                    show()
            
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
                    zerar()
                    show()
                    
            
            except:
                    messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan2)

    def limpar():
                idCliOpEntry.delete(0, 'end')
                NomeCliEntry.delete(0, 'end')#limpa o label Nome
                TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
    def selecionar():
            try: 
                id=idCliOpEntry.get()
                if(idCliOpEntry.get() == ""):
                        messagebox.showinfo("Delete Status", "ID não informado",parent=jan2)

                else:
                    
                    database.cursor.execute(''' 
                    select * from cliente where idCli=%s
                    ''',(id))
                    rows = database.cursor.fetchall()

                    
                    NomeCliEntry.delete(0, 'end')#limpa o label Nome
                    TelefoneCliEntry.delete(0, 'end')#limpa o label telefone
                    EnderecoCliEntry.delete(0, 'end')#limpa o label endereco
                    for row in rows:
                        NomeCliEntry.insert(0,row[1])
                        TelefoneCliEntry.insert(0,row[2])
                    
            except:
                    messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan2)
            
    def alterar():
            try: 
                id=idCliOpEntry.get()
                nome=NomeCliEntry.get()
                telefone=telefoneCliEntry.get()
                endereco=enderecoOpEntry.get()
                cpf=i.get()
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
                    zerar()
                    show()
            except:
                    messagebox.showinfo(title="Register Info",message="Erro Conexao ao Banco !!!",parent=jan2)
                    
    def show():
            database.cursor.execute('''
            SELECT idCli,nome FROM cliente''')
            rows = database.cursor.fetchall()
            
            for results in rows:
                insertData = str(results[0])+ '          '+ results[1]
                lista.insert("end", insertData)


    def zerar():
            lista .delete(0,"end")


    imag = PhotoImage(file="img/limpar.png")
    limparButton = ttk.Button(ClienteFrame1,image=imag,command=limpar)
    limparButton.place(x=20,y=410)

    photo01 = PhotoImage(file="img/iconsalvar.png")
    salvarButton = ttk.Button(ClienteFrame1, image=photo01,command=salvar)
    salvarButton.place(x=140,y=410)

    photo02 = PhotoImage(file="img/iconExcluir.png")
    deleteButton = ttk.Button(ClienteFrame1, image=photo02, command=excluir)
    deleteButton.place(x=260,y=410)

    photo03 = PhotoImage(file="img/selectIcon.png")
    updateButton = ttk.Button(ClienteFrame1, image=photo03, command=selecionar)
    updateButton.place(x=380,y=410)

    photo04 = PhotoImage(file="img/alterarIcon.png")
    getButton = ttk.Button(ClienteFrame1, image=photo04, command=alterar)
    getButton.place(x=500,y=410)

    scroll=Scrollbar(ClienteFrame1)  
    scroll.place(x=750,y=160)
    lista=Listbox(ClienteFrame1,width=40)
    lista.place(x=500, y=122)
    lista.config(yscrollcommand=scroll.set)
    show()
    
    jan2.mainloop()
