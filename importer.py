import csv
import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='Srth#hak2411',
                     db='fyle')

cursor = db.cursor()

csv_data = csv.reader(open('Bank-Datasets/bank_branches.csv'))

for row in csv_data:
    cursor.execute('INSERT INTO api_branch(ifsc, bank_id, branch, address, city, district, state, bank_name) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', row)
    print('Inserted '+row[0])

db.commit()
cursor.close()
print('Done')
