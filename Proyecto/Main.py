#Importo sql lite y lo nombro como sql para acortar.
from asyncore import read
import sqlite3 as sql
 
#Base de datos ITLA por:
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
        conn.execute("""CREATE TABLE Estudiantes  (
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
        conn.execute("""CREATE TABLE Asignaturas  (
                            Matricula integer NOT NULL,
                            Nombre text NOT NULL,
                            Asignatura text NOT NULL
                        )""")
        print("se creo la tabla Asignaturas")                        
    except sql.OperationalError:
        print("La tabla Asignaturas ya existe")         
    conn.close()
def insertarFilaEstu():
    try:
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
    except sql.OperationalError:
        print("Ha habido un error al insertar valores")
def insertarFilaAsign():
    try:
        conn=sql.connect("ITLA.db")
        cursor = conn.cursor()

        Matricula = int(input("Matricula:\n"))
        Nombre = input("Nombre:\n")
        Asignatura = input("Asignatura:\n")

        instruccion = f"INSERT INTO Asignaturas VALUES ({Matricula},'{Nombre}','{Asignatura}')"
        cursor.execute(instruccion)
        conn.commit()
    except sql.OperationalError:
        print("Ha habido un error al insertar valores")
def borrarFilas(tabla):
    conn=sql.connect("ITLA.db")
    matricula=input("Ingrese la matricula que quiere borrar:")
    conn.execute(f"DELETE FROM {tabla} WHERE Matricula='{matricula}' ")
    print("El estudiante ha sido eliminado")
    conn.commit()
def actualizarAsig():
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()

    Matricula=input("Ingrese la matricula que quiere actualizar:")
    borrarPantalla()
    print("Actualice los siguientes datos \n\n")

    Nombre = input("Nombre:\n")
    Asignatura = input("Asignatura:\n")

    cursor.execute(f""" UPDATE Asignaturas SET Nombre="{Nombre}",Asignatura="{Asignatura}" WHERE Matricula={Matricula}""")
    conn.commit()
def actualizarEstu():
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()

    Matricula=input("Ingrese la matricula que quiere actualizar:")
    borrarPantalla()

    Nombre = input("Nombre:\n")
    Apellido = input("Apellido:\n")
    Direccion = input("Direccion:\n")
    Telefono = int(input("Telefono:\n"))

    cursor.execute(f""" UPDATE Estudiantes SET Nombre="{Nombre}",Apellido="{Apellido}",Direccion="{Direccion}",Telefono={Telefono} WHERE Matricula={Matricula}""")
    conn.commit()
def readRows(tabla):
    print("")
    conn=sql.connect("ITLA.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM {tabla}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    if datos==[]:
        print(f"La tabla {tabla} esta vacia")
    else:
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
def salir():
    input("\nPresioneEnter para continuar")
    sql.connect("ITLA.db").close
    borrarPantalla()
    input("Bye-Bye")
    borrarPantalla()
    return False 
#Llamo las funciones 
if __name__ == "__main__":
    borrarPantalla()
    c = True
    C = False
    while c==True:
        borrarPantalla()
        print("""
        [1] - Inicializar Base de Datos
        [2] - Crear
        [3] - Lectura
        [4] - Busqueda
        [5] - A??adir
        [6] - Actualizar
        [7] - Borrar
        [8] - Salir""") 
        if C==True:
            print("      Recuerda salir al terminar!")
        guia = int(input("Escriba el numero para realizar la operacion deseada\n"))
        if guia == 1:   #Inicializar
            crearDB()
            print("Se ha iniciado la base de datos")
            input("Enter para continuar")
            borrarPantalla()
            C=True
        elif guia == 2: #Crear
            borrarPantalla()
            crearTablaEstu()
            crearTablaAsig()
            input("\n Se han creado las tablas con exito")
            borrarPantalla()
            C=True
        elif guia == 3: #Lectura
            guia = input("??Que tabla quieres leer?\n[1]Asignaturas\n[2]Estudiantes\n[0]Ambas\n")
            if guia == "1":
                readRows("Asignaturas")
                input("Enter para continuar")
            elif guia =="2":
                readRows("Estudiantes")
                input("Enter para continuar")
            elif guia == "0":
                readRows("Estudiantes")
                readRows("Asignaturas")
                input("\nEnter para continuar")
            C=True
        elif guia == 5: #Anadir
            borrarPantalla()
            guia = input("??A que tabla quieres a??adir una fila?\n[1]Asignatura\n[2]Estudiantes\n") 
            if guia == "1":
                insertarFilaAsign()
                input("Enter para continuar")
            elif guia =="2":
                insertarFilaEstu()
                input("Enter para continuar")
            else:
                print("Esa tabla no existe")
                input("Enter para continuar")
            borrarPantalla()
            C=True
        elif guia == 6: #Actualizar
            borrarPantalla()
            guia = input("??Que tabla quieres actualizar?\n[1]Asignaturas\n[2]Estudiantes\n")
            if guia == "2":
                actualizarEstu()
                input("Se ha actualizado la tabla con exito")
            elif guia =="1":
                actualizarAsig()
                input("Se ha actualizado la tabla con exito")
            input("Enter para continuar")
            borrarPantalla()
            C=True
        elif guia == 4: #Busqueda
            guia = input("??En que tabla quieres buscar?\n[1]Asignaturas\n[2]Estudiantes\n")
            if guia == "1":
                guia = "Asignaturas"
                buscar(guia)
                input("Enter para continuar")
            elif guia== "2":
                guia = "Estudiantes"
                buscar(guia)
                input("Enter para continuar")
            else:
                print("Esa tabla no existe")
            C=True
        elif guia == 7: #Borrar
            guia = input("??En que tabla quieres borrar una fila?\n[1]Asignaturas\n[2]Estudiantes\n")
            if guia == "1":
                guia = "Asignaturas"
                borrarFilas(guia)
                input("Enter para continuar")
            elif guia == "2":
                guia = "Estudiantes"
                borrarFilas(guia)
                input("Enter para continuar")
            else:
                print("Esa tabla no existe")
            C=True
        elif guia == 8: #Salir
             c=salir()   
        else:
            input("ERROR! Esa opcion no existe :(")
            break