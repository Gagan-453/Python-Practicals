import mysql.connector as sq

conn = sq.connect(host='106.51.104.145', user='root', passwd="Gagan@python", database='mydatabase')
c = conn.cursor()
conn.close()

# User-name: python-user
# Password: Password1$