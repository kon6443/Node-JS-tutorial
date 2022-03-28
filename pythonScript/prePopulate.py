import sqlite3
import sys
import json

def main(arg):
    #sql processing
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Country FROM Uni_Programs_Requ")
    data = cursor.fetchall()

    results = {}
    results["country"] = []
    last_answer = ''

    #comparing with the db file
    for row in data:
        for word in row:
            if word != last_answer and arg == word[:len(arg)].strip().lower():
                results["country"].append(word)
                last_answer = word
    return_value = json.dumps(results)
    print(return_value)

def insert(name, category, state):
    #   SQLite DB connection
    conn = sqlite3.connect("keystroke.db")
    with conn:
        #   generating a cursor from connection
        cursor = conn.cursor()
        data = (
            ('One', 1, 'Seoul'),
            ('Two', 2, 'Suwon'),
            ('Three', 3, 'Daegu')
        )
        sql = "insert into customer(name,category,region) values (?,?,?)"
        #cursor.executemany(sql, data)    
        cursor.execute(sql,(name,category,state))
        conn.commit()        


if __name__ == '__main__':
    main(sys.argv[1])
    