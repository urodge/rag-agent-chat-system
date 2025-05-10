import mysql.connector

def get_recent_drug_recalls(limit=5):
    conn = mysql.connector.connect(host="localhost", user="root", password="yourpass", database="rag_db")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM drug_recalls ORDER BY recall_date DESC LIMIT %s", (limit,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
