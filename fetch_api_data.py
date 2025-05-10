import requests
import mysql.connector
from datetime import datetime

def fetch_and_store_data():
    url = "https://api.fda.gov/drug/enforcement.json?limit=10"
    response = requests.get(url)
    data = response.json()["results"]

    conn = mysql.connector.connect(host="localhost", user="root", password="yourpass", database="rag_db")
    cursor = conn.cursor()

    for item in data:
        cursor.execute(
            "INSERT INTO drug_recalls (product_description, recall_reason, recall_date) VALUES (%s, %s, %s)",
            (item["product_description"], item["reason_for_recall"], item["recall_initiation_date"])
        )
    conn.commit()
    cursor.close()
    conn.close()
