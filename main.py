import asyncio
import aiohttp
import logging
import sys
from pymazda.client import Client as MazdaAPI

EMAIL = ""
PSSWD = ""

async def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    logger.debug(f"Python version info: {sys.version}")
    timeout = aiohttp.ClientTimeout(total=15)
    connector = aiohttp.TCPConnector(force_close=True)
    #make sure to setup proxy if desired
    websession = aiohttp.ClientSession(timeout=timeout, connector=connector, trust_env=True)
    # Initialize API client (MNAO = North America)
    client = MazdaAPI(EMAIL, PSSWD, "MNAO", websession=websession)

    # Get list of vehicles from the API (returns a list)
    vehicles = await client.get_vehicles()

    # Loop through the registered vehicles
    for vehicle in vehicles:
        # Get vehicle ID (you will need this in order to perform any other actions with the vehicle)
        vehicle_id = vehicle["id"]

        # Get and output vehicle status
        status = await client.get_vehicle_status(vehicle_id)
        print(status)

        # Start engine
        
    # Close the session
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())