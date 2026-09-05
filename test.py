import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="eduadapt",
        port=3306
    )

    print("Connected Successfully!")

except Exception as e:
    print(e)