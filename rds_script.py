import mysql.connector

# Connect to RDS
conn = mysql.connector.connect(
    host="studentdb.c6js08okwcpt.us-east-1.rds.amazonaws.com",  # Your RDS endpoint
    user="admin",  # Your RDS username
    password="Plmzaq1234",  # Replace with your actual password
    database="University"  # The database you created
)

cursor = conn.cursor()

# Insert Data
cursor.execute("INSERT INTO Students (StudentID, Name, Age, Department) VALUES (2, 'Jane Smith', 22, 'Mathematics')")
conn.commit()

# Fetch Data
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()


