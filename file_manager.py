import asyncio
import sqlite3

class FileManager:
    def __init__(self, db_path):
        self.db_path = db_path

    async def run(self):
        while True:
            await asyncio.sleep(5)  # Periodic tasks like data cleanup or autosave
            self.save_simulation_state()

    def save_simulation_state(self):
        conn = sqlite3.connect(self.db_path)
        with conn:
            conn.execute("CREATE TABLE IF NOT EXISTS state (id INTEGER PRIMARY KEY, data TEXT)")
            conn.execute("INSERT INTO state (data) VALUES (?)", ("Simulation data",))
        print("Simulation state saved.")
