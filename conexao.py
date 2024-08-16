import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Pizzaateotalo',
        database='bancodoleo'
    )
    cursor = conexao.cursor()
    return conexao, cursor

def fechar_conexao(cursor, conexao):
    cursor.close()
    conexao.close()
