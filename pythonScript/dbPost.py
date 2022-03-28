import sqlite3
import sys
import json

def delete(id):
    conn = sqlite3.connect("test.db")
    with conn:
        cursor = conn.cursor()
        sql = 'DELETE FROM COUNTRY WHERE id=?'
        cursor.execute(sql,(id,))
        conn.commit()

def show():
    conn = sqlite3.connect("test.db")
    with conn:
        result = []
        #   generating a cursor from connection
        cursor = conn.cursor()
        cursor.execute('select * from COUNTRY')
        # Data fetch and printing out
        rows = cursor.fetchall()
        for row in rows:
            result.append(row)
            #print(row)
        return_value = json.dumps(result)
        print(return_value)

def insert(country):
    #   SQLite DB connection
    conn = sqlite3.connect("test.db")
    with conn:
        #   generating a cursor from connection
        cursor = conn.cursor()
        data = (
            ('Korea'),
            ('United States'),
            ('United Kingdom'),
            ('Russia'),
            ('Ukraine'),
            ('Japan'),
            ('China'),
        )
        sql = "insert into COUNTRY(NAME) values (?)"
        #cursor.executemany(sql, data)    
        cursor.execute(sql,(country))
        conn.commit()

def main(arg):
    # country = arg[:]
    country = input()
    print('coutry: ', country)
    insert(country)
    show()

if __name__ == '__main__':
    main(sys.argv[1:])