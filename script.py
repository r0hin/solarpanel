import asyncio
import asyncio
from bleak import BleakClient

# E4E4DE6F-B744-25D4-825D-D6570D65505C
# Name: SmartSolar HQ21373YXAC
# Address: E4:D9:E2:93:2C:0B

# mac address: e4:5f:01:13:79:7b

address = "E4:D9:E2:93:2C:0B"
uuid = "9DF9212F-3A4E-55AB-9C54-1E2E888EDDE1"

async def main(address):
    async with BleakClient(address) as client:
      print("Connected")

asyncio.run(main(address))