import sqlite3
from hashlib import sha256

def init_db():
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    
    # Create table for storing hashed Aadhaar numbers
    c.execute('''CREATE TABLE IF NOT EXISTS voters
                 (aadhaar_hash text PRIMARY KEY)''')
    
    conn.commit()
    conn.close()

def check_voter(aadhaar_number):
    """Check if Aadhaar number already voted"""
    aadhaar_hash = sha256(aadhaar_number.encode()).hexdigest()
    
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    
    c.execute("SELECT 1 FROM voters WHERE aadhaar_hash=?", (aadhaar_hash,))
    exists = c.fetchone() is not None
    
    conn.close()
    return exists

def add_voter(aadhaar_number):
    """Add Aadhaar number to database"""
    aadhaar_hash = sha256(aadhaar_number.encode()).hexdigest()
    
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    
    try:
        c.execute("INSERT INTO voters VALUES (?)", (aadhaar_hash,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:  # Aadhaar already exists
        return False
    finally:
        conn.close()

# Initialize the database when this module is imported
init_db()