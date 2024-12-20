import asyncio
import concurrent.futures
import sqlite3
from simulation_environment import SimulationEnvironment
from file_manager import FileManager

async def main():
    # Initialize components
    db_path = "data/simulations_data.db"
    file_manager = FileManager(db_path)
    simulation_env = SimulationEnvironment(file_manager)

    # Start simulation and file management
    await asyncio.gather(
        simulation_env.run(),
        file_manager.run(),
    )

if __name__ == "__main__":
    asyncio.run(main())

