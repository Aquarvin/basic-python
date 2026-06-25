import asyncio
from models import Driver

async def fetch_driver_data(name: str, points: int) -> Driver:
    print(f"Загружаю данные {name}...")
    await asyncio.sleep(1)
    a = Driver(name, points)
    return a

async def main():
    drivers = await asyncio.gather(
        fetch_driver_data('Max Verstappen', 437),
        fetch_driver_data('Charles Leclerc', 356),
        fetch_driver_data('Lando Norris', 374),
        )

    sorted_drivers = sorted(drivers, key=lambda d: d.points, reverse=True)

    for index, driver in enumerate(sorted_drivers, start=1):
        print(f"{index}. {driver.info()}")
        
asyncio.run(main())