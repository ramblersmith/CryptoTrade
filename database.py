
import sqlite3

def db_exists(db_name):
    # check if database exists, and if not create it

def write_historic_data(exchange_prices):
    conn = sqlite3.connect('db/crypto.db')
    c = conn.cursor()
    # Create table Historic_Price
    c.execute("CREATE TABLE Historic_Price (Timestamp text, Exchange text, Bid_Price real, Bid_Volume real, Ask_Price real, Ask_Volume)")
    # Insert a row of data
    c.executemany("INSERT INTO Historic_Price VALUES (?,?,?,?,?,?)", exchange_prices)
    # Save (commit) the changes
    conn.commit()

