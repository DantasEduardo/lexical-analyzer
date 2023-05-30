"""
CREATE TABLE IF NOT EXISTS `lexical` (
    id int PRIMARY KEY AUTO_INCREMENT,
    phrase varchar(255),                      
    value  INT,                    
    search  varchar(30),                    
    date DATE
);
"""


import mysql.connector
from datetime import datetime

QUERY = 'INSERT INTO lexical(phrase, value, search, date) VALUES (%s,%s,%s,%s)'

def upload_data(registers:dict):
    print("INFO: Conecting with DB")
    mydb = mysql.connector.connect(
        host = 'soy-bean-02211010.mysql.database.azure.com',
        user = 'root02211010',
        database = 'sensor_data',
        password = '**********',
        port = "3306")

    mycursor = mydb.cursor()

    for key in registers.keys():
        print(f"INFO: Sending {key} search result")
        for values in registers[key]:
            mycursor.execute(QUERY, [",".join(values[0]), values[1], key, datetime.now().date()])
            mydb.commit()
            