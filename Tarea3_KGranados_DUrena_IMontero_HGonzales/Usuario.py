import os
class Usuario:
    def __init__(self) -> None:
        pass
    def __init__(self, Nombre, Contra,Permiso):
        self.Nombre=Nombre
        self.Contra=Contra
        self.Permiso=Permiso
        self.DatoActual=""
    def toString(self):
        sstream="Nombre: "+self.Nombre+"\nContraseña: "+self.Contra+"\nPermiso: "+str(self.Permiso)+"\n"
        return str(sstream)
    def CrearCarpeta(self):
        direccion="Usuarios/"+self.Nombre+"/"+input("Digite el nombre de la Carpeta: ")
        try:
            os.mkdir(direccion)
        except:
            print("No se pudo crear la carpeta en la direccion: "+direccion)
    