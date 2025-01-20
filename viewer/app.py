from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)


DATABASE_URL = os.getenv("DATABASE_URL")

def get_messages():
    try:
        # Connect to the database
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cur = conn.cursor()

        # Query to fetch all messages
        cur.execute("SELECT name, email, message FROM contact ORDER BY submitted_at DESC;")
        messages = cur.fetchall()  # Fetch all rows

        cur.close()
        conn.close()
        return messages
    except Exception as e:
        print(f"Error fetching messages from the database: {e}")
        return []

@app.route('/')
def display_messages():
    messages = get_messages()

    return render_template('display.html', messages=messages)

if __name__ == "__main__":
    app.run(debug=True)