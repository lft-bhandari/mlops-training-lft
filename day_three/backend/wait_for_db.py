import time
import socket
import os

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_PORT = 3306

print("Waiting for MySQL...")

while True:
    try:
        sock = socket.create_connection((DB_HOST, DB_PORT), timeout=2)
        sock.close()
        print("✅ MySQL is ready!")
        break
    except OSError:
        print("❌ MySQL not ready, retrying...")
        time.sleep(2)
