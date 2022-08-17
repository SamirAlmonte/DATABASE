#Importo sql lite y lo nombro como sql para acortar.
import sqllite3 as sql 

#Referentes: 
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=87&codigo=88&inicio=75



def createDB():
    conn=sql.connect("ITLA.db")
    conn.commit()
    conn.close()
                  
def createTable():
    conn=sql.connect("ITLA.db")
    try:
        conn.execute("""create table Estudiantes (
                                codigo integer primary key autoincrement,
                                descripcion text,
                                precio real
                            )""")
        print("se creo la tabla articulos")                        
    except sql.OperationalError:
        print("La tabla articulos ya existe")         
    conn.close()

#Llamo las funciones 
if __name__ == "__main__":
    pass