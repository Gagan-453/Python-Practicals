import mysql.connector as sq

conn = sq.connect(user='root', host='localhost', password="Gagan@python")
c = conn.cursor()

conn.close()

# me: fe80::d0e6:8801:ae56:2bff