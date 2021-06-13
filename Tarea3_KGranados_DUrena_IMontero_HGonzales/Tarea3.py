from Usuario import *
import os
import numpy as np
from datetime import datetime
import shutil
import msvcrt as ms
class   ControlVersiones:
    def __init__(self) :
        self.userslist=list()
        self.Inicio=False

    def CrearCarpeta(self,nombre): #Crea por defecto las carpetas de cada usuario
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
            os.mkdir(directorio+"/Documentos")
        except OSError:
            print("La creacion de la carpeta %s fallo" % directorio)
        else:
            print("Se ha creado la carpeta:%s"%directorio)


    def Registrar(self): # Registra un usuario
        print("\033[2J\033[1;1f")
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


    def InicioSesion(self,name,passw):# Verifica si el usuario existe, si existe ingresa a la app sino lo envia a registrarse
        concat=str(name+" "+passw)
        lista = list()
        usuario=False
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                if concat in line:
                    usuario=True
        if usuario:
            print("Inicio Sesion de forma Satisfactoria\n\n")
        else:
            print("No Encontrado\n\n\tPor favor proceda a registrarse")
            self.Registrar()


    def Autenticar(self,nombre): #Verifica si el usuario existe en la "bd"
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                if nombre in line:
                    # print("Encontrado %s" %line)
                    return True
                else:
                    # print("No Encontrado %s" %line)
                    return False


    def AddFile(self,tipo,nombre,dato): # Agrega archivos temporales o permanentes a sus respectivas carpetas
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



    def grabarArchivo(self, direccion,dato):# Crea o modifica un archivo
        registro= open(direccion, 'a')
        registro.write(dato)
        registro.close()



    def RecuperarArchivo(self,nombre,tipo):#obtiene la ultima version guardada
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

    def Commit(self, nombre): #Transfiere la ultima actualizacion de los archivos temporales a los Permanentes
        try:
            lista= list()
            concat='Usuarios/'+nombre+'/Archtemp.txt'
            concat2='Usuarios/'+nombre+'/Archperm.txt'
            with open(concat) as temp_f:
                archivo = temp_f.readlines()
                for line in archivo:
                    lista.append(line)
            nombrearch=lista.pop(len(lista)-1)
            nombrearch=nombrearch[0:len(nombrearch)-1]

            print(lista)
            print(nombrearch)
            filedir= 'Usuarios/'+nombre+"/Temp/"+nombrearch
            filedir2='Usuarios/'+nombre+"/Perm/"+nombrearch
            
            self.ObtenerArch(filedir)
            
            shutil.move(filedir,filedir2)
            self.grabarArchivo(concat2,nombrearch+"\n")
            # os.remove(concat)
            registro= open(concat, 'w')
            for x in lista:
                registro.write(x)
            registro.close()
        except:
            print("\n\nNo se encuentra ningun Backup\n\n")

    def ObtenerArch(self,direccion):

        registro= open(direccion, 'r')
        print(registro.read())
        registro.close()

    def Principal(self):
        self.getUsuarios()
        print("\033[2J\033[1;1f")
        print(chr(27)+"[1;30;47m"+"\t\t***BIENVENIDO AL SISTEMA DE CONTROL DE VERSIONES***\n\n\n"+'\033[0;m')
        print(chr(27)+"[1;31m"+"\t0) Salir\n"+chr(27)+"[1;32m"+"\t1) Iniciar Sesion\n"+chr(27)+"[1;33m"+"\t2) Registrarse\n"+'\033[0;m'+'\033[0;m'+"\t3) Ver Usuarios\n"+'\035')
        print(chr(27)+"[1;30;47m"+"**Si no posee cuenta favor registrarse**\n"+'\033[0;m')
        op=int(input(chr(27)+"[1;30m"+"Seleccione una opcion: "+'\033[0;m'))
        while(op!=0):
            print("\033[2J\033[1;1f")
            if op==1:
                nombre=input("Introduzca el nombre: ")
                password=input("Introduzca la contraseña: ")
                self.InicioSesion(nombre,password)
                break
            elif op==2:
                self.Registrar()
                break
            elif op==3:
                self.VerUsuarios()
                break
            print(chr(27)+"[1;30;47m"+"\t\t***BIENVENIDO AL SISTEMA DE CONTROL DE VERSIONES***\n\n\n"+'\033[0;m')
            print(chr(27)+"[1;31m"+"\t0) Salir\n"+chr(27)+"[1;32m"+"\t1) Iniciar Sesion\n"+chr(27)+"[1;33m"+"\t2) Registrarse\n"+'\033[0;m'+'\033[0;m'+"\t3) Ver Usuarios\n"+'\035')
            print(chr(27)+"[1;30;47m"+"**Si no posee cuenta favor registrarse**\n"+'\033[0;m')
            op=int(input(chr(27)+"[1;30m"+"Seleccione una opcion: "+'\033[0;m'))
                        
    def VerUsuarios(self):
        doc=list()
        print("Los usuarios existentes son: ")
        contador=0
        for x in self.userslist:
            print(str(contador+1)+"."+x.Nombre)
            contador+=1
        nombre=input("Porfavor escriba el nombre del usuario que desea observar: ")
        for x in self.userslist:
            if nombre == x.Nombre:
                contador=0
                print("\033[2J\033[1;1f")        
                print("Los archivos del usuario "+chr(27)+"1;33m"+x.Nombre+'\033[0;m'+" son:")
                directorio="Usuarios/"+nombre
                with os.scandir(directorio) as ficheros:
                    for fichero in ficheros:
                        doc.append(directorio+"/"+fichero.name)
                        # print(str(contador+1)+"."+fichero.name)
                        contador+=1
                opcion= int(input("Digite el numero de su eleccion: "))
                directorio=doc[opcion-1]
                contador=0
                with os.scandir(directorio) as ficheros:
                    for fichero in ficheros:
                        print(str(contador+1)+"."+fichero.name)
                        contador+=1

    def getUsuarios(self):# Llenar la lista de los usuarios registrados
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                user=Usuario(line[0:line.index(" ")],line[line.index(" "):line.index("\n")],1)
                self.userslist.append(user)
    def Borrar(self):
        cadena="Hola mundo que tal, estoy programando"
        while True:
            if ms.kbhit():
                print(ms.getch())
        # while True:
            # try:
            #     if ms.kbhit() and ms.getch()==chr(13):
            #         cadena[0:len(cadena)-1]
            #         print(cadena)
            #         break #finishing the loop
            #     else:
            #         pass
            # except:
            #     break

    def Carpetas(self, nombre):# Crea Una carpeta si el usuario asi lo desea
        for x in self.userslist:
            if x.Nombre==nombre:
                x.CrearCarpeta()

    def ModificarArchivo(self, nombre):
        direccion="Usuarios/"+nombre+"/Documentos/"
        with open(direccion) as temp_f:
                archivo = temp_f.readlines()
                # for line in archivo:
                    # lista.append(line)

c=ControlVersiones()
i=0
def __main__():
    # os.mkdir("Usuarios")
    # c.getUsuarios()
    # c.Principal()
    # c.Borrar()
    # c.Registrar()
    
    # c.Carpetas("Dario")
    # c.AddFile(1,"Kendall","Hola quiubo x2+221\n haoisdjk\nasdhjkahskjh\njhskdjhkeb")
    # c.RecuperarArchivo('Kendal',1)
    # c.InicioSesion("Ian","mamapichas")

    
if __name__ =="__main__":
    __main__()