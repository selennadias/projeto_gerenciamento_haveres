import MySQLdb  #Conectando o python ao banco de dados 


host ="localhost"
user ="root"
password="root" 
db ="login_supermecado"
port = 3306
db = MySQLdb.Connect(host, user, password,db,port)
cursor=db.cursor()


#db = MySQLdb.connect(host="localhost",user="root", passwd="root", db="login_supermecado")  cursor = db.cursor() 

