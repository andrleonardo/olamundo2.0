



cursor=0
conexao=0
def crudopen():
    import  mysql.connector 
    conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
    )
    cursor=conexao.cursor()
    cursor.close()
    conexao.close()

def crudclose():
    cursor.close()
    conexao.close()