# Import module 
import psycopg2


# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
        user="postgres",
        password="Tanzeem@12345",
        host="localhost",
        port=5432,
        database="generative_ai"
    )

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Creating table 

cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT (NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255));''')
#table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
#SECTION VARCHAR(255));"""
#cursor.execute(table) 

# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Tanzeem', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Fazlur', 'Data Science', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Khateeb', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Mudasieer', 'Data Science', 'C')''') 

# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 

#for row in data:
#    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()
