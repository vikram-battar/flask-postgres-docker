from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def db_connection():
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "db"),
        database=os.environ.get("POSTGRES_DB", "appdb"),
        user=os.environ.get("POSTGRES_USER", "appuser"),
        password=os.environ.get("POSTGRES_PASSWORD", "apppass"),
        port=os.environ.get("POSTGRES_PORT", "5432"),
    )

@app.route("/")
def hello():
    # Simple DB check
    try:
        conn = db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()
        status = "DB OK"
    except Exception as e:
        status = f"DB ERROR: {e}"
    return f"Hello from Flask! [{status}]"

