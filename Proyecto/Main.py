#Importo sql lite y lo nombro como sql para acortar.
import sqlite3 as sql
import string 

#Referentes: 
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=87&codigo=88&inicio=75
#https://conclase.net/c/sqlite/litesen/CREATE_TABLE#:~:text=La%20sentencia%20CREATE%20TABLE%20se,El%20nombre%20de%20la%20tabla.


def crearDB():
    conn=sql.connect("ITLA.db")
    conn.commit()
    conn.close()
#Arreglar la funcion de Crear tabla,
#agregando una variable y haciendo uso de la sintaxix(F"Variable")
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
    print("Ingrese los siguientes datos \n\n")
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


def borrarFilas():
    conn=sql.connect("ITLA.db")
    matricula=input("Ingrese la matricula que quiere borrar:")
    conn.execute(f"delete from Estudiantes where Matricula='{matricula}' ")
    print("El estudiante ha sido eliminado")
    conn.commit()
    conn.close()


def salir():
    crearDB()
    print ("Bye")







def readRows(tabla):
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM {tabla}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print("Tabla {tabla} \n",datos)
    print("")

#Llamo las funciones 
if __name__ == "__main__":
    while True:
        print("""
        1 - Inicializar Base de Datos
        2 - Crear
        3 - Datos
        4 - Añadir
        5 - Actualizar
        6 - Busqueda
        7 - Borrar
        8 - Salir
    """)
        guia = int(input("Escriba el numero para realizar la operacion deseada"))
        if guia == 1:
            crearDB()
            print("Se ha iniciado la base de datos")
        elif guia == 2:
            guia = input("¿Que tabla quieres crear?")
            crearTablaAsig()
            #crearTabla(guia)

        elif guia == 3:
            pass

        elif guia == 4:
            pass

        elif guia == 5:
           pass 

        elif guia == 6:
            readRows("Asignacion") 
        
        elif guia == 7:
             borrarFilas()

        elif guia == 8:
             borrarFilas()    

        else:
            break
    #crearTablaEstu()
    #insertarFilaAsign(20220726,"Samir","Educacion Fisica")
    #insertarFilaEstu(20220726,"Samir","Almonte","resp. Villa Carmen",8097775525)
    

    

#def borrar():
    #bnom=input("Ingrese el nombre del contacto que quiere borra :")
    #conexion.execute(f"delete from Estudiantes where Matricula='{bnom}' ")
    #print("El contacto esta borrado")
    #conn.commit()
    #conn=sql.connect("ITLA.db")




    
