import csv
from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 
  
app = Flask(__name__) 
  
# Connect to the database 
conn = psycopg2.connect(database="essentia_music", user="damlaonder", 
                        password="donder", host="localhost", port="5432") 
  
# create a cursor 
cur = conn.cursor() 

# commit the changes 
conn.commit() 
  
# close the cursor and connection 
cur.close() 
conn.close() 
  
  
@app.route('/') 
def index(): 
    # Connect to the database 
    conn = psycopg2.connect(database="essentia_music", user="damlaonder", 
                        password="donder", host="localhost", port="5432") 
  
    # create a cursor 
    cur = conn.cursor() 
  
    # Select all products from the table 
    cur.execute('''SELECT * FROM essentia_music''') 
  
    # Fetch the data 
    data = cur.fetchall() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
  
    return render_template('index.html', data=data) 
  
  
  
  
  
if __name__ == '__main__': 
    app.run(debug=True) 