import json
import os
import importlib.resources as pkg_resources
import sys
import mysql.connector
from dotenv import load_dotenv
import urllib.parse
import urllib.request
import requests
from datetime import datetime
import time
import asyncio
import aiohttp

from databaseInsert import DatabaseInsert

# Parse the JSON object
# Parse JSON data


async def process_data(data):
    # Your data processing logic here
    # ...

    # Create a session to make asynchronous HTTP requests
    async with aiohttp.ClientSession() as session:
        # Make the HTTP request
        response = await session.get(
            f"https://backend.production.omeda-aws.com/api/public/get-matches-since/{current_epoch}/"
        )
        json_response = await response.json()
        if len(json_response) == 0:
            timestamp = current_epoch + 3600
            with open("CurrentEpoch.json", "w") as file:
                # Write the data to the JSON file
                json.dump({"current_epoch": timestamp}, file)
            await asyncio.sleep(1)
            return

        last_match = json_response[-1]

        # ...
        # Perform your database operations here
        DatabaseInsert(json_response)
        # ...

        await asyncio.sleep(1)  # Delay between requests


async def main():
    response = True

    current_epoch = True
    while response:
        with open("CurrentEpoch.json") as f:
            epoch = json.load(f)
        current_epoch = epoch["current_epoch"]

        # Connect to the database
        load_dotenv()
        MYSQL_PW = os.getenv("MYSQL_PW")

        # Make the initial HTTP request
        async with aiohttp.ClientSession() as session:
            response = await session.get(
                f"https://backend.production.omeda-aws.com/api/public/get-matches-since/{current_epoch}/"
            )
            json_response = await response.json()

        if len(json_response) == 0:
            timestamp = current_epoch + 3600
            with open("CurrentEpoch.json", "w") as file:
                # Write the data to the JSON file
                json.dump({"current_epoch": timestamp}, file)
            await asyncio.sleep(1)
            continue

        last_match = json_response[-1]

        # -----------
        # for match in json_response:
        #     set_null_values(match)
        # # ------------
        dt = datetime.strptime(last_match["endTime"], "%Y-%m-%d %H:%M:%S")

        timestamp = int(dt.timestamp())
        with open("CurrentEpoch.json", "w") as file:
            # Write the data to the JSON file
            json.dump({"current_epoch": timestamp}, file)

        # Create tasks for processing data asynchronously
        tasks = []
        for data in json_response:
            tasks.append(process_data(data))

        # Execute tasks concurrently
        await asyncio.gather(*tasks)

        # Commit the changes and close the cursor and database connection

        await asyncio.sleep(3)


# Run the main function asynchronously
asyncio.run(main())
