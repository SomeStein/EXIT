import asyncio
from concurrent.futures import ProcessPoolExecutor
from ui import start_ui

class SimulationEnvironment:
    def __init__(self, file_manager):
        self.file_manager = file_manager
        self.executor = ProcessPoolExecutor()
        self.tasks = []

    async def run(self):
        # Start UI in a separate thread
        ui_task = asyncio.create_task(start_ui(self))
        self.tasks.append(ui_task)

        # Example: Add simulation tasks
        while True:
            await self.schedule_simulation_task()
            await asyncio.sleep(1)  # Adjust interval as needed

    async def schedule_simulation_task(self):
        result = await asyncio.get_event_loop().run_in_executor(
            self.executor, self.run_simulation_step
        )
        print(f"Simulation step result: {result}")

    def run_simulation_step(self):
        # Example calculation
        return sum(i * i for i in range(10**6))

