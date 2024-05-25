import mysql.connector
from mysql.connector import Error

def koneksi():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pbotest"
        )
        
        if mydb.is_connected():
            print("Berhasil Koneksi ke Database")
            return mydb
        else:
            print("Koneksi Gagal")
            return None
        
    except Error as e:
        print(f"Terjadi kesalahan saat menghubungkan ke database: {e}")
        return None

def query(p):
    mydb = koneksi()
    query_result = None
    if mydb:
        try:
            CMD = mydb.cursor()
            CMD.execute(p)
            query_result = CMD.fetchall()
            for row in query_result:
                print(row)
        except Error as e:
            print(f"Terjadi kesalahan saat menjalankan query: {e}")
        finally:
            if mydb.is_connected():
                mydb.close()
                print("Koneksi ke database ditutup")
    else:
        print("Tidak dapat membuat koneksi ke database untuk menjalankan query.")
    return query_result  # Mengembalikan hasil query
