import datetime
import os
import subprocess
class Usuario:
    def __init__(self) -> None:
        pass
    def __init__(self, Nombre, Contra,Permiso):
        self.Nombre=Nombre
        self.Contra=Contra
        self.Permiso=Permiso
        self.DatoActual=""
        self.Temporal=""
        self.Permanete=""
        self.NombreCarpeta=""
    def toString(self):
        sstream="Nombre: "+self.Nombre+"\nContraseña: "+self.Contra+"\nPermiso: "+str(self.Permiso)+"\n"
        return str(sstream)
    def CrearCarpeta(self):
        direccion="Usuarios/"+self.Nombre+"/"+input("Digite el nombre de la Carpeta: ")
        try:
            os.mkdir(direccion)
        except:
            print("No se pudo crear la carpeta en la direccion: "+direccion)
    def CrearArchivo(self, name):
        direccion="Usuarios/"+self.Nombre+"/Documentos/"+name+".txt"
        self.Temporal="Usuarios/"+self.Nombre+"/Temp/"+name
        self.Permanete="Usuarios/"+self.Nombre+"/Perm/"+name
        self.NombreCarpeta=name
        registro= open(direccion, 'w')
        registro.write('')
        registro.close()
        subprocess.run(["notepad.exe",direccion])
        
        os.mkdir(self.Temporal)#Crea una carpeta personal para los datos de cada archivo
        os.mkdir(self.Permanete) 

        with open(direccion) as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                self.DatoActual+=line
