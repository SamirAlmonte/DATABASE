#Importo sql lite y lo nombro como sql para acortar.
from asyncore import read
import sqlite3 as sql
 
#Base de datos ITLA por
#Samir Almonte
#Zayas

#Referentes: 
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=87&codigo=88&inicio=75
#https://conclase.net/c/sqlite/litesen/CREATE_TABLE#:~:text=La%20sentencia%20CREATE%20TABLE%20se,El%20nombre%20de%20la%20tabla.


def crearDB():
    conn=sql.connect("ITLA.db")
    conn.commit()
    conn.close()

def crearTablaEstu():
    conn=sql.connect("ITLA.db")
    try:       
        conn.execute("""create table Estudiantes  (
                           Matricula integer NOT NULL,
                            Nombre text NOT NULL,
                            Apellido text NOT NULL,
                            Direccion text NOT NULL,
                            Telefono integer NOT NULL
                        )""")
        print("se creo la tabla Estudiantes")                        
    except sql.OperationalError:
        print("La tabla Estudiantes ya existe")         
    conn.close()

def crearTablaAsig():
    conn=sql.connect("ITLA.db")
    try:      
        conn.execute("""create table Asignaturas  (
                            Matricula integer NOT NULL,
                            Nombre text NOT NULL,
                            Asignatura text NOT NULL
                        )""")
        print("se creo la tabla Asignaturas")                        
    except sql.OperationalError:
        print("La tabla Asignaturas ya existe")         
    conn.close()

def insertarFilaEstu():
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()

    print("Ingrese los siguientes datos: \n\n")
    Matricula = int(input("Matricula:\n"))
    Nombre = input("Nombre:\n")
    Apellido = input("Apellido:\n")
    Direccion = input("Direccion:\n")
    Telefono = int(input("Telefono:\n"))

    instruccion = f"INSERT INTO Estudiantes VALUES ({Matricula},'{Nombre}','{Apellido}','{Direccion}',{Telefono})"
    cursor.execute(instruccion)
    conn.commit()
    

def insertarFilaAsign():
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()

    Matricula = int(input("Matricula:\n"))
    Nombre = input("Nombre:\n")
    Asignatura = input("Asignatura:\n")

    instruccion = f"INSERT INTO Asignatura VALUES ({Matricula},'{Nombre}','{Asignatura}')"
    cursor.execute(instruccion)
    conn.commit()



def borrarFilas(tabla):
    conn=sql.connect("ITLA.db")
    matricula=input("Ingrese la matricula que quiere borrar:")
    conn.execute(f"delete from {tabla} where Matricula='{matricula}' ")
    print("El estudiante ha sido eliminado")
    conn.commit()


def salir():
    input("\nPresione Enter para continuar")
    sql.connect("ITLA.db").close
    print ("Bye-Bye")
    input()
    borrarPantalla()
    

def actualizarAsig():
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()

    print("Actualice los siguientes datos \n\n")
    Matricula = int(input("Matricula:\n"))
    Nombre = input("Nombre:\n")
    Asignatura = input("Asignatura:\n")

    cursor.execute(f" update Asignacion set Matricula= {Matricula},{Nombre},{Asignatura}")

    

def actualizarEstu():
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()

    print("Actualice los siguientes datos \n\n")
    Matricula = int(input("Matricula:\n"))
    Nombre = input("Nombre:\n")
    Apellido = input("Apellido:\n")
    Direccion = input("Direccion:\n")
    Telefono = int(input("Telefono:\n"))

    cursor.execute(f" update Asignacion set Matricula ({Matricula},'{Nombre}','{Apellido}','{Direccion}',{Telefono})")
    


def readRows(tabla):
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM {tabla}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(f"Tabla {tabla} \n",datos)
    print("")

    
def buscar(tabla):
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()
    matricula=(input("Ingrese la matricula que quiere buscar:\n"))
    instruccion = f"SELECT * FROM {tabla} WHERE Matricula = {matricula}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    print(f"Tabla {tabla} \n",datos)
    print("")

def borrarPantalla(): 
    import os
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#Llamo las funciones 
if __name__ == "__main__":
    borrarPantalla()
    while True:
        borrarPantalla()
        print("""
        1 - Inicializar Base de Datos
        2 - Crear
        3 - Lectura
        4 - Busqueda
        5 - Añadir
        6 - Actualizar
        7 - Borrar
        8 - Salir
        0 - Limpiar la pantalla
    """)
        guia = int(input("Escriba el numero para realizar la operacion deseada\n"))
        if guia == 1:   #Inicializar
            crearDB()
            print("Se ha iniciado la base de datos")
            input("Presione la tecla Enter para continuar")
            borrarPantalla()

        elif guia == 2: #Crear
            borrarPantalla()
            crearTablaEstu()
            crearTablaAsig()
            input("\n Se han creado las tablas con exito")
            borrarPantalla()
                

        elif guia == 3: #Lectura
            guia = input("¿Que tabla quieres leer?\n[1]Asignatura\n[2]Estudiantes")
            if guia == "1":
                readRows("Asignatura")
                input("Presione la tecla Enter para continuar")
            elif guia =="2":
                readRows("Estudiantes")
                input("Presione la tecla Enter para continuar")
            
            
        
        elif guia == 5: #Anadir, pendiente
            borrarPantalla()
            guia = input("¿A que tabla quieres añadir una fila?\n[1]Asignatura\n[2]Estudiantes") 
            if guia == "1":
                insertarFilaAsign()
                input("Presione la tecla Enter para continuar")
            elif guia =="2":
                insertarFilaEstu()
                input("Presione la tecla Enter para continuar")
            else:
                print("Esa tabla no existe")
                input("Presione la tecla Enter para continuar")
            borrarPantalla()
            
           
        elif guia == 6: #Actualizar
            borrarPantalla()
            guia = input("¿Que tabla quieres actualizar?\n[1]Asignatura\n[2]Estudiantes")
            if guia == "2":
                actualizarEstu()
                input("Presione la tecla Enter para continuar")
            elif guia =="1":
                actualizarAsig()
                input("Presione la tecla Enter para continuar")
            print("Se ha actualizado la tabla con exito")
            borrarPantalla()

        elif guia == 4: #Busqueda
            guia = input("¿En que tabla quieres buscar?\n[1]Asignatura\n[2]Estudiantes")
            if guia == "1":
                guia = "Asignatura"
                buscar(guia)
                input("Presione la tecla Enter para continuar")
            elif guia== "2":
                guia = "Estudiantes"
                buscar(guia)
                input("Presione la tecla Enter para continuar")
            else:
                print("Esa tabla no existe")

        elif guia == 7: #Borrar
            guia = input("¿En que tabla quieres borrar una fila?\n[1]Asignatura\n[2]Estudiantes")
            if guia == "1":
                guia = "Asignatura"
                borrarFilas(guia)
                input("Presione la tecla Enter para continuar")
            elif guia == "2":
                guia = "Estudiantes"
                borrarFilas(guia)
                input("Presione la tecla Enter para continuar")
            else:
                print("Esa tabla no existe")

        elif guia == 8: #Salir
             salir()   

        elif guia == 0: #Limpiar la pantalla
            borrarPantalla()
        else:
            break
   








