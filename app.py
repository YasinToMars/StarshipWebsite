from flask import Flask, render_template, request
import sqlite3
import psycopg2
import os


DATABASE_URL = os.getenv("DATABASE_URL")

### CONNECTING WITH THE DATABASE FOR CONTACT PAGE
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    print("Database connected successfully!")
except Exception as e:
    print("Error connecting to database:", e)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/multicam')
def multi_cam():
    return render_template('multicam.html')

# Route for the closures page
@app.route('/closures')
def closures():
    conn = sqlite3.connect('closures.db')
    cursor = conn.cursor()
    cursor.execute("SELECT closure_name, closure_date FROM closures")
    closures_data = cursor.fetchall()
    conn.close()
    
    return render_template("closures.html", closures=closures_data)

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        conn.commit()
        cur.close()
        return render_template('contact.html', success=True)
    except Exception as e:
        print("Error saving data:", e)
        return render_template('contact.html', success=False)
    
if __name__ == '__main__':
    app.run(debug=True)