import sqlite3
import json
import matplotlib.pyplot as plt
import numpy as np


# SQLite DB Name
DB_Name =  "jal2018.db"

#===============================================================
# Database Manager Class

# class DatabaseManager():
# 	def __init__(self):
# 		self.conn = sqlite3.connect(DB_Name)
# 		self.conn.execute('pragma foreign_keys = on')
# 		self.conn.commit()
# 		self.cur = self.conn.cursor()
#
#     def read_from_db():
#
#
# 	def add_del_update_db_record(self, sql_query, args=()):
# 		self.cur.execute(sql_query, args)
# 		self.conn.commit()
# 		return
#
# 	def __del__(self):
# 		self.cur.close()
# 		self.conn.close()
#
#
# # Function to save Humidity to DB Table
# def DHT22_Humidity_Data_Plotter():
# 	#Read from DB Table
# 	dbObj = DatabaseManager()
conn = sqlite3.connect(DB_Name)
cursor = conn.cursor()

#Print all the Temperature Data.
cursor.execute("SELECT * FROM DHT22_Temperature_Data")
results = cursor.fetchall()
time = len(results)
time_rng = np.arange(time)
temp = np.zeros(time)
i=0
for row in results:
    print(row[3])
    temp[i] = float(row[3])
    i += 1


print(time_rng)
print(temp)

#plt.scatter(time_rng,temp)
plt.plot(time_rng,temp)
plt.plot(time_rng,temp,'or')
plt.show()
# #Print all the Humidity Data.
# cursor.execute("SELECT * FROM DHT22_Humidity_Data")
# results = cursor.fetchall()
# for row in results:
#     print(row)
