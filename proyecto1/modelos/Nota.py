import mysql.connector
from datetime import datetime

database = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="",
                                   database="master_python",
                                   port=3306)

cursor = database.cursor(
    buffered=True
)  # El parametro buffered sirve para que el mismo cursor pueda ejecutar varias consultas


class Nota:

    id_usuario: int
    titulo: str
    nota: str

    def __init__(self, id_usuario, titulo, nota):
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.nota = nota

    def crear_nota(self):
        try:
            sql_request = f"INSERT INTO notas VALUES (null, {self.id_usuario}, '{self.titulo}', '{self.nota}', '{datetime.now()}')"
            cursor.execute(sql_request)
            database.commit()
            return cursor.rowcount()
        except Exception as err:
            print("Error al crear la nota. " + str(type(err).__name__) + ": " +
                  str(err))

    def buscar_notas(self):
        try:
            sql_request = f"SELECT * FROM notas WHERE id_usuario={self.id_usuario}"
            cursor.execute(sql_request)
            notas = cursor.fetchall()
            return notas
        except Exception as err:
            print("Error al buscar las nota. " + str(type(err).__name__) +
                  ": " + str(err))

    def borrar_nota(self, codigo):
        try:
            sql_request = f"DELETE FROM notas WHERE id={codigo}"
            cursor.execute(sql_request)
            database.commit()
            return True
        except Exception as err:
            print("Error al borrar la nota. " + str(type(err).__name__) +
                  ": " + str(err))

    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def get_id_usuario(self):
        return self.id_usuario

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_nota(self, nota):
        self.nota = nota

    def get_nota(self):
        return self.nota
