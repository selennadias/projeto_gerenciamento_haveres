# coding=utf-8
# Desenvolvimento Aberto
# Funcionario.py
 
__author__ = 'Elenna e Mainara'
 
class operadorer():
 
    # Define atributos privados
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__usuario = None
        self.__senha = None
        self.__admim = None
 
    # Define métodos Getter e Setter
    # Você também pode optar por propriedades
    def getId(self):
        return self.__id
 
    def setId(self, id):
        self.__id = id
 
    def getNome(self):
        return self.__nome
 
    def setNome(self, nome):
        self.__nome = nome
 
    def getUsuario(self):
        return self.__usuario
 
    def setUsuario(self, usuario):
        self.__usuario = usuario
 

    def getSenha(self):
        return self.__senha
 
    def setSenha(self, senha):
        self.__senha = senha
 
    def getAdmim(self):
        return self.__admim
 
    def setadmim(self, admim):
        self.__admim = admim