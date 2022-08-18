#Importo sql lite y lo nombro como sql para acortar.
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
                           Matricula integer,
                            Nombre text,
                            Apellido text,
                            Direccion text,
                            Telefono integer
                        )""")
        print("se creo la tabla Estudiantes")                        
    except sql.OperationalError:
        print("La tabla Estudiantes ya existe")         
    conn.close()

def crearTablaAsig():
    conn=sql.connect("ITLA.db")
    try:      
        conn.execute("""create table Asignacion  (
                            Matricula integer NOT NULL,
                            Nombre text NOT NULL,
                            Asignatura text NOT NULL
                        )""")
        print("se creo la tabla Asignacion")                        
    except sql.OperationalError:
        print("La tabla Asignacion ya existe")         
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

    instruccion = f"INSERT INTO Estudiantes VALUEs ({Matricula},'{Nombre}','{Apellido}','{Direccion}',{Telefono})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertarFilaAsign():
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()

    Matricula = int(input("Matricula:\n"))
    Nombre = input("Nombre:\n")
    Asignatura = input("Asignatura:\n")

    instruccion = f"INSERT INTO Asignacion VALUEs ({Matricula},'{Nombre}','{Asignatura}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def borrarFilas(tabla):
    conn=sql.connect("ITLA.db")
    matricula=input("Ingrese la matricula que quiere borrar:")
    conn.execute(f"delete from {tabla} where Matricula='{matricula}' ")
    print("El estudiante ha sido eliminado")
    conn.commit()
    conn.close()


def salir():
    sql.connect("ITLA.db").close
    borrarPantalla()
    print ("Bye-Bye")

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
    conn.close()
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
    while True:
        print("""
        1 - Inicializar Base de Datos
        2 - Crear
        3 - Lectura
        4 - Añadir
        5 - Actualizar
        6 - Busqueda
        7 - Borrar
        8 - Salir
        0 - Limpiar la pantalla
    """)
        guia = int(input("Escriba el numero para realizar la operacion deseada"))
        if guia == 1:   #Inicializar
            crearDB()
            print("Se ha iniciado la base de datos")
            borrarPantalla()

        elif guia == 2: #Crear
            guia = input("¿Que tabla quieres crear?\n")
            
            if guia == "Estudiantes" or "estudiantes":
                crearTablaEstu()
            elif guia == "Asignacion" or "asignacion":
                crearTablaAsig()
            else:
                print("Ese nombre no, otro-")
                

        elif guia == 3: #Lectura
            guia = input("¿Que tabla quieres leer?\n")
            
        
        elif guia == 4: #Anadir, pendiente
           guia = input("¿A que tabla quieres añadir una fila?\n") 
           if guia == "Estudiantes" or "estudiantes":
                insertarFilaAsign()
           elif guia == "Asignacion" or "asignacion":
                insertarFilaEstu()
           else:
                print("Ese nombre no, otro-")  
           
        elif guia == 5: #Actualizar
            guia = input("¿Que tabla quieres actualizar?\n")
            if guia == "Estudiantes" or "estudiantes":
                actualizarEstu()
            elif guia == "Asignacion" or "asignacion":
                actualizarAsig()
    
        elif guia == 6: #Busqueda
            guia = input("¿En que tabla quieres buscar?\n")
            if guia == "Estudiantes" or "estudiantes" or "Asignacion" or "asignacion":
                buscar(guia)
            else:
                print("Esa tabla no existe")
        
        elif guia == 7: #Borrar
            guia = input("¿En que tabla quieres borrar una fila?\n")
            if guia == "Estudiantes" or "estudiantes" or "Asignacion" or "asignacion":
                borrarFilas(guia)
            else:
                print("Esa tabla no existe")

        elif guia == 8: #Salir
             salir()   

        elif guia == 0: #Limpiar la pantalla
            borrarPantalla()
        else:
            break
   








