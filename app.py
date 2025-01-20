from flask import Flask, render_template, request
import sqlite3
import psycopg2
import os

app = Flask(__name__)

# Route for the homepage
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

# Fetch DATABASE_URL from environment variables (use External URL if running locally)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://starshipcontactus_user:zag0Thjg9L1E4muCunhZZe5BsY6IoLKU@dpg-cu76hobqf0us73e2bh80-a/starshipcontactus"
)

# Connect to the database
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    print("Database connected successfully!")
except Exception as e:
    print("Error connecting to database:", e)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save the data in the database
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

    return render_template('contact.html', success=True)
if __name__ == '__main__':
    app.run(debug=True)


