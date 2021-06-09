import os
import numpy as np
from datetime import datetime
class   ControlVersiones:
    def __init__(self) :
        self.RegistrosArch=[]
        self.Inicio=False

    def CrearCarpeta(self,nombre):
        directorio="Usuarios/"+nombre
        try:
            
            os.mkdir(directorio)
            direccion=directorio+"/Archtemp.txt"
            registro= open(direccion, 'a')
            registro.close()
            direccion=directorio+"/Archperm.txt"
            registro= open(direccion, 'a')
            registro.close()

            os.mkdir(directorio+"/Temp")
            os.mkdir(directorio+"/Perm")
        except OSError:
            print("La creacion de la carpeta %s fallo" % directorio)
        else:
            print("Se ha creado la carpeta:%s"%directorio)


    def Registrar(self):
        nombre=input("Introduzca el nombre: ")
        password=input("Introduzca la contraseña: ")
        registro= open("Usuarios.rg", 'a')
        if not self.Autenticar(nombre)and nombre != password:
            registro.write(nombre+" "+password+'\n')
            self.CrearCarpeta(nombre)
            print("%s se ha registrado de manera exitosa" %nombre)
            registro.close()
        else:
            print("Los datos ya estan en el sistema, vuelva a intentarlo con otro nombre de usuario\n")
            registro.close()
            self.Registrar()


    def InicioSesion(self,name,passw):
        concat=str(name+" "+passw)
        
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                if concat in line:
                    self.Inicio=True
                    print("Inicio Sesion de forma Satisfactoria\n\n")
                else:
                    self.Inicio=False
                    print("No Encontrado\n\n\tPor favor proceda a registrarse")
                    self.Registrar()


    def Autenticar(self,nombre):
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                if nombre in line:
                    # print("Encontrado %s" %line)
                    return True
                else:
                    # print("No Encontrado %s" %line)
                    return False


    def AddFile(self,tipo,nombre,dato):
        now=datetime.now()
        
        filename=datetime.now().strftime("%d_%b_%Y_%H_%M_%S")
        if tipo==1:
            #Guardar el nombre del registro en el archivo
            direccionlist="Usuarios/"+nombre+"/Archtemp.txt"
            #Guardar el archivo en temp con el nombre de la fecha actual
            direccion="Usuarios/"+nombre+"/Temp/"+filename+".txt"
        if tipo==2:
            #Guardar el nombre del registro en el archivo
            direccionlist="Usuarios/"+nombre+"/Archperm.txt"
            #Guardar el archivo en temp con el nombre de la fecha actual
            direccion="Usuarios/"+nombre+"/Perm/"+filename+".txt"
        self.grabarArchivo(direccionlist,filename+".txt\n")
        self.grabarArchivo(direccion,dato)



    def grabarArchivo(self, direccion,dato):
        registro= open(direccion, 'a')
        registro.write(dato)
        registro.close()



    def RecuperarArchivo(self,nombre,tipo):
        lista= list()
        if tipo==1:
            concat='Usuarios/'+nombre+'/Archtemp.txt'
        if tipo==2:
            concat='Usuarios/'+nombre+'/Archperm.txt'
        with open(concat) as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                lista.append(line)

        nombrearch=lista.pop(len(lista)-1)
        nombrearch=nombrearch[0:len(nombrearch)-1]
        print(lista)
        print(nombrearch)
        if tipo==1:
            filename= 'Usuarios/'+nombre+"/Temp/"+nombrearch
        if tipo==2:
            filename= 'Usuarios/'+nombre+"/Perm/"+nombrearch
        self.ObtenerArch(filename)
        os.remove(filename)
        registro= open(concat, 'w')
        for x in lista:
            registro.write(x)
        registro.close()


    def ObtenerArch(self,direccion):

        registro= open(direccion, 'r')
        print(registro.read())
        registro.close()

    def Principal(self):

        print("\033[2J\033[1;1f")
        print(chr(27)+"[1;30;47m"+"\t\t***BIENVENIDO AL SISTEMA DE CONTROL DE VERSIONES***\n\n\n"+'\033[0;m')
        print(chr(27)+"[1;31m"+"\t0) Salir\n"+chr(27)+"[1;32m"+"\t1) Iniciar Sesion\n"+chr(27)+"[1;33m"+"\t2) Registrarse\n"+'\033[0;m')
        print(chr(27)+"[1;30;47m"+"**Si no posee cuenta favor registrarse**\n"+'\033[0;m')
        op=int(input(chr(27)+"[1;30m"+"Seleccione una opcion: "+'\033[0;m'))
        if op==1:
            print("\033[2J\033[1;1f")
            nombre=input("Introduzca el nombre: ")
            password=input("Introduzca la contraseña: ")
            self.InicioSesion(nombre,password)
        elif op==2:
            print("\033[2J\033[1;1f")
            self.Registrar()


c=ControlVersiones()
i=0
def __main__():
    c.Principal()
    
    # c.Registrar()
    # c.AddFile(1,"Kendal","Hola quiubo x2+221\n haoisdjk\nasdhjkahskjh\njhskdjhkeb")
    # c.RecuperarArchivo('Kendal',1)
    # c.InicioSesion("Ian","mamapichas")

    
if __name__ =="__main__":
    __main__()