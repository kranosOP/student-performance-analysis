import mysql.connector
import pandas as pd

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="student_db"
)
cursor = db.cursor()

# Fetch student performance data
query = "SELECT * FROM performance;"
df = pd.read_sql(query, db)

# Calculate performance percentage
df['percentage'] = (df['marks_obtained'] / df['total_marks']) * 100

# Identify students at dropout risk
dropout_risk = df[(df['percentage'] < 40) & (df['attendance'] < 50)]

print("Students at dropout risk:")
print(dropout_risk)

db.close()
