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
def crearTabla(tabla):
    conn=sql.connect("ITLA.db")
    tabla = input("Nombre:\n")
    try:       
        conn.execute(f"""if not exists create table {tabla} (
                                

        )""")
    #    conn.execute("""create table Estudiantes  (
    #                        Matricula integer,
    #                        Nombre text,
    #                        Apellido text,
    #                        Direccion text,
    #                        Telefono integer
    #                    )""")
        print("se creo la tabla Estudiantes")                        
    except sql.OperationalError:
        print("La tabla Estudiantes ya existe")         
    conn.close()

def crearTablaAsig():
    conn=sql.connect("ITLA.db")
    try:      
        conn.execute("""create table Asignacion  (
                            Matricula integer,
                            Nombre text,
                            Asignatura text
                        )""")
        print("se creo la tabla Asignacion")                        
    except sql.OperationalError:
        print("La tabla Asignacion ya existe")         
    conn.close()

def insertarFilaEstu(Matricula,Nombre,Apellido,Direccion,Telefono):
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Estudiantes VALUEs ({Matricula},'{Nombre}','{Apellido}','{Direccion}',{Telefono})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertarFilaAsign(Matricula,Nombre,Asignatura):
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Asignacion VALUEs ({Matricula},'{Nombre}','{Asignatura}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#Trabajame en esto bro
def borrarFilas():
    conn=sql.connect("ITLA.db")
    bnom=input("Ingrese la matricula que quiere borrar :")
    conn.execute(f"delete from Estudiantes where Matricula='{bnom}' ")
    print("El contacto esta borrado")
    conn.commit()
    conn.close()


def salir():
    conn = sql.connect("ITLA.db")
    conn.commit()
    conn.close()
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
    """)
        guia = int(input("Escriba el numero para realizar la operacion deseada"))
        if guia == 1:
            crearDB()
            print("Se ha iniciado la base de datos")
        elif guia == 2:
            guia = input("Nombre de la Tabla")
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




    
