#importando as Blibiotecas
from tkinter import*
from tkinter import messagebox  # importar caixa de messangens(mensagens usuário)
from tkinter import ttk
import database   #importando o arquivo database para fazer a conexao com banco de dados 
from haveres import haver




jan=Tk()  #atribuindo uma variável á uma janela
jan.title('Supermecado Alves - Acess Panel') # Dando titulo a janela
#jan.geometry('600x300') # Tamanho da janela
jan.configure (background ="white") #Cor da Janela
jan.resizable(width=False, height=False) #tamanho fixo da janela, nao podendo altera altura e largura e nem maximizala
jan.attributes("-alpha",0.94) #deixa a janela com transparência


#centralizando a tela 
window_height = 300
window_width = 600
screen_width = jan.winfo_screenwidth()
screen_height = jan.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/1.5))
jan.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))




#Separando a  janela em duas partes
LeftFrame= Frame(jan, width=200, height=300, bg="white", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame= Frame(jan, width=395, height=300, bg="#05A134", relief="raise")
RightFrame.pack(side=RIGHT)


# Colocando o Logo
logo=PhotoImage(file="img/log.png") #python é melhor trabalhar com png 
LogoLabel = Label(LeftFrame,image=logo,bg="white")  #carregando o logo através de um label, label serve tanto para texto como imagens
LogoLabel.place(x=50, y=100)  #posicionando a iamgem


#Criando Label usuario
UserLabel = Label(RightFrame, text="Usuário:",font=("Century Gothic",16),bg="#05A134",fg="White")
UserLabel.place(x=10, y=100)


# Criando  uma combobox que contém  usuários do banco de dados 
database.cursor.execute('select usuario from operadores;')  #puxando os usuarios do banco de dados 
results = database.cursor.fetchall()
#database.cursor.close()
results_for_combobox = [result[0] for result in results]

comboExample = ttk.Combobox(RightFrame, width=27,values=results_for_combobox,state="readonly")
comboExample.pack()
comboExample.place(x=100,y=106)
comboExample.current()


#Criando Label senha
PassLabel = Label(RightFrame, text="Senha :",font=("Century Gothic",16),bg="#05A134",fg="White")
PassLabel.place(x=10, y=140)

PassEntry= ttk.Entry(RightFrame,width=30,show="●●●●●●●") #Deixando a senha oculta
PassEntry.place(x=100, y=146)
 

# O erro que tava dando no where era porque estava usando ?, tem que especificar o tipo %s
  

def callback(event):
    usuario=str(comboExample.get())
    senha=PassEntry.get()

    database.cursor.execute('''
    SELECT * FROM operadores
    WHERE (usuario=%s AND senha=%s)  
    ''', (usuario,senha))

    verifyLogin = database.cursor.fetchone()
    try:
        if (usuario in verifyLogin and senha in verifyLogin):
            jan.destroy()
            haver()
    except:
        PassEntry.delete(0, 'end')#limpa o label senha
        
    
jan.bind('<Return>', callback)

 
def Login():  #Função para verificar o login
    usuario=str(comboExample.get())
    senha=PassEntry.get()

    database.cursor.execute('''
    SELECT * FROM operadores
    WHERE (usuario=%s AND senha=%s)  
    ''', (usuario,senha))

    verifyLogin = database.cursor.fetchone()
    try:
        if (usuario in verifyLogin and senha in verifyLogin):
            jan.destroy()
            haver()
          


    except:
        
        PassEntry.delete(0, 'end')#limpa o label senha
        messagebox.showinfo(title="Login Info",message="Acesso Negado. Usuário ou senha Invalido")
        
        
        


  


#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=15, command=Login)
LoginButton.place(x=130,y=200)



jan.mainloop()

