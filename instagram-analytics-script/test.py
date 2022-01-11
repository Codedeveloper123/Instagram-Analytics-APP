import sqlite3

conn = sqlite3.connect("instagramstats.db")
c = conn.cursor()
c.execute("""SELECT * FROM instagramstatistics""")
l = c.fetchall()
print(len(l))
# c.execute("""SELECT * FROM latestpoststats""")
# m = c.fetchall()
# print(m)
